import pykakasi
import requests

import pandas as pd

from app.domain.schemas.stock_search_response import StockSearchResponse
from app.config import settings
import urllib.parse

from app.exceptions.app_exception import AppException


class StockUseCase:
    def __init__(self):
        pass

    def search_stocks(self, query: str) -> list[StockSearchResponse]:
        results = []
        # If the query is only Japanese, also search from CSV
        if all(ord(c) > 127 or c == ' ' for c in query):
            results += self._search_csv(query)
        # Always add API search results
        results += self._search_api(query)
        return results

    def _search_csv(self, query: str) -> list[StockSearchResponse]:
        results = []
        try:
            df = pd.read_csv("data_j.csv")
            # Partial match search for company name
            matched = df[df["銘柄名"].str.contains(query, na=False)]
            for _, row in matched.iterrows():
                code = str(row["コード"])
                name = row["銘柄名"]
                results.append(
                    StockSearchResponse(
                        symbol=code,
                        name=name,
                        yahoo_url=f"https://finance.yahoo.com/quote/{code}.T",
                        ir_bank_url=f"https://irbank.net/{code}",
                        buffett_code_url=f"https://www.buffett-code.com/company/{code}"
                    )
                )
        except Exception as e:
            pass
        return results

    def _search_api(self, query: str) -> list[StockSearchResponse]:
        kakasi = pykakasi.kakasi()
        kakasi.setMode("H", "a")  # Hiragana to ascii
        kakasi.setMode("K", "a")  # Katakana to ascii
        kakasi.setMode("J", "a")  # Japanese to ascii
        kakasi.setMode("r", "Hepburn")  # Use Hepburn Romanization
        kakasi.setMode("s", True)  # Add space
        converter = kakasi.getConverter()
        
        converted_query = converter.do(query)
        url = settings.YAHOO_FINANCE_URL.format(query=converted_query)
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            res = requests.get(url, headers=headers)
            res.raise_for_status()
        except requests.RequestException as e:
            raise AppException(f"Yahoo Finance API request failed: {e}")
        data = res.json()

        allowed_exchanges = {"JPX", "NYQ", "NMS", "NASDAQ", "NYSE"}
        return [
            StockSearchResponse(
                symbol=item["symbol"],
                name=item.get("longname", item.get("shortname", "")),
                yahoo_url=f"https://finance.yahoo.com/quote/{item['symbol']}",
                ir_bank_url=f"https://irbank.net/{item['symbol']}",
                buffett_code_url=f"https://www.buffett-code.com/company/{item['symbol']}"
            )
            for item in data.get("quotes", [])
            if item.get("exchange") in allowed_exchanges
        ]

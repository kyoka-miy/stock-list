class NumberUtils:
    @staticmethod
    def get_percent_and_round(val):
        if isinstance(val, (int, float)):
            return round(val * 100, 2)
        return None

    @staticmethod
    def get_round(val):
        if isinstance(val, (int, float)):
            return round(val, 2)
        return None
    
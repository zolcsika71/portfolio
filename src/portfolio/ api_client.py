import requests
from typing import Optional

class DanelfinAPIClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"x-api-key": self.api_key}

    def _get(self, endpoint: str, params: Optional[dict] = None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            return None

        try:
            data = response.json()
        except ValueError:
            print("Failed to parse JSON response.")
            return None

        return data

    def get_historical_data_for_ticker(self, ticker: str):
        params = {"ticker": ticker}
        return self._get("ranking", params)

    def get_top_100_tickers_for_date(self, date_str: str):
        params = {"date": date_str}
        return self._get("ranking", params)

    def get_ticker_data_for_date(self, ticker: str, date_str: str):
        params = {"date": date_str, "ticker": ticker}
        return self._get("ranking", params)

    def get_values_by_score_for_date(self, date_str: str, aiscore: int):
        params = {"date": date_str, "aiscore": str(aiscore)}
        return self._get("ranking", params)

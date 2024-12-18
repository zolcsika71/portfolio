import time
import requests
from typing import Optional


class DanelfinAPIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.headers = {"x-api-key": self.api_key}


    def _get(self, params: Optional[dict] = None):
        url = f"{self.base_url}"
        params = {} if params is None else params
        response = None
        print(f"URL: {url}")
        print(f"Headers: {self.headers}")
        print(f"Params: {params}")
        for _ in range(5):
            try:
                response = requests.get(url, headers=self.headers, params=params, timeout=10)
                response.raise_for_status()
                print("Response Code: OK")
                return response.json()
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:
                    print("Rate limit exceeded.")
                    break
                print(f"HTTP Error: {e} Status Code: {response.status_code}")
            except requests.exceptions.RequestException as err:
                print(f"Request Error: {err}")
        print("Failed to retrieve data after multiple attempts.")
        return None

    def get_historical_data_for_ticker(self, ticker: str):
        params = {"ticker": ticker}
        return self._get(params)

    def get_top_100_tickers_for_date(self, date_str: str):
        params = {"date": date_str}
        return self._get(params)

    def get_ticker_data_for_date(self, ticker: str, date_str: str):
        params = {"date": date_str, "ticker": ticker}
        return self._get(params)

    def get_values_by_score_for_date(self, date_str: str, scoring_type: str, score: float):
        params = {"date": date_str, "type": scoring_type, "score": score}
        return self._get(params)




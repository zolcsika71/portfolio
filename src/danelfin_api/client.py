import requests
from typing import Optional


class DanelfinAPIClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"x-api-key": self.api_key}

    def _get(self, params: Optional[dict] = None):
        url = f"{self.base_url}"
        params = {} if params is None else params
        max_tries = 5
        delay = 1  # seconds

        for _ in range(max_tries):
            try:
                print(f"Sending GET request to {url} with params: {params}")
                response = requests.get(self.base_url, headers=self.headers, params=params, timeout=10)
                print(f"Response Code: {response.status_code}")
                response.raise_for_status()
                return response.json()
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:
                    print("Rate limit exceeded. Retrying in", delay, "seconds...")
                    time.sleep(delay)
                    delay *= 2
                    continue
                print(f"HTTP Error: {e}")
            except requests.exceptions.RequestException as err:
                print(f"Request Error: {err}")

        print("Failed to retrieve data after multiple attempts.")
        return None

    def _get(self, params: Optional[dict] = None):
        url = f"{self.base_url}"
        params = {} if params is None else params
        try:
            print(f"Sending GET request to {url} with params: {params}")
            response = requests.get(self.base_url, headers=self.headers, params=params, timeout=10)
            print(f"Request URL: {response}")
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
        return self._get(params)

    def get_top_100_tickers_for_date(self, date_str: str):
        params = {"date": date_str}
        return self._get(params)

    def get_ticker_data_for_date(self, ticker: str, date_str: str):
        params = {"date": date_str, "ticker": ticker}
        return self._get(params)

    def get_values_by_score_for_date(self, date_str: str, aiscore: int):
        params = {"date": date_str, "aiscore": str(aiscore)}
        return self._get(params)
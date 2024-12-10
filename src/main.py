from src.danelfin_api.client import DanelfinAPIClient
from src.danelfin_api.config import DANELFIN_API_KEY, BASE_URL, TICKER, DATE, AI_SCORE
from datetime import datetime


def display_data(title: str, data: dict):
    print(f"\n{title}:")
    print(data)


if __name__ == "__main__":
    print("Welcome to the Danelfin API Client!")
    print(f"Using API Key: {DANELFIN_API_KEY}")
    print(f"Using Base URL: {BASE_URL}")
    print(f"Using Ticker: {TICKER}")
    print(f"Using Date: {DATE}")
    print(f"AI_SCORE: {AI_SCORE}")

    client = DanelfinAPIClient(api_key=DANELFIN_API_KEY, base_url=BASE_URL)



    print("-" * 50)
    print(f"Historical Data for: {TICKER}")
    display_data(f"Historical Data for {TICKER}", client.get_historical_data_for_ticker(TICKER))

    print("-" * 50)
    print(f"Top 100 Tickers for {DATE}:")
    display_data("Top 100 Tickers for", client.get_top_100_tickers_for_date(DATE))

    print("-" * 50)
    print(f"Ticker Data for: {DATE} and {TICKER}")
    # Correct function call with proper method
    display_data("Ticker Data for date and ticker:",
                 client.get_ticker_data_for_date(TICKER, DATE))

    parameter = ('2024-01-02', 'aiscore', 10)
    print("-" * 50)
    values_by_score = client.get_values_by_score_for_date("2024-01-02", 10)
    display_data("Values by AIScore=10 for 2024-01-02", values_by_score)

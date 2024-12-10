from src.danelfin_api.config import DANELFIN_API_KEY, BASE_URL, TICKER, DATE, SCORE, TYPE, DANELFIN_MAX_TRY, DANELFIN_DELAY
from src.danelfin_api.client import DanelfinAPIClient

if __name__ == "__main__":

    def display_data(title: str, data: dict):
        print(f"\n{title}:")
        print(data)

    print("Welcome to the Danelfin API Client!")
    print(f"Using Base URL: {BASE_URL}")
    print(f"Using Ticker: {TICKER}")
    print(f"Using Date: {DATE}")
    print(f"Using AI Type: {TYPE}")
    print(f"AI SCORE: {SCORE}")
    print(f"max_retries: {DANELFIN_MAX_TRY}")
    print(f"delay: {DANELFIN_DELAY}")

    client = DanelfinAPIClient(api_key=DANELFIN_API_KEY, base_url=BASE_URL, max_retries=DANELFIN_MAX_TRY, delay=DANELFIN_DELAY)

    print("-" * 100)
    display_data(f"Historical Data for {TICKER}", client.get_historical_data_for_ticker(TICKER))

    print("-" * 100)
    print(f"Top 100 Tickers for {DATE}:")
    display_data(f"Top 100 Tickers for {DATE}:", client.get_top_100_tickers_for_date(DATE))

    print("-" * 100)
    print(f"Ticker: {TICKER} and Date: {DATE}")
    display_data("Ticker Data for date and ticker:", client.get_ticker_data_for_date(TICKER, DATE))

    print("-" * 100)
    print(f"Values by ScoreType on Date: {DATE}, Type: {TYPE}, Score: {SCORE}")
    display_data("Values by ScoreType on Date", client.get_values_by_score_for_date(DATE, TYPE, SCORE))


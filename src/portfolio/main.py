from src.portfolio.api_client import DanelfinAPIClient
from src.portfolio.config import DANELFIN_API_KEY, BASE_URL


def display_data(title: str, data):
    print("\n" + "="*50)
    print(title)
    print("="*50)
    if data is None:
        print("No data available or an error occurred.")
        return

    if isinstance(data, list):
        for idx, item in enumerate(data, start=1):
            print(f"{idx}. {item}")
    elif isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(data)

if __name__ == "__main__":
    client = DanelfinAPIClient(api_key=DANELFIN_API_KEY, base_url=BASE_URL)

    historical_data = client.get_historical_data_for_ticker("PYPL")
    display_data("Historical Data for PYPL", historical_data)

    top_100_data = client.get_top_100_tickers_for_date("2024-01-02")
    display_data("Top 100 Tickers for 2024-01-02", top_100_data)

    ticker_data_for_date = client.get_ticker_data_for_date("PYPL", "2024-01-02")
    display_data("Ticker Data for PYPL on 2024-01-02", ticker_data_for_date)

    values_by_score = client.get_values_by_score_for_date("2024-01-02", 10)
    display_data("Values by AIScore=10 for 2024-01-02", values_by_score)

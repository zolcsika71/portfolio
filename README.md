*** PORTFOLIO CREATOR ***

** Using danelfin API ***

- Ticker historical data:
curl -H 'x-api-key: THE_API_KEY_CREATED' "https://apirest.danelfin.com/ranking?ticker=PYPL"

- All data in a day (Top 100 tickers):
curl -H 'x-api-key: THE_API_KEY_CREATED' "https://apirest.danelfin.com/ranking?date=2024-01-02"

- Ticker data in a day:
curl -H 'x-api-key: THE_API_KEY_CREATED' "https://apirest.danelfin.com/ranking?date=2024-01-02&ticker=PYPL"

- Value by score type in a day:
curl -H 'x-api-key: THE_API_KEY_CREATED' "https://apirest.danelfin.com/ranking?date=2024-01-02&aiscore=10"
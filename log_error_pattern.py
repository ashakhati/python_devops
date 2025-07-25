import requests
log_url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs"

try:
    response = requests.get(log_url)
    logs = response.text.splitlines()
    for log in logs:
        if '404' in log:
            print(log)
except requests.exceptions.RequestException as e:
    print(f"Error fetching logs: {e}")

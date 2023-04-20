from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
    "type": "service_account",
    "project_id": "lunar-temple-382122",
    "private_key_id": "7c1b2c71a609bfe89df9e324736c37513ae2b641",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDOoP7kiezR0rBK\nCNqunpWE7nmcr4SCdvHcyaYnvfocXWo3nH5mImVOSvDaGFR3lJen7xYFyFCWrPSs\n/kQAmD6TyOlV5A+t09TsflWNNYx+y2hDqPygep/6UxHm9/gQLgV7qo3dbUcBdNxP\npMQiL+P9HGzwtwctRd37FmepbwOd7K3Tq53jJM8Tw4HTbwr+suchJ8+WTcb5g/jh\nadNpymHF+N0HJ9fm+2ndZHLvVqqX2Yzee21NQGv/ra9mu5MZcKV9SSLBVB5J+UvH\nZ5jUb6J8mwphUWrl5IOLEL/l2CNPix0VbGnvQwOrqR4n4ztEwvYEUPShZN0S8ByU\naLkSVYb7AgMBAAECggEAPwfGaUGXj5Pk+diEmMLAWnoCd+Tkl4WgFtkeSb4+Ztuq\nFIe02QQCAiWDHgxQ699UecJJZf8qciQVSRYQ+Vt3r04Yu34juENHjtKk1zvv/Reg\nWQ9Z7LwrQ8mGSv32Wj0nqAcpWlPE1rFmqRbaS5FvSx0aMD2sv0cyRS8a9QjrwgbN\nsNwvQaWKoxz1t8w6YZ3LzyHu1Pm+FE8B8wxEpqOsQkVSdgoShfis9BSL/QGyuqdG\nmgGdEObCbaPN6v0CqGj94d6loST6oNjKHgyp4ghr3Wzy6k2HpJik8MHgITmiK4sP\nGtqbsTFJgzdlYYmosqKStnsKKkN0W7sW2rF9EVsduQKBgQDxC+62oH/voQ+XahfK\nIQrO3gaJBm+TN2fyL7pOs9kRihR2VQMKvWyQb63+zrynQwud6TH6Dc47aNO2EOdM\nMLhbzRMgjR8BPwFX2Rha6Yda1wQ2hzPMdT+roX8HMagOeMqkxjU1v5BSvQ55fqP8\n7aA4spbjJ1H8EJCB4/dWbM8kIwKBgQDbcnl2Rg8scFUhx2dmFJiZ5IONLCAccFod\nzqRwa/LZ82fsQidAuxvH1KLuTAdk4pEn0S3hD4sKe0dC4s/HyLeXtQ61bnvQsU/z\nysb5PvO0IU4QCnAPoC4xsU3xmN7VC9pi4xVxFCkBIEcN732kNDLwu38d1izkQm1M\ncB3lnB3zSQKBgQCZwJ28mfXhGOAEGeUgxiDJwS9z+cnzonTIM49oIinEmUniDOnK\n0PbNzp6ymJYXLpnbWOLK+EFi/cOFL5UJsU33KIEZ00pClji6Gz0AyFLRK7OBQI5W\nzTcWuAV5xj/HM1826UMJjK53SCZScugRLlVztN6v9+XAnaQ/ZfTfiLo79wKBgQDK\nG+FgG+BHtmHBzYweiSOOwNakA5rDdnqY70OlwtYVA8eX4cmTJYDNh7pTrLQ2pzC3\nMkGGAbG2Apo8MPba8rKcR4X3dX0VVOjlCMI+tkrvgKkLvwE8cvN4kurNc1TvdI46\n+xg5YC7vuZGXdRYLUIQGETle+m24ALH3b18ppKI0+QKBgHMBT1dIi4+p6qm85RNH\nCspDzJJlVLgRkIcKZmvb9gLO8Gxn0a7g0qcQifaIQZLdi0jsM6HA2uJwIS3Dsn86\nfRs2aLlzkk4wO4pIgwipcowrFfvHui25GOYpgm3qExV2TYko+2jpU4/+Aje0uXnR\nfEs/t/MwTJGSz32AJYZr8OT6\n-----END PRIVATE KEY-----\n",
    "client_email": "371655092907-compute@developer.gserviceaccount.com",
    "client_id": "103301982757574639893",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/371655092907-compute%40developer.gserviceaccount.com"
}

try:
    res = requests.get(f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    
    print("Loading...")
    
    soup = BeautifulSoup(res.text, 'html.parser')
    
    info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
    
    print(info)
    
    """Uploads a file to the bucket."""
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket('weather__sp')
    blob = bucket.blob('weather_info.txt')
    
    blob.upload_from_string(info + '\n')
    
    print('File uploaded.')
    
    print("Finished.")
except Exception as ex:
    print(ex)

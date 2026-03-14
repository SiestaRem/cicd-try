import requests
def main():
    try:
        url = "www.baidu.com"
        response = requests.get(url)
        print(response.text)
    except :
        print(f"request error occurred")
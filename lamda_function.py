import requests

def runNasaApi():
    url = "http://localhost:8000/api/send-apod"
    try:
        r = requests.get(url)
        return r.json()
    except Exception as e:
        return None

def lambda_handler(event, context):
    return runNasaApi()

if __name__ == "__main__":
    lambda_handler(None, None)
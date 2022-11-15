import requests

def lambda_handler(event, context):
    try:
        res = requests.get("http://localhost:8000/api/send-apod")
        return res.json()
    except Exception as e:
        return None

if __name__ == "__main__":
    lambda_handler(None, None)
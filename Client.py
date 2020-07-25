import requests

if __name__ == "__main__":
    response = requests.post('http://localhost:5000/complaint', json={"message":"water quality is poor"})
    print(response.status_code)
    print(response.json())



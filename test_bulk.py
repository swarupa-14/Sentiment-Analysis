import requests

url = "http://127.0.0.1:5000/predict"

files = {'file': open('test_sentences.csv', 'rb')}

response = requests.post(url, files=files)

if response.status_code == 200:
    with open('Predictions.csv', 'wb') as f:
        f.write(response.content)
    print("Bulk prediction successful, saved as Predictions.csv")
else:
    print("Error:", response.text)

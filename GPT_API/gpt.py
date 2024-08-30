import requests
import json

api_key = "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"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}


data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "hi, GPT-4!"},
    ]
}


response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    data=json.dumps(data)
)

if response.status_code == 200:
    response_data = response.json()
    print(response_data['choices'][0]['message']['content'])
else:
    print("wrong:", response.status_code, response.text)
print(response.status_code)
print(response.text)
response = requests.get(
    "https://api.openai.com/v1/usage",
    headers=headers
)

print(response.status_code)
print(response.text)


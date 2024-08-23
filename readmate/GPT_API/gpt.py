import requests
import json


def call_gpt3(api_key, prompt):
    api_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(api_key),
    }
    payload = {
        "prompt": prompt,
        "max_tokens": 50
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)
        return None


if __name__ == "__main__":
    api_key = "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"
    prompt = "Translate the following English text to French: 'Hello, how are you?'"
    result = call_gpt3(api_key, prompt)
    if result:
        print(result['choices'][0]['text'])

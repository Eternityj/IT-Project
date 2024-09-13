import requests

api_key = "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"

def ask_gpt_with_current_page(book_content, user_question):
    try:
        headers = {
            'Authorization': 'Bearer {}'.format(api_key),
            'Content-Type': 'application/json',
        }

        data = {
            "model": "gpt-3.5-turbo",  # Update to a supported model
            "messages": [
                {"role": "system", "content": "You are a helpful assistant with deep knowledge about books."},
                {"role": "user", "content": "Here is an excerpt from a book: {}. Now answer this question: {}".format(book_content, user_question)}
            ],
            "max_tokens": 150
        }

        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

        if response.status_code == 200:
            response_json = response.json()
            return response_json['choices'][0]['message']['content'].strip()
        else:
            return "Error: {} - {}".format(response.status_code, response.text)

    except Exception as e:
        return "Error occurred: {}".format(str(e))


import requests

api_key = 'your own key'
headers = {
           "Authorization": f"Bearer {api_key}",
           "Context-Type": "application/json"
          }
url = "https://api.openai.com/v1/chat/completions"
while True:
    prompt = input('Ask something: ')
    data = {
              "model": "gpt-3.5-turbo",
              "messages": [
                {
                "role":"user",
                "content":prompt
                }
              ]
            }

    response = requests.post(url, headers=headers, json = data)
    answer = response.json()['choices'][0]['message']['content']
    print(f'{answer}\n{"~"*100}')

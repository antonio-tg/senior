import requests
import openai

openai.api_key = 'your own key'

while True:
    prompt = input('Ask someting: ')

    if prompt == 'exit':
        break
    completion = openai.Completion.create(engine='text-davinci-003',prompt=prompt, n=1, max_tokens=2048)

    answer = completion.choices[0].text
    print(f'{answer}\n{"~"*100}')

print('It is always a pleasure to help you')

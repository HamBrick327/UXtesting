import requests
import json
from os import getenv
from openai import OpenAI

log = open("output.txt", 'a')
apiKey = getenv("OPENAIKEY2")
print(f'using {apiKey}')


def openaiGenerate(prompt):
    client = OpenAI(api_key=apiKey)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
    )
    return completion.choices[0].message

# 
# response = requests.get(f'https://api.api-ninjas.com/v1/jokes?limit={1}', headers={'X-Api-Key' : "FWIYfCodkizNPtWSfjMNYw==BpZw8KgtJ4foUCyJ"})
# 
# if response.status_code == requests.codes.ok:
    # response = json.loads(response.text)
    # print(response[0]['joke'])

response = openaiGenerate("gaming")
print()
print(response.content)
print()
log.write(str(response) + '\n')
log.write(str(response.content))
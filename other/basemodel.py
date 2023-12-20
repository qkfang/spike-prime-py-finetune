import os
import re
from openai import AzureOpenAI

def robotCommand(questionText):
  f = open('v6/training-set.dt', 'r')
  data= f.read()
  f.close()

  blocks = re.split('###', data)

  messages = []
  systemMsg = {"role":"system","content": blocks[0].split('\n')[1]}
  messages.append(systemMsg)

  for block in blocks[1:]:
    userMsg = block.split('\n')[1]
    assistMsg=""
    for blockUser in block.split('\n')[2:]:
      assistMsg += blockUser + '\n'
    messages.append({"role": "user", "content": userMsg}) 
    messages.append({"role": "assistant", "content": assistMsg})

  # print(messages)


  client = AzureOpenAI(
    azure_endpoint = "https://oai-test-666.openai.azure.com/", 
    api_key="65c1efa7e30b41d4814f0492f9837940",  
    api_version="2024-02-15-preview"
  )

  question = {"role":"user", "content": questionText}
  messages.append(question)

  completion = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name"
    messages = messages,
    temperature=0,
    max_tokens=800,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
  )

  print('###')
  print(questionText)
  print(completion.choices[0].message.content)
  print('')
import os
import re
import json
from openai import AzureOpenAI

with open(r'config.json') as config_file:
    config_details = json.load(config_file)

def chat(modelName, systemPrompt, userMessage):
  messages = []
  systemMsg = {"role":"system","content": systemPrompt}
  messages.append(systemMsg)

  question = {"role":"user", "content": userMessage}
  messages.append(question)

  client = AzureOpenAI(
    azure_endpoint = config_details["OPENAI_API_BASE"],
    api_key = config_details["OPENAI_API_KEY"],  
    api_version="2024-02-15-preview"
  )

  completion = client.chat.completions.create(
    model= modelName, # model = "deployment_name"
    messages = messages,
    temperature=0,
    max_tokens=800,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
  )

  print('###')
  print(userMessage)
  print(completion.choices[0].message.content)
  print('')
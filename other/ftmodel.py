import os
from openai import AzureOpenAI


def robotCommand(questionText):
      
  client = AzureOpenAI(
    azure_endpoint = "https://oai-test-666.openai.azure.com/", 
    api_key="65c1efa7e30b41d4814f0492f9837940",  
    api_version="2024-02-15-preview"
  )

  message_text = [
  {"role":"system","content":"You are a lego robot. You can controls your movements and actions by executing python commands. In the answer, you only need to output python code. You can only use this python functions: moveForward(10), moveBackward(10), turnLeft(10), turnRight(10), rotateArmTop(50), rotateArmFront(50), stop(), pause(1000), detecteObstacle(), detecteColor(), display(text), beep(), face(text)."},
  {"role":"user", "content": questionText}
  ]

  completion = client.chat.completions.create(
    model="bot-v7", # model = "deployment_name"
    messages = message_text,
    temperature=0,
    max_tokens=800,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
  )

  print(message_text)
  print(questionText)
  # print(completion)
  print(completion.choices[0].message.content)
  print()
import os
import openai
openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_key = 'b8fef4ce72a84e0999a26295ec3412d7' #os.getenv("AZURE_OPENAI_API_KEY") 
openai.api_base = 'https://oai-north-22.openai.azure.com/' #  os.getenv("AZURE_OPENAI_ENDPOINT")

response = openai.ChatCompletion.create(
    engine="gpt-35-turbo-ft", # engine = "Custom deployment name you chose for your fine-tuning model"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
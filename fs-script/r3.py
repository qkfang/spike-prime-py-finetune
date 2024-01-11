# Upload fine-tuning files
import openai
import os

openai.api_key = 'b8fef4ce72a84e0999a26295ec3412d7' #os.getenv("AZURE_OPENAI_API_KEY") 
openai.api_base = 'https://oai-north-22.openai.azure.com/' #  os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = 'azure'
openai.api_version = '2023-12-01-preview' # This API version or later is required to access fine-tuning for turbo/babbage-002/davinci-002

training_file_name = 'training_set.jsonl'
validation_file_name = 'validation_set.jsonl'

# Upload the training and validation dataset files to Azure OpenAI with the SDK.

training_response = openai.File.create(
    file=open(training_file_name, "rb"), purpose="fine-tune", user_provided_filename="training_set.jsonl"
)
training_file_id = training_response["id"]

validation_response = openai.File.create(
    file=open(validation_file_name, "rb"), purpose="fine-tune", user_provided_filename="validation_set.jsonl"
)
validation_file_id = validation_response["id"]

print("Training file ID:", training_file_id)
print("Validation file ID:", validation_file_id)


# Training file ID: file-de0ad6cf499a4e0f8b6ba1b3b3a5899e
# Validation file ID: file-a0dccb2c14b34d08885c6b43ec7db906

import openai

openai.api_key = 'b8fef4ce72a84e0999a26295ec3412d7' #os.getenv("AZURE_OPENAI_API_KEY") 
openai.api_base = 'https://oai-north-22.openai.azure.com/' #  os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = 'azure'
openai.api_version = '2023-12-01-preview' # This API v

response = openai.FineTuningJob.create(
    training_file='file-de0ad6cf499a4e0f8b6ba1b3b3a5899e',
    validation_file='file-a0dccb2c14b34d08885c6b43ec7db906',
    model="gpt-35-turbo-0613",
)

job_id = response["id"]

# You can use the job ID to monitor the status of the fine-tuning job.
# The fine-tuning job will take some time to start and complete.

print("Job ID:", response["id"])
print("Status:", response["status"])
print(response)
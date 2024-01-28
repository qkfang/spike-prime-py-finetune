# Track training status

import openai

openai.api_key = 'b8fef4ce72a84e0999a26295ec3412d7' #os.getenv("AZURE_OPENAI_API_KEY") 
openai.api_base = 'https://oai-north-22.openai.azure.com/' #  os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = 'azure'
openai.api_version = '2023-12-01-preview' # This API v


from IPython.display import clear_output
import time

# Job ID: ftjob-13fcdd4548f64f5da56491657bf0276f
# Status: pending
# {
#   "hyperparameters": {
#     "n_epochs": -1,
#     "batch_size": -1,
#     "learning_rate_multiplier": 1
#   },
#   "status": "pending",
#   "model": "gpt-35-turbo-0613",
#   "training_file": "file-de0ad6cf499a4e0f8b6ba1b3b3a5899e",
#   "validation_file": "file-a0dccb2c14b34d08885c6b43ec7db906",
#   "id": "ftjob-13fcdd4548f64f5da56491657bf0276f",
#   "created_at": 1709443606,
#   "updated_at": 1709443606,
#   "object": "fine_tuning.job"
# }

start_time = time.time()
job_id='ftjob-13fcdd4548f64f5da56491657bf0276f'

# Get the status of our fine-tuning job.
response = openai.FineTuningJob.retrieve(job_id)

status = response["status"]

# If the job isn't done yet, poll it every 10 seconds.
while status not in ["succeeded", "failed"]:
    time.sleep(10)
    
    response = openai.FineTuningJob.retrieve(job_id)
    print(response)
    print("Elapsed time: {} minutes {} seconds".format(int((time.time() - start_time) // 60), int((time.time() - start_time) % 60)))
    status = response["status"]
    print(f'Status: {status}')
    clear_output(wait=True)

print(f'Fine-tuning job {job_id} finished with status: {status}')

# List all fine-tuning jobs for this resource.
print('Checking other fine-tune jobs for this resource.')
response = openai.FineTuningJob.list()
print(f'Found {len(response["data"])} fine-tune jobs.')
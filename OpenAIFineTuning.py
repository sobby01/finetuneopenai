import os
import openai

openai.api_key = "your_key"

model_engine = "davinci"
n_epochs = 15
batch_size = 3
learning_rate = 0.3
max_tokens = 1024

# Create the fine-tuning job
fine_tuning_job = openai.FineTune.create(
    model=model_engine,
    n_epochs=n_epochs,
    batch_size=batch_size,
    learning_rate_multiplier=learning_rate,
    training_file = "file-tYfedsdfeqrFSVCB4y65Wja",
    validation_file = "file-oWdrererUlnCbTkq678BU"
)

job_id = fine_tuning_job["id"]
print("Fine-tuning job created with ID: {}".format(job_id))
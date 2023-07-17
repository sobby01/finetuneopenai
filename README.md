# OpenAI Fine-Tune Scripts

This repository contains Python scripts for fine-tuning OpenAI models using the OpenAI API.

## Prerequisites

Before running the scripts, make sure you have the following:

1. OpenAI API Key: You will need to sign up for an OpenAI account and obtain an API key.

2. Python: The scripts are written in Python, so you should have Python installed on your system. Python3 is required

3. openai Library: Install the `openai` library using the following command:
```python
   pip install openai
```
   
## Getting Started

1. Set the OpenAI API key in the script. Replace `"your_key"` with your actual API key:
```python
import openai
openai.api_key = "your_key"
```
2. Prepare your training data in Jsonl format

{"prompt": "<prompt text>", "completion": "<text>"}
{"prompt": "<prompt text>", "completion": "<text>"}
{"prompt": "<prompt text>", "completion": "<text>"}

3. Validate this data using :
```python
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>
```
This will ask you to add separators at the end of prompts and completion.

4. Upload the JSONL data set file to OpenAI using the following code
```python
 response = openai.File.create(
  file=open("D:\\Pythongscripts\\finetune\\os-helptext2-finetune_prepared.jsonl", "rb"),
   purpose='fine-tune'
 )

 print(response)

#sample response
# {
#   "object": "file",
#   "id": "file-trtyCCfrt678Y7dFSVCB4GTUWja",
#   "purpose": "fine-tune",
#   "filename": "file",
#   "bytes": 13126,
#   "created_at": 1689582512,
#   "status": "uploaded",
#   "status_details": null
# }
```
5. Note the previous response ID and pass it to open AI to train the model
```python

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
    training_file = "file-4235ertwreterY7dFSVCB4GTUWja",
    validation_file = "file-dfefdwerw4543trwertwtweeBU"
)

job_id = fine_tuning_job["id"]
print("Fine-tuning job created with ID: {}".format(job_id))
```

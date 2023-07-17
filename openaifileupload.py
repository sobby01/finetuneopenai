import os
import openai
openai.api_key = "your_key"
response = openai.File.create(
file=open("file_path, "rb"),
purpose='fine-tune'
)

print(response)
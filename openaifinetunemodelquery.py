import os
import openai
openai.api_key = "your_key"

response = openai.FineTune.retrieve(id="ft-pHedeeeef3eizNVW0bofVje3ez")
print(response)

#Sample Response : 
# {
#   "object": "file",
#   "id": "file-ddfdfee59Y7dFSVCB4GTUWja",
#   "purpose": "fine-tune",
#   "filename": "file",
#   "bytes": 13126,
#   "created_at": 1689582512,
#   "status": "uploaded",
#   "status_details": null
# }
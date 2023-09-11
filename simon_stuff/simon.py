import vertexai
from vertexai.preview.language_models import TextGenerationModel

filename = "simon.txt"

with open(filename,'r') as file:
    json_string = file.read()

print(json_string)

vertexai.init(project="gen-ai-sandbox", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """The file contains some json formatted text, read the file and summarise what it contains. Do not skip anything. Put it in a nice list or tabular format for explanation. Here is the json file:""" + json_string,
    **parameters
)
print(f"Response from Model: {response.text}")
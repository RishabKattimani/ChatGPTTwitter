# ------------------------------------------------------------------------------
# Imports
import openai
import requests

# ------------------------------------------------------------------------------
# Setup
openai.api_key = "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"
model_engine = "text-davinci-003"

# ------------------------------------------------------------------------------
# Generating Response

prompt = input("enter your question here: ")

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

response = completion.choices[0].text
print(response)
# ------------------------------------------------------------------------------
# IFTTT

json = {"value1": response, "value2": prompt, "value3": "value3"}
requests.post('https://maker.ifttt.com/trigger/chatgpt_python/with/key/gKZRLSUmd340uHUslyzRYVhgYSBGnbw2WHCc97qm5zb', data=json)

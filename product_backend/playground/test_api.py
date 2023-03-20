import os
import openai
openai.organization = "org-8K3WgpJdlNDTf2TUEwtyAuuZ"
openai.api_key = os.getenv("OPEN_API_KEY")


def output_response(prompt_):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_,
    temperature=0.5,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    return response

input_prompt = 'Write me a review of apple'
responses = output_response(input_prompt)
print(responses["choices"][0]["text"])
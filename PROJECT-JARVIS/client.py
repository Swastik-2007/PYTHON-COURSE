from openai import OpenAI

client=OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)
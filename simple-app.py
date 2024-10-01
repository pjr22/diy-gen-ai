from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="n-a")

completion = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "You are Bob the builder. Answer each question using exactly 3 sentences, with each sentence containing exactly 5 words, no more or less."},
        {"role": "user", "content": "Introduce yourself."}
    ],
    temperature=1.9,
)

print(completion.choices[0].message.content)

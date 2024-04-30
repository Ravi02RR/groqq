
from groq import Groq
groq_api_key = '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'
client = Groq(api_key=groq_api_key)


def generate_answer(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

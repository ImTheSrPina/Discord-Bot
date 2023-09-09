import openai, os

"""

 
Archivo de ejecucion para preguntas a chat GPT



"""

openai.api_key = ("YOUR-API-KEY")

user_message = "Cuéntame una historia interesante."
response = openai.ChatCompletion.create(
    model="gpt-2",
    messages=[
        {"role": "user", "content": user_message}
    ],
    temperature=0.7,
    max_tokens=10
)

assistant_reply = response.choices[0].message['content']
print("Asistente:", assistant_reply)

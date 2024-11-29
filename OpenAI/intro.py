from openai import OpenAI
import getpass

client = OpenAI(
    api_key = getpass.getpass("Ingresa tu API Key de OpenAI : ")
)

model = "gpt-3.5-turbo-0125" #gpt-4o"

# Define el mensaje de entrada para el chat
prompt = "quién es Leonel Messi"
message_input = {
    'messages': [
        {'role': 'system', 'content': 'Eres un asistente virtual'}, #como tono divertido, rol
        {'role': 'user', 'content': prompt} #que deseo que me responda
    ]
}

# Realiza una solicitud a la API de OpenAI
response = client.chat.completions.create(
    model = model,
    messages = message_input['messages'],
    temperature = 0, #Si está más cercano a 1, es posible que tenga alucinaciones.
    n = 1, #Número de respuestas
    max_tokens = 200
)

# Imprime la respuesta del modelo
result = response.choices[0].message.content
print(result)

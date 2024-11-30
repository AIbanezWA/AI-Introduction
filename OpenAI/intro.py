from openai import OpenAI
import getpass #paquete para ofuscar (tipo de cifrado) los valores de las variables en tiempo de ejecución.

#variable para invocar todos lo métodos de OpenAI
client = OpenAI(
    api_key = getpass.getpass("Ingresa tu API Key de OpenAI : ")
)

#Indica con que modelo se va a trabajar, se recomienta utilizar los modelos de lenguaje más recientes.
model = "gpt-3.5-turbo-0125" #gpt-4o"

# Define una variable para almacenar el prompt en el chat.
prompt = "quién es Leonel Messi"
#variable que contiene un array de mensajes.
message_input = {
    'messages': [
        {'role': 'system', 'content': 'Eres un asistente virtual'}, #rol del sistema: Cómo quiero que me responda el sistema (en este caso un tono divertido).
        {'role': 'user', 'content': prompt} #rol del usuario: Qué deseo que me responda.
    ]
}

#Invoca al modelo de mensajes (chat) de OpenAI  => para imagenes (image)
response = client.chat.completions.create(
    model = model,
    messages = message_input['messages'],
    temperature = 0, # Si se desea que sea creativo es 1 y es posible que tenga alucinaciones. Se recomienda que sea 0.
    n = 1, #Número de respuestas
    max_tokens = 200 # Cuantos tokens va a recibir este modelo (entrada y salida)
)

# Imprime la primera respuesta del modelo
result = response.choices[0].message.content
print(result)

# DEMO #2: Calculando las tarifas por tokens de entrada y salida en chatGPT
# Reference: https://openai.com/pricing


from openai import OpenAI
import getpass, os

# Se define una variable de entorno para el API key.
os.environ["OPENAI_API_KEY"] = getpass.getpass("Ingresa tu API Key de OpenAI : ")

# Se define el modelo de lenguaje que se va a utilizar.
model_openai = "gpt-4o"

# Ya no es necesario utilizar la variable del API key como parámetro en la clase OpenAI. Internamente lo de la variable de entorno
client = OpenAI()

# Se define una función de cálculo de tarifa con 2 argumentos: uso (input/output) y el modelo.
def openai_api_calculate_cost(usage, model):
    # Se define un diccionario de clasificación
    pricing = {
        'gpt-3.5-turbo-0125': {
            'prompt': 0.0005,
            'completion': 0.0015
        },
        'gpt-4o': {
            'prompt': 0.005,
            'completion': 0.015
        }
    }

    try:
        model_pricing = pricing[model]
    except KeyError:
        raise ValueError("Modelo inválido")

    prompt_cost = usage['prompt_tokens'] * model_pricing['prompt'] / 1000
    completion_cost = usage['completion_tokens'] * model_pricing['completion'] / 1000

    total_cost = prompt_cost + completion_cost
    print(f"\nTokens usados:  {usage['prompt_tokens']:,} prompt + {usage['completion_tokens']:,} completion = {usage['total_tokens']:,} tokens")
    print(f"Total costo ({model}): ${total_cost:4f}\n")

    return total_cost

# Define el mensaje de entrada para el chat
prompt = "dame el código para usar la API de OpenAI con Python"
message_input = {
    'messages': [
        {'role': 'system', 'content': 'Eres un asistente virtual'},
        {'role': 'user', 'content': prompt}
    ]
}

# Realiza una solicitud a chatGPT con la API de OpenAI
response = client.chat.completions.create(
    model = model_openai,
    messages = message_input['messages'],
    temperature = 0, #Si está más cercano a 1, es posible que tenga alucinaciones.
    n = 1, #Número de respuestas
    max_tokens = 400
)

result = response.choices[0].message.content
print(result)

# Se declara un array para capturar la respuesta
data_usage = {
    "completion_tokens" : response.usage.completion_tokens, # número de tokens usados en la salida
    "prompt_tokens" :  response.usage.prompt_tokens, # número de tokens usados en el prompt (entrada)
    "total_tokens" : response.usage.total_tokens # número de tokens de entrada y salida
}

# Se invoca a la función de cálculo de la tarifa.
openai_api_calculate_cost(data_usage, model_openai)

# Curso : Creando aplicaciones con Inteligencia Artificial Generativa

Codespaces es un entorno de desarrollo integrado en la nube (basado en VS Code) que utiliza un contenedor para proporcionar lenguajes comunes, herramientas y utilidades para el desarrollo.

![image](https://user-images.githubusercontent.com/2066453/278680037-24cbb036-f0e0-4410-974d-eb04b36426c7.png)

Crear un Codespace, clic en Code -> Codespace -> Create codespace on master.

![image]([https://github.com/AIbanezWA/AI-Introduction/blob/main/Create%20codespace.png)

En el terminal de Codespaces ejecuta este comando para instalar las librerías necesarias para el curso:

Sesión 1: Copiar y pegar el siguiente comando en el prompt y pulsar enter para ejecutarlo

	pip install openai==1.35.10 streamlit==1.36.0 tiktoken==0.7.0 Pillow==10.3.0 langchain==0.2.6 langchain-community==0.2.6 langchain_openai==0.1.9 langchain_together==0.1.3 replicate==0.26.1 pinecone-client==4.1.1 pypdf==4.2.0 unstructured==0.14.8
 	python -m pip install --upgrade pip
  	echo "Completado"

Sesión 2: Copiar y pegar el siguiente comando en el prompt y pulsar enter para ejecutarlo

	pip install pydub==0.25.1 langchain-qdrant==0.1.1 langchain-google-genai==1.0.6 langchainhub==0.1.20 numexpr==2.10.1 langchain_experimental==0.0.61 faiss-cpu==1.8.0 qdrant-client==1.9.2 google-cloud-storage==2.17.0 tabulate==0.9.0 sqlalchemy==2.0.31 google-cloud-bigquery==3.25.0 google-cloud-bigquery-storage==2.25.0 langchain-google-vertexai==1.0.5 boto3==1.34.131 langchain-aws==0.1.7 sqlalchemy-bigquery==1.11.0

En el repositorio no se podrán subir cambios, para descargar los cambios ejecutar estos dos comandos en el terminal de Codespaces:

	git checkout -f
 	git pull

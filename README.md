# Sinapsis_IA

___________________________________________________________________________________
### Elaborado por:
Jose Ricardo Olarte Pardo

___________________________________________________________________________________
### Pre-requisitos

  - Python
  - Consola, preferencia Windows (No ensayado en linux)
  - IDLE de python, recomendación Pycharm
  - Pinecone, crear un AI Agent index

___________________________________________________________________________________
### Instalación

1. Clonamos el repositorio y accedemos desde la consola:
```
https://github.com/Ricardo-Olarte/Sinapsis_IA.git
```
```
cd Sinapsis_IA
```
2. Desde nuestra consola CMD, se realizará la instalación de librerías

```
pip install --upgrade pip
```
```
pip install langchain==0.0.331
```
```
pip install openai==0.27.8
```
```
pip install ChatOpenAI
```
```
pip install OpenAIEmbeddings
```
```
pip install Pinecone
```
```
pip install AgentType
```
```
pip install tool
```

3. Debemos tener en cuenta guardar en Windows la API Key y el enviroment del Agente IA index de Pinecone, en variables de entorno ó desde las configuraciones de Pycharm lo podemos realizar
```
$env:PINECONE_API_KEY = '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'
```
```
$env:PINECONE_ENVIRONMENT = 'gcp-starter'
```
4. Con el tool configurado podemos consultar los documentos, y así mismo, que nuestro agente 'challenge1' pueda respondernos

___________________________________________________________________________________
### Elaborado por:

* Jose Ricardo Olarte Pardo

___________________________________________________________________________________
### Autores:

* David Esteban Useche
* Santiago Velez

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool

import os
import pinecone

@tool("SayHello", return_direct=True)
def say_hello(name: str) -> str:
    """Answer when someone says hello"""
    return f"Hello {name}! My name is Sainapsis"

## @author Luis Benavides, modify by Ricardo Olarte
def main():
    pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENVIRONMENT'))
    embeddings = OpenAIEmbeddings()
    text = open("economia.txt", "r")
    #print(text.read())
    pinecone.create_index("challenge1", dimension=1536, metric="cosine")

    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='challenge1')
    text = open("economia.txt", "r")
    print(text)

    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='challenge1')
    text = open("ingenieria-civil.txt", "r")
    print(text)

    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='challenge1')
    text = open("ingenieria-electrica.txt", "r")
    print(text)

    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='challenge1')
    text = open("ingenieria-electronica.txt", "r")
    print(text)

    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='challenge1')
    text = open("ingenieria-industrial.txt", "r")
    print(text)

    data = Pinecone.from_texts(texts=text.readlines(), embedding=embeddings, index_name='challenge1')
    text = open("ingenieria-sistemas.txt", "r")
    print(text)

    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    print(agent.run("Hello! My name is RiCHi"))

def buscar():
    pinecone.init(api_key="PINECONE_API_KEY", environment="PINECONE_ENVIRONMENT")
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index("challenge1", embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de industrial?"
    docs = docsearch.similarity_search(query)
    print(docs)

if __name__ == '__main__':
    buscar()
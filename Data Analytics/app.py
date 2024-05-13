# Groq Integration

# import pandas as pd
# from pandasai import SmartDataframe
# from langchain_groq.chat_models import ChatGroq
# from langchain_community.llms import Ollama 
# import sqlite3
# import os

# llm = ChatGroq(model_name="llama3-70b-8192", api_key = os.environ["GROQ_API_KEY"])

# df = pd.read_excel('data.xlsx')
# df = SmartDataframe(df, config={"llm": llm})

# print( df.chat('Which are the 5 happiest countries?'))
# print( df.chat('What is the sum of the GDPs of the 2 happiest countries?'))


# Ollama Integration
# ollama pull llama3


# import pandas as pd
# from pandasai import SmartDataframe
# from langchain_groq.chat_models import ChatGroq
# from langchain_community.llms import Ollama 
# import sqlite3
# import os

# llm = Ollama(model="llama3")

# df = pd.read_excel('data.xlsx')
# df = SmartDataframe(df, config={"llm": llm})

# print( df.chat('Which are the 5 happiest countries?'))
# print( df.chat('What is the sum of the GDPs of the 2 happiest countries?'))


# Database Integration

# import pandas as pd
# from pandasai import SmartDataframe
# from langchain_groq.chat_models import ChatGroq
# from langchain_community.llms import Ollama 
# import sqlite3
# import os

# llm = Ollama(model="llama3")

# conn = sqlite3.connect('data.db')
# df = pd.read_sql('SELECT * FROM countries', conn)
# conn.close()
# df = SmartDataframe(df, config={"llm": llm})

# print( df.chat('Which are the 5 happiest countries?'))
# print( df.chat('What is the sum of the GDPs of the 2 happiest countries?'))


# User Interface Chatbot

# import pandas as pd
# import sqlite3
# # import seaborn as sns
# import chainlit as cl
# from openai import AsyncOpenAI
# from pandasai import SmartDataframe
# from langchain_community.llms import Ollama
# from langchain_groq.chat_models import ChatGroq 
# from dotenv import load_dotenv
# import sqlite3
# import os
# load_dotenv()


# llm = ChatGroq(model_name="llama3-70b-8192", api_key = os.environ["GROQ_API_KEY"])

# @cl.on_chat_start
# def start_chat():
#     # Set initial message history
#     cl.user_session.set(
#         "message_history",
#         [{"role": "system", "content": "You are a helpful assistant."}],
#     )

# @cl.on_message
# async def main(message: cl.Message):
#     # Retrieve message history
#     message_history = cl.user_session.get("message_history")
#     message_history.append({"role": "user", "content": message.content})

#     # Load data
#     # df = pd.read_excel('data.xlsx')
#     df = pd.read_csv("Datasets\data.csv")
#     # conn = sqlite3.connect('data.db')
#     # df = pd.read_sql('SELECT * FROM countries', conn)
#     # conn.close()

#     df = SmartDataframe(df, config={"llm": llm})
    
#     question = message.content
#     response = df.chat(question)
#     msg = cl.Message(content=response)
    
#     await msg.send()

#     # Update message history and send final message
#     message_history.append({"role": "assistant", "content": msg.content})
#     await msg.update()



import pandas as pd
import chainlit as cl
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq 
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the ChatGroq model
llm = ChatGroq(model_name="llama3-70b-8192", api_key=os.environ["GROQ_API_KEY"])

# Specify the directory where you want charts to be saved
custom_chart_directory = os.path.abspath("directory")  # Use absolute path

@cl.on_chat_start
def start_chat():
    # Set initial message history
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )

@cl.on_message
async def main(message: cl.Message):
    # Retrieve message history
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    # Load data (example: from CSV file)
    df = pd.read_csv("Datasets/data.csv")  # Change path to your CSV file

    # Initialize SmartDataframe with custom configuration
    df = SmartDataframe(df, config={"llm": llm, "chart_dir": custom_chart_directory})
    
    question = message.content
    response = df.chat(question)
    msg = cl.Message(content=response)
    
    await msg.send()

    # Update message history and send final message
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load Gemini pro model and get response
model = genai.GenerativeModel('gemini-1.5-flash')
chat= model.start_chat(history=[])


def get_conversational_chain(question):
    response=chat.send_message(question,stream=True )
    return response


# initialize stremlit app

st.set_page_config("Chatbot")
st.header("Chat with Gemini")

#initialie session for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
input = st.text_input("Input",key='input')
submit=st.button("Ask the question")

if submit and input:
    response = get_conversational_chain(input)
    #Add user response and session query to chat history        
    st.session_state['chat_history'].append(('You',input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot',chunk.text))
st.subheader("The chat history is ")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
  



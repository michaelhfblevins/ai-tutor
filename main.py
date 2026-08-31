# main.py
import streamlit as st
from anthropic import Anthropic

st.set_page_config(
    page_title="My Personal AI Tutor",
    page_icon="tutor_favicon.png",
    layout="centered"
)

# Get API key
api_key = st.secrets["ANTHROPIC_API_KEY"]

# Title
st.markdown("<h1 style='text-align: center; '>My Personal AI Tutor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #808080;'>Michael Blevins</h4>", unsafe_allow_html=True)

# Interaction Tips
with st.expander("**Tips for Getting Started 🚀**"):
    st.markdown('''
- To get the best results, be as specific as you can.
- Ask follow-up questions if you are still unclear.
- To help type math, use the following keyboard shortcuts:
    - × : `*`
    - ÷ : `/`
    - Powers: `x^2`
    - Square root: `\sqrt{x}`
- Example Prompts to Get Started:
    - "Summarize Lecture 4 on Linear Regression"
    - "Explain the math involved in the k-means clustering algorithm."
    - "Can you recommend some papers to help me get started on my project on PCA?"
    - "Which lecture covers Linear Regression with Input Uncertainties?"
    - "What are some papers that discuss machine learning approaches for calibrating radial velocity measurements?"
    - "How do I code prediction uncertainties in linear regression?"
    ''')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input and response
if prompt := st.chat_input("Message"):
    if api_key:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get Claude response
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-5",
            max_tokens=200,
            messages=st.session_state.messages
        )
        
        # Add assistant message
        answer = next(block.text for block in response.content if block.type == "text")
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        # Display
        with st.chat_message("assistant"):
            st.write(answer)

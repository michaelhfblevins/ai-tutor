import streamlit as st
from anthropic import Anthropic

st.set_page_config(
    page_title="Blevins AI Tutor",
    page_icon="tutor_favicon.png",
    layout="centered"
)
avatar = {"user": "./images/student_avatar.png",
          "assistant": "./images/cropped_tutor_favicon.png"}
# Get API key
api_key = st.secrets["ANTHROPIC_API_KEY"]

# Logo
st.logo("./images/cropped_tutor_favicon.png", size="large")

# Display Tutor Profile Image
tutor_image_url = "./images/tutor_favicon.png"
col1, col2, col3 = st.columns((1,0.4,1.1))
col2.image(tutor_image_url)

# Title
st.markdown("<h1 style='text-align: center; '>Blevins AI Tutor</h1>", unsafe_allow_html=True)

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

        # Use a spinner to indicate LLM processing
        with st.spinner('Thinking...'):
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
        with st.chat_message("assistant", avatar=avatar["assistant"]):
            st.write(answer)

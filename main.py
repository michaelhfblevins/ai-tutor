import streamlit as st
from anthropic import Anthropic
import time
from app_utils.save_to_html import escape_markdown
from app_utils.complete_assistant import complete_assistant

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
    - "What's the distance to a star with 0.1 arcsecond parallax?",
    - "What did we learn about conversation histories in the API?",
    - "Calculate the luminosity of a star with radius 3 solar radii and temperature 7000K"
    ''')

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": """Hello, I'm your personal tutor! I can assist with:

- Physics concepts and theoretical explanations
- Data analysis and coding support
- Working through practice problems

How can I help you today?"""}]

# Function to stream text word by word
def stream_text(text):
    sentence = ""
    for letter in text:
        sentence += letter
        yield sentence

if "stream_init_msg" not in st.session_state:
    st.session_state.stream_init_msg = True

# Display conversation
if len(st.session_state.messages)>0:
    if st.session_state.stream_init_msg:
        msg = st.session_state.messages[0]
        with st.chat_message(msg["role"], avatar=avatar[msg["role"]]):
            intro_msg = rf"{msg["content"]}"
            with st.empty():
                for char in stream_text(intro_msg):
                    st.markdown(char)
                    time.sleep(0.01)
        st.session_state.stream_init_msg = False
    else:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.chat_message(msg["role"], avatar=avatar[msg["role"]]).markdown(escape_markdown(rf"{msg["content"]}"))
            else:
                st.chat_message(msg["role"], avatar=avatar[msg["role"]]).markdown(rf"{msg["content"]}")

# Input and response
if prompt := st.chat_input("Message"):
    if api_key:
        
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user", avatar=avatar["user"]).markdown(escape_markdown(prompt))

        # Use a spinner to indicate LLM processing
        with st.spinner('Thinking...'):
            # Get Claude response
            response = complete_assistant(st.session_state.messages)
        
        # Add assistant message
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Get TextBlocks from response
        text_blocks = [
        getattr(block, "text", None)
        if not isinstance(block, dict)
        else block.get("text")
        for block in getattr(response, "content", [])
        ]
        text_blocks = [item for item in text_blocks if item]

        # Get text from TextBlock
        for block in text_blocks:
            if block.type == "text":
                text = block.text
        
        # Display response
        with st.chat_message("assistant", avatar=avatar["assistant"]):
            with st.empty():
                for char in stream_text(text):
                    st.markdown(rf"{char}")
                    time.sleep(0.01)
        st.rerun()

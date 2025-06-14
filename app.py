import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from translatepy import Translator
import requests

# Load environment and model
load_dotenv()
translator = Translator()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=20,
    temperature=0.1
)
model = ChatHuggingFace(llm=llm)

# Streamlit config
st.set_page_config(page_title="Sahaayak", page_icon="🆘")

# Language selection
st.sidebar.title("🌐 Language")
language_map = {
    "English": "en",
    "Hindi (हिंदी)": "hi",
    "Bengali (বাংলা)": "bn",
    "Tamil (தமிழ்)": "ta",
    "Marathi (मराठी)": "mr",
    "Telugu (తెలుగు)": "te"
}
lang_name = st.sidebar.selectbox("Choose language", list(language_map.keys()))
lang_code = language_map[lang_name]

# Initial bot instruction
initial_instruction = """
You are Sahaayak – a Disaster Assistance Chatbot. Your job is to help people during natural disasters like earthquakes, floods, cyclones, and fires.

You should:
- Provide safety tips.
- Guide users to nearby help (e.g., hospitals, shelters).
- Share verified emergency contact info.
- Keep answers short and clear.
- Stay calm and reassuring.

Do not provide medical or legal advice. Encourage users to contact local authorities in emergencies.
"""

# Translate UI text
def t(text):
    if lang_code == "en":
        return text
    try:
        return translator.translate(text, lang_code).result
    except:
        return text

# Title
st.title("🆘 " + t("Sahaayak - Your Disaster Assistance Chatbot"))

# Initialize chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=initial_instruction)]

# Hardcoded emergency contacts
emergency_contacts = {
    "India": {
        "Fire": "101",
        "Ambulance": "102",
        "Disaster Mgmt": "108",
        "Police": "100"
    }
}

# Alerts from ReliefWeb
def get_disaster_alerts():
    try:
        url = "https://api.reliefweb.int/v1/disasters?appname=chatbot&limit=3&profile=full"
        data = requests.get(url).json()
        return [d["fields"]["name"] for d in data["data"]]
    except:
        return [t("⚠️ Unable to fetch alerts at this time.")]

# Display emergency contacts
with st.expander("📞 " + t("Emergency Contacts")):
    for country, contacts in emergency_contacts.items():
        st.subheader(t(country))
        for service, number in contacts.items():
            st.write(f"{t(service)}: {number}")

# Display live alerts
with st.expander("📢 " + t("Live Disaster Alerts")):
    for alert in get_disaster_alerts():
        st.markdown(f"• {alert}")

# Quick help FAQ buttons
st.markdown(f"### 💬 {t('Quick Help')}")
faq_col1, faq_col2 = st.columns(2)
faq_clicked = None
with faq_col1:
    if st.button(t("🚨 What to do in a flood?")):
        faq_clicked = "I'm in a flood. What should I do?"
    if st.button(t("🔥 What to do during fire?")):
        faq_clicked = "There's a fire. How should I stay safe?"

with faq_col2:
    if st.button(t("🌪️ Earthquake safety tips")):
        faq_clicked = "Earthquake safety tips"
    if st.button(t("🌀 Cyclone precautions")):
        faq_clicked = "Precautions for cyclone situations"

# Chat styling
st.markdown("""
<style>
.chat-bubble {
    padding: 10px 15px;
    margin: 5px;
    border-radius: 20px;
    display: inline-block;
    max-width: 75%;
    word-wrap: break-word;
    font-size: 16px;
}
.user-bubble {
    background-color: #DCF8C6;
    color: black;
    margin-left: auto;
    border-bottom-right-radius: 5px;
}
.bot-bubble {
    background-color: #F1F0F0;
    color: black;
    margin-right: auto;
    border-bottom-left-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# Show existing chat history
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.markdown(f"<div class='chat-bubble user-bubble'>{msg.content}</div>", unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        translated = translator.translate(msg.content, lang_code).result if lang_code != "en" else msg.content
        st.markdown(f"<div class='chat-bubble bot-bubble'>{translated}</div>", unsafe_allow_html=True)

# Chat input
user_input = st.chat_input(t("Type your emergency query..."))

if faq_clicked:
    user_input = faq_clicked

if user_input:
    translated_input = translator.translate(user_input, "en").result if lang_code != "en" else user_input
    st.session_state.chat_history.append(HumanMessage(content=translated_input))
    st.markdown(f"<div class='chat-bubble user-bubble'>{user_input}</div>", unsafe_allow_html=True)

    try:
        response = model.invoke(st.session_state.chat_history)
        bot_msg = response.content.strip()
        translated_response = translator.translate(bot_msg, lang_code).result if lang_code != "en" else bot_msg
    except:
        translated_response = t("⚠️ I'm currently offline. For emergencies, call your nearest help center or dial 108 (India).")

    st.session_state.chat_history.append(AIMessage(content=translated_response))
    st.markdown(f"<div class='chat-bubble bot-bubble'>{translated_response}</div>", unsafe_allow_html=True)

# Reset button
if st.button("🔁 " + t("Reset Chat")):
    st.session_state.chat_history = [SystemMessage(content=initial_instruction)]
    st.rerun()

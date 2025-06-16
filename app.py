import streamlit as st
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from translatepy import Translator
import requests

load_dotenv()
translator = Translator()
model = ChatOllama(model="llama3", temperature=0.3)

st.set_page_config(page_title="Sahaayak - AI Disaster Assistant", page_icon="🆘", layout="centered")

# Sidebar - Language Selection
st.sidebar.markdown("### 🌐 Language")
language_map = {
    "English": "en",
    "Hindi (हिंदी)": "hi",
    "Bengali (বাংলা)": "bn",
    "Tamil (தமிழ்)": "ta",
    "Marathi (मराठी)": "mr",
    "Telugu (తెలుగు)": "te"
}
lang_name = st.sidebar.selectbox("Choose your language", list(language_map.keys()))
lang_code = language_map[lang_name]

def t(text):
    if lang_code == "en":
        return text
    try:
        return translator.translate(text, lang_code).result
    except:
        return text

initial_instruction = """
You are Sahaayak – a calm, helpful Disaster Assistance Bot for India.
Provide short and clear guidance on:
- Natural disaster safety in India (flood, earthquake, fire, cyclone)
- Indian emergency contact numbers (e.g., 112 for all emergencies, 101 for fire, 100 for police, 108 for ambulance)
- Shelters, relief centers, or medical help as per Indian disaster management guidelines
- Mention organizations like NDMA, NDRF, and State Disaster Management Authorities
Do not mention any foreign emergency numbers or organizations.
Never give legal or medical advice. Always guide users to real-life help available in India.
"""


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content=initial_instruction)]

# === Custom CSS Styling ===
st.markdown("""
<style>
body {
    background-color: #121212;
    color: white;
}
[data-testid="stAppViewContainer"] {
    background: #121212;
}
[data-testid="stSidebar"] {
    background-color: #1f1f1f;
}
h1, h2, h3, h4, h5 {
    color: #FFFFFF;
}
button[kind="secondary"] {
    background-color: #222 !important;
    color: #fff !important;
    border: 1px solid #555;
}
.chat-bubble {
    padding: 14px 18px;
    border-radius: 20px;
    margin: 10px 0;
    max-width: 75%;
    font-size: 15px;
    line-height: 1.6;
    word-break: break-word;
}
.user {
    background: #0084FF;
    color: white;
    align-self: flex-end;
    margin-left: auto;
    border-bottom-right-radius: 4px;
}
.bot {
    background: #2c2c2c;
    color: white;
    align-self: flex-start;
    margin-right: auto;
    border-bottom-left-radius: 4px;
}
.stChatInputContainer {
    background: transparent;
    border-radius: 8px;
}
input[type="text"] {
    background-color: #1e1e1e !important;
    color: white !important;
    border: 1px solid #444;
    border-radius: 10px;
    padding: 0.6em;
}
</style>
""", unsafe_allow_html=True)

# === Title ===
st.markdown(f"<h1 style='text-align:center;'>🤖 {t('Sahaayak - Your Disaster Assistant')}</h1>", unsafe_allow_html=True)

# === Emergency Numbers ===
with st.expander("📞 " + t("Emergency Numbers")):
    st.subheader("🇮🇳 India")
    contacts = {
        "National Emergency Number":"112",
        "Fire Department": "101",
        "Ambulance": "102",
        "Disaster Response": "108",
        "Police": "100"
        
    }
    for k, v in contacts.items():
        st.write(f"**{t(k)}**: {v}")

# === Disaster Alerts from ReliefWeb ===
def get_disaster_alerts():
    try:
        data = requests.get("https://api.reliefweb.int/v1/disasters?appname=sahaayak&limit=3").json()
        return [d["fields"]["name"] for d in data["data"]]
    except:
        return [t("⚠️ Cannot fetch alerts right now.")]

with st.expander("📢 " + t("Latest Disaster Alerts")):
    for alert in get_disaster_alerts():
        st.markdown(f"• {alert}")

# === Quick Help ===
st.markdown("### 💬 " + t("Quick Help"))
c1, c2 = st.columns(2)
faq_clicked = None
with c1:
    if st.button(t("🌊 Flood Safety")):
        faq_clicked = "What should I do during a flood?"
    if st.button(t("🔥 Fire Safety")):
        faq_clicked = "Fire emergency safety tips?"

with c2:
    if st.button(t("🌪️ Earthquake Safety")):
        faq_clicked = "How to stay safe during earthquakes?"
    if st.button(t("🌀 Cyclone Tips")):
        faq_clicked = "What precautions to take during a cyclone?"

# === Chat History ===
for msg in st.session_state.chat_history:
    if isinstance(msg, SystemMessage):
        continue  # skip system prompt from showing in UI

    role_class = "user" if isinstance(msg, HumanMessage) else "bot"
    content = msg.content

    # Translate bot messages if needed
    if isinstance(msg, AIMessage) and lang_code != "en":
        content = translator.translate(content, lang_code).result

    st.markdown(f"<div class='chat-bubble {role_class}'>{content}</div>", unsafe_allow_html=True)

# === Input ===
user_input = st.chat_input(t("Type your emergency query here..."))
if faq_clicked:
    user_input = faq_clicked

if user_input:
    translated_input = translator.translate(user_input, "en").result if lang_code != "en" else user_input
    st.session_state.chat_history.append(HumanMessage(content=translated_input))
    st.markdown(f"<div class='chat-bubble user'>{user_input}</div>", unsafe_allow_html=True)

    try:
        response = model.invoke(st.session_state.chat_history)
        reply = response.content.strip()
    except:
        reply = t("⚠️ I'm currently offline. Please contact local emergency services.")
    st.session_state.chat_history.append(AIMessage(content=reply))

    translated = translator.translate(reply, lang_code).result if lang_code != "en" else reply
    st.markdown(f"<div class='chat-bubble bot'>{translated}</div>", unsafe_allow_html=True)

# === Reset Chat ===
if st.button("🔄 " + t("Reset Chat")):
    st.session_state.chat_history = [SystemMessage(content=initial_instruction)]
    st.rerun()

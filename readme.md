````markdown
# 🆘 Sahaayak – AI Disaster Assistant 🇮🇳

**Sahaayak** is an intelligent, multilingual chatbot designed to help people in **India** during disasters such as floods, earthquakes, fires, and cyclones. Built with **Streamlit**, **LangChain**, **LLaMA 3**, and **Translatepy**, it provides instant, localized guidance and emergency support — all in your preferred Indian language.

---

## 🚀 Features

✅ Powered by **LLaMA 3** via Ollama (local)  
🌐 Supports Indian languages: English, Hindi, Bengali, Tamil, Marathi, Telugu  
📍 **Emergency contacts** for fire, ambulance, disaster response, police  
📢 Real-time **disaster alerts** via [ReliefWeb API](https://reliefweb.int/)  
💬 **Quick Help buttons** for common disasters  
🧠 **Session memory** using LangChain history  
🔁 **Reset chat** anytime  
🎨 Dark-mode themed UI with clean bubble chat

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – App framework  
- [LangChain](https://www.langchain.com/) – LLM orchestration  
- [ChatOllama (LLaMA 3)](https://ollama.com/) – Local chat model  
- [Translatepy](https://pypi.org/project/translatepy/) – Multilingual support  
- [ReliefWeb API](https://reliefweb.int/) – Disaster alerts (India)

---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Akash007AD/Disaster-Help-Chatbot.git
cd Disaster-Help-Chatbot
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

Create a `.env` file in the root folder and add:

```env
# Optional if you're using Hugging Face instead of Ollama
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501).

---

## 🗂 File Structure

```bash
.
├── app.py               # Main Streamlit chatbot code
├── .env                 # API keys (gitignored)
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── .gitignore           # Ignore venv and secrets
```

---

## 📱 Emergency Numbers (India)

| Service            | Number |
| ------------------ | ------ |
| National Emergency | 112    |
| Fire Department    | 101    |
| Ambulance          | 102    |
| Disaster Response  | 108    |
| Police             | 100    |

---

## 🙌 Acknowledgments

* [NDMA](https://ndma.gov.in/) and [NDRF](https://ndrf.gov.in/) for national guidelines
* [ReliefWeb](https://reliefweb.int/) for real-time disaster updates
* [Translatepy](https://github.com/Animenon/translatepy) for smooth language translation
* [Streamlit](https://streamlit.io/) for intuitive UI design
* [LangChain](https://www.langchain.com/) for chat memory and logic

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

# 🆘 Disaster Assistance ChatBot

A multilingual AI chatbot to assist people during natural disasters such as floods, earthquakes, fires, and cyclones. Built with Streamlit and powered by Hugging Face models, the bot provides safety tips, emergency contacts, live alerts, and more — all in multiple Indian languages.

---

## 🚀 Features

* ✅ Real-time AI chat powered by LLaMA-3.1 (via Hugging Face)
* 🌐 Supports multiple Indian languages: English, Hindi, Bengali, Tamil, Marathi, Telugu
* 📍 Detects user location (based on IP)
* 📢 Shows live disaster alerts from ReliefWeb API
* 📞 Displays emergency contact numbers (India-specific)
* 🧠 Quick help buttons for FAQs (e.g., flood, fire, earthquake)
* 🔁 Reset chat functionality
* 🌈 Intuitive and responsive UI

---

## 🛠️ Technologies Used

* [Streamlit](https://streamlit.io/)
* [Langchain](https://www.langchain.com/)
* [Hugging Face Transformers](https://huggingface.co/)
* [Translatepy](https://github.com/Animenon/translatepy)
* [ReliefWeb API](https://api.reliefweb.int/)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/disaster-assistance-chatbot.git
cd disaster-assistance-chatbot
```

### 2. Create and activate virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up `.env` file

Create a `.env` file in the root directory:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

⚠️ **Do NOT commit this file to GitHub.**

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open the local URL (e.g., `http://localhost:8501`) in your browser.

---

## 🌐 Deploy on Streamlit Cloud

1. Push your project to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app.
3. Set up **Secrets** in the app settings with:

```toml
HUGGINGFACEHUB_API_TOKEN = "your_huggingface_api_token"
```

---

## 📁 File Structure

```bash
.
├── app.py               # Main Streamlit app
├── .env                 # API keys (excluded from GitHub)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignore .env and virtual env
```

---

## 🙏 Acknowledgements

* Hugging Face LLaMA models
* Translatepy for multilingual support
* ReliefWeb for real-time disaster feeds
* Streamlit for the amazing frontend framework

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

# AI-Chatbot
# 🤖 AI Chatbot Decision Support Framework

> An intelligent chatbot system that assists users in making informed decisions by processing natural language queries and returning structured, actionable responses.

---

## 📌 About the Project

The **AI Chatbot Decision Support Framework** application is designed to help users ask questions related to NGO services, volunteering, and donations. It uses Google Gemini AI to understand natural language input and generate helpful, conversational responses in real time.

The project is built with Python and integrates the Gemini API through the google.generativeai library. It loads the API key securely from a .env file and provides a simple chat interface where users can interact with the assistant directly.

This application is useful for NGOs that want a lightweight AI-powered support tool to guide users, answer common queries, and improve communication around services, donation support, and volunteer opportunities. It also provides a simple foundation that can be extended later with stronger error handling, structured decision flows, or support for additional AI/NLP services.

---

## ✨ Features

- 🧠Natural Language Query Handling - processes user messages using Gemini AI
- 🔌AI-Powered NGO Assistance - helps with volunteering, services, and donations
- ⚡Real-Time Chat Interface - displays user and AI messages instantly through Streamlit
- 🔄 Session-Based Conversation Memory - keeps chat history during the current session
- 🛡️ Environment-Based API Configuration - loads the Gemini API key from .env

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, streamlit|
| AI / NLP |  Google Gemini API, google.generativeai |
| Communication | HTTP via Streamlit, API communication handled by Gemini SDK |
| Tools |  VS Code, Git |

---

## 🚀 Getting Started

Install these dependencies:
```
pip install streamlit google-generativeai python-dotenv
[Make sure your .env file has:
GOOGLE_API_KEY=your_api_key_here]

Run the app with:
python -m streamlit run app.py

Then open:
http://localhost:8501
---
```
## 📁 Project Structure

```
final/
├── app.py
├── .env
└── README.md
```

---

## 📸 Screenshots

<img width="1904" height="918" alt="Screenshot 2026-05-01 192928" src="https://github.com/user-attachments/assets/badc8925-d2a5-4516-b3bb-79747d95ed02" />


---

## 🔮 Future Enhancements

- [ ] Add conversation history and session management
- [ ] Deploy on Render
- [ ] Add support for multi-language queries

---

## 👩‍💻 Author

Dharmashree S
- 📧 dharmashree.s04@gmail.com
- 🌐 [GitHub](https://github.com/DharmaShree04)
- 💼 [LinkedIn](www.linkedin.com/in/dharmashree-s-)

---


⭐ If you found this project useful, please consider giving it a star!


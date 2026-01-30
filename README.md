# Career-Path-Analyzer
Career Bot Chatbot is an AI-powered career guidance system built using Python and Streamlit that analyzes resumes and user interests to recommend suitable career paths. Uploaded resumes are securely stored in the cloud using AWS S3 for scalability and future analysis.
# 🎯 Career Bot Chatbot – Cloud Deployed AI Career Guidance System

Career Bot Chatbot is an AI-powered career guidance application built using **Python and Streamlit**, designed to help users identify suitable career paths based on their **resume analysis or career interests**.  
The application is **deployed on AWS EC2** and securely stores uploaded resumes in **AWS S3**, demonstrating real-world cloud implementation.

---

## 🚀 Key Features

- 📄 Upload PDF resumes for career analysis  
- 💡 Interest-based career recommendations  
- 🧠 NLP-based skill and domain prediction  
- 🗺️ Step-by-step career roadmaps  
- ☁️ Cloud deployment using AWS EC2  
- 🗃️ Secure resume storage using AWS S3  
- 🎨 Interactive and user-friendly Streamlit UI  

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|------------|
| Frontend | Streamlit |
| Backend | Python |
| NLP | spaCy |
| PDF Parsing | pdfminer.six |
| Cloud Compute | AWS EC2 |
| Cloud Storage | AWS S3 |

---

## 📂 Project Structure

career-bot-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resume.pdf (optional)

---

## ⚙️ How It Works

1. User uploads a **PDF resume** or enters an **area of interest**
2. Resume is securely stored in **AWS S3**
3. NLP techniques extract keywords and skills
4. The system predicts the most suitable career domain
5. A structured career roadmap is displayed to the user

---

## 📦 Local Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/career-bot-chatbot.git
cd career-bot-chatbot


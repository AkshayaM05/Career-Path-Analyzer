
# 🎯 Career Path Analyzer – Cloud Deployed AI Career Guidance System

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



clone the Repository:
git clone https://github.com/AkshayaM05/Carrer-Path-Analyzer.git
cd career-bot-chatbot
setup:
  steps:
    - step: "Create Virtual Environment"
      command:
        - python -m venv venv
        - venv\\Scripts\\activate   # Windows

    - step: "Install Dependencies"
      command:
        - pip install -r requirements.txt

    - step: "Download spaCy Model"
      command:
        - python -m spacy download en_core_web_sm

    - step: "Run Application"
      command:
        - streamlit run app.py

☁️ AWS Deployment
🔹 AWS EC2 (Application Hosting)

Instance: Ubuntu 22.04 (t2.micro – free tier)

Streamlit app runs on EC2

Application accessible via public IP
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Access:  http://EC2_PUBLIC_IP:8501

AWS S3 (Resume Storage)

All uploaded resumes are stored securely in AWS S3

Ensures data persistence and scalability

Enables future analytics and reprocessing
User Browser
     ↓
Streamlit UI (AWS EC2)
     ↓
Resume Upload
     ↓
AWS S3 (Storage)
     ↓
NLP Processing (Python)
     ↓
Career Domain Prediction & Roadmap

aws_s3_upload.py → Handles secure resume upload to AWS S3


🔐 Security & Scalability

Secure cloud storage using AWS S3

Scalable deployment via AWS EC2

Accessible from any device with internet

📌 Future Enhancements

GPT-based conversational chatbot

User authentication system

Skill gap analysis

Job recommendation APIs

Admin dashboard



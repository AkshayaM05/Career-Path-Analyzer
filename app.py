import streamlit as st
from pdfminer.high_level import extract_text
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Keywords for domain classification
domain_keywords = {
    "Web Development": ["html", "css", "javascript", "react", "node", "php", "frontend", "backend"],
    "Data Science": ["python", "pandas", "numpy", "statistics", "ml", "data", "regression", "clustering"],
    "Cybersecurity": ["network", "linux", "hacking", "firewall", "nmap", "wireshark", "security", "kali"],
    "AI/ML": ["deep learning", "machine learning", "neural networks", "tensorflow", "pytorch", "opencv"],
    "App Development": ["android", "flutter", "kotlin", "java", "ios", "swift", "mobile"],
    "UI/UX Design": ["figma", "wireframe", "prototyping", "user flow", "adobe xd", "ux research", "interface"],
    "Cloud Computing": ["aws", "azure", "gcp", "cloud", "ec2", "s3", "lambda", "cloudformation"],
    "DevOps": ["docker", "kubernetes", "ci/cd", "jenkins", "ansible", "terraform", "monitoring"],
    "Game Development": ["unity", "unreal", "blender", "game physics", "game engine", "c#", "2d", "3d"],
    "Blockchain Development": ["blockchain", "smart contract", "ethereum", "solidity", "web3", "nft"]
}

# Career paths per domain
career_roadmaps = {
    "Web Development": [
        "1. Learn HTML, CSS, JavaScript",
        "2. Learn frontend (React, Angular)",
        "3. Learn backend (Node.js, PHP, Django)",
        "4. Build 3-5 projects",
        "5. Contribute to open source or freelance"
    ],
    "Data Science": [
        "1. Learn Python, Pandas, Numpy, Matplotlib",
        "2. Study statistics, ML algorithms",
        "3. Do Kaggle competitions or real datasets",
        "4. Build 3 projects (EDA, ML, Dashboard)",
        "5. Get certifications from IBM/Google"
    ],
    "Cybersecurity": [
        "1. Learn Networking, Linux, OS Concepts",
        "2. Learn Hacking tools (Wireshark, Nmap)",
        "3. Setup a virtual lab (Kali, Metasploit)",
        "4. Join CTFs and hackathons",
        "5. Get CEH or OSCP certified"
    ],
    "AI/ML": [
        "1. Learn Python, Sklearn, Pandas",
        "2. Study ML, DL (TensorFlow, PyTorch)",
        "3. Build 3+ projects (Image, Text, Time Series)",
        "4. Study math behind ML (Linear Algebra, Calc)",
        "5. Do internships or publish models"
    ],
    "App Development": [
        "1. Learn Java/Kotlin or Flutter",
        "2. Understand Android/iOS lifecycle",
        "3. Build and publish 3 apps",
        "4. Integrate with Firebase, APIs",
        "5. Do internships or freelance"
    ],
    "UI/UX Design": [
        "1. Learn Figma, Adobe XD, design thinking",
        "2. Master wireframing, prototyping",
        "3. Study color, typography, layout",
        "4. Build 3+ real projects (apps, websites)",
        "5. Upload on Behance, Dribbble"
    ],
    "Cloud Computing": [
        "1. Learn basics of cloud (AWS/GCP)",
        "2. Study compute, storage, networking",
        "3. Practice with AWS EC2, S3, Lambda",
        "4. Do hands-on labs and mini-projects",
        "5. Get AWS/GCP certified"
    ],
    "DevOps": [
        "1. Learn Linux, Git, Docker",
        "2. Study CI/CD pipelines (Jenkins)",
        "3. Master Kubernetes, Terraform",
        "4. Build a DevOps project pipeline",
        "5. Get certified (CKA, AWS DevOps)"
    ],
    "Game Development": [
        "1. Learn Unity or Unreal Engine",
        "2. Study 2D/3D game mechanics",
        "3. Create 2-3 small games",
        "4. Publish on Play Store or Steam",
        "5. Join game jams or indie dev forums"
    ],
    "Blockchain Development": [
        "1. Learn blockchain basics",
        "2. Learn Solidity and smart contracts",
        "3. Build dApps using Web3",
        "4. Explore NFTs and DeFi projects",
        "5. Join blockchain hackathons"
    ]
}

# Text extraction
def extract_text_from_pdf(pdf_file):
    return extract_text(pdf_file).lower()

# Domain prediction
def predict_domain(text):
    scores = {}
    doc = text.lower()

    for domain, keywords in domain_keywords.items():
        match_count = sum(1 for kw in keywords if kw in doc)
        total_keywords = len(keywords)
        score_percent = round((match_count / total_keywords) * 100, 2)
        scores[domain] = score_percent

    best_domain = max(scores, key=scores.get)
    return best_domain, scores[best_domain]



# 🌐 UI
st.set_page_config(page_title="Career Path Analyzer", layout="centered")
st.title("\U0001F3AF Career Path Analyzer - Resume or Interest Based")

# Option to choose input method
option = st.radio("Select how you'd like to proceed:", ["\U0001F4C4 Upload Resume", "\U0001F4A1 Enter Area of Interest"])

# --- Resume Path ---
if option == "\U0001F4C4 Upload Resume":
    uploaded_file = st.file_uploader("Upload your PDF resume:", type="pdf")

    if uploaded_file and st.button("\U0001F50D Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            domain, score = predict_domain(resume_text)

        st.success(f"\U0001F31F You shine best in: **{domain}** (Score: {score} matches)")
        st.subheader(f"\U0001F4C8 Recommended Career Path for {domain}:")
        for step in career_roadmaps[domain]:
            st.markdown(f"- {step}")

# --- Interest Path ---
elif option == "\U0001F4A1 Enter Area of Interest":
    user_interest = st.text_input("Enter your area of interest (e.g., AI/ML, Web Development, Cybersecurity):")

    if user_interest and st.button("\U0001F680 Get Career Path"):
        cleaned_input = user_interest.lower().replace(" ", "")
        matched = None

        for domain in domain_keywords:
            if cleaned_input in domain.lower().replace(" ", ""):
                matched = domain
                break

        if matched:
            st.success(f"\u2728 Career Path for: **{matched}**")
            for step in career_roadmaps[matched]:
                st.markdown(f"- {step}")
        else:
            st.warning("\u274C Sorry, we couldn't recognize that domain. Try keywords like: Web, Data, Cloud, DevOps, AI, etc.")

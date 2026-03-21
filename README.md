# 🧠 AI Resume Screening System

An AI-powered resume screening system that automatically scores and ranks candidates based on a job description.

## 🎥 Demo Video
Watch Demo - https://www.loom.com/share/f3a754e6fac1481db3998a2a9cb53685

## ⚙️ Tech Stack
- **Frontend:** Streamlit
- **AI Model:** Llama 3.3 70B (via Groq API)
- **PDF Reading:** PyMuPDF
- **Word Reading:** python-docx
- **Language:** Python

## 📋 Features
- Upload multiple resumes (PDF or Word)
- Paste any Job Description
- Get instant AI scoring (0-100)
- Filter candidates by verdict
- Color coded bar chart for visual ranking
- Download results as CSV

## 🛠️ Setup Instructions

1. Clone the repo
```bash
git clone git@github.com:choudhary09srishti-boop/AI_Resume_Screener.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your API key in `.env` file
```
GROQ_API_KEY=your_key_here
```

4. Run the app
```bash
cd src
streamlit run app.py
```

## 📁 Project Structure
```
AI_Resume_Screener/
├── src/
│   ├── app.py
│   ├── gemini_helper.py
│   └── pdf_reader.py
├── data/resumes/      ← upload resumes here
├── output/            ← results saved here
├── requirements.txt
└── .env               ← add your API key here
```

## 🛠️ Tools Used
- Streamlit
- Groq API (Llama 3.3 70B)
- PyMuPDF
- python-docx
- Plotly
- Pandas
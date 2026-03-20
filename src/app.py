import streamlit as st
import pandas as pd
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(__file__))

from pdf_reader import extract_text
from gemini_helper import screen_resume

st.set_page_config(page_title="AI Resume Screener", page_icon="🧠", layout="wide")
st.title("🧠 AI Resume Screening System")
st.caption("Powered by Gemini 1.5 Flash — 100% Free")

# --- Inputs ---
st.subheader("Step 1 — Paste the Job Description")
jd_text = st.text_area("Job Description", height=200, placeholder="Paste the full job description here...")

st.subheader("Step 2 — Upload Resumes (PDF or Word)")
uploaded_files = st.file_uploader("Upload resumes", type=["pdf", "docx"], accept_multiple_files=True)

# --- Run Screening ---
if st.button("🚀 Screen Resumes", use_container_width=True):
    if not jd_text:
        st.warning("Please paste a Job Description first!")
    elif not uploaded_files:
        st.warning("Please upload at least one resume!")
    else:
        results = []
        progress = st.progress(0, text="Screening resumes...")

        for i, file in enumerate(uploaded_files):
            candidate_name = file.name.replace(".pdf", "").replace(".docx", "").replace("_", " ").title()
            with st.spinner(f"Analyzing {candidate_name}..."):
                resume_text = extract_text(file)
                result = screen_resume(jd_text, resume_text, candidate_name)
                results.append(result)
            progress.progress((i + 1) / len(uploaded_files), text=f"Done {i+1}/{len(uploaded_files)}")

        progress.empty()
        st.success(f"✅ Screened {len(results)} candidates!")

        # --- Results Table ---
        st.subheader("📊 Results")
        df = pd.DataFrame([{
            "Candidate": r["name"],
            "Score": r["score"],
            "Verdict": r["verdict"],
            "Strengths": " | ".join(r["strengths"]),
            "Gaps": " | ".join(r["gaps"]),
            "Summary": r["summary"]
        } for r in results])

        df = df.sort_values("Score", ascending=False).reset_index(drop=True)

        def color_verdict(val):
            if val == "Strong Fit":
                return "background-color: #d4edda; color: #155724"
            elif val == "Moderate Fit":
                return "background-color: #fff3cd; color: #856404"
            else:
                return "background-color: #f8d7da; color: #721c24"

        st.dataframe(df.style.map(color_verdict, subset=["Verdict"]), use_container_width=True)

        # --- Export ---
        csv = df.to_csv(index=False)
        st.download_button("⬇️ Download Results as CSV", csv, "results.csv", "text/csv", use_container_width=True)
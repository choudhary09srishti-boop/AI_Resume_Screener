import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def screen_resume(jd_text, resume_text, candidate_name):
    prompt = f"""
You are an expert HR recruiter. Compare the resume against the job description.

JOB DESCRIPTION:
{jd_text}

CANDIDATE NAME: {candidate_name}

RESUME:
{resume_text}

Return ONLY a JSON object like this (no extra text, no markdown):
{{
  "name": "{candidate_name}",
  "score": <number between 0 and 100>,
  "strengths": ["strength 1", "strength 2", "strength 3"],
  "gaps": ["gap 1", "gap 2", "gap 3"],
  "verdict": "<Strong Fit / Moderate Fit / Not Fit>",
  "summary": "<one line reason for verdict>"
}}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    raw = response.choices[0].message.content.strip()

    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    return json.loads(raw)
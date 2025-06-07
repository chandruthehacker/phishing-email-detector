# AI-Powered Phishing Email Detector

![Phishing Email Detector Banner](https://github.com/chandruthehacker/phising-email-detector/blob/main/frontend/thumbnail.png)  
*Protect yourself from phishing attacks using cutting-edge AI technology.*

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Technology Stack](#technology-stack)  
- [Installation](#installation)  
- [Usage](#usage) 

---

## Project Overview

Phishing emails are one of the most common cybersecurity threats, targeting individuals and organizations alike. This project provides a smart AI-powered phishing email detector that analyzes email content using Google’s Generative AI (Gemini API) to determine whether an email is safe or malicious.

The detector offers an easy-to-use web interface built with Flask and JavaScript, allowing users to paste email text and get instant feedback on its phishing likelihood.

---

## Features

- **AI-based phishing detection**: Uses Google Generative AI to analyze email content.  
- **User-friendly web interface**: Paste email content and get real-time results.  
- **Cross-Origin Resource Sharing (CORS)** enabled backend for seamless frontend-backend communication.  
- **Environment variable management** via `.env` for secure API key storage.  
- **Lightweight & easy to deploy** on any system with Python installed.  

---

## Technology Stack

| Technology           | Purpose                         |
| -------------------- | -------------------------------|
| Python               | Backend language               |
| Flask                | Web framework                  |
| Flask-CORS           | Handling CORS                  |
| Google Generative AI API | AI-powered phishing detection |
| JavaScript, HTML, CSS| Frontend UI                   |
| python-dotenv        | Environment variable loading   |

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/phishing-email-detector.git
   cd phishing-email-detector
   ```

2. **Create and activate a virtual environment:**

   Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   macOS / Linux:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install required packages:**
   ```
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```
   python app.py
   ```
5. **Enter your Google Generative AI API key when prompted:**
   - If you don’t have an API key yet, get it here:
   - https://aistudio.google.com/app/apikey
   - Paste your API key into the terminal and press Enter. This will save the key securely for the app.

---

## Usage
1. **After running the command The application will automatically open in your default web browser.**

2. **In the webpage:**
   - Enter or paste the email content you want to analyze.
   - Click the Analyze email button.
3. **The result will display whether the email is Phishing or Safe based on AI analysis.**


---

> “Cybersecurity is much more than an IT topic—it's a critical part of protecting our digital future.”
> “The future belongs to those who prepare for it today—with tools powered by AI and driven by purpose.”

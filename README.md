# 🚨 AI-Powered Phishing Email Detector

![Phishing Email Detector Banner](https://chandruthehacker.github.io/portfolio-website-old/projects/all-projects/phising-email-detector/assets/images/phishing-detector.webp)  
*Protect yourself from phishing attacks using cutting-edge AI technology.*

---

## 📚 Table of Contents

- [🧠 Project Overview](#-project-overview)  
- [✨ Features](#-features)  
- [🛠️ Technology Stack](#-technology-stack)  
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [🔐 Final Thoughts](#-final-thoughts)

---

## 🧠 Project Overview

Phishing emails are one of the most dangerous and common cyber threats targeting individuals and organizations. This AI-powered tool uses **Google’s Generative AI (Gemini API)** to intelligently analyze email content and detect if it’s **phishing or safe**.

With a user-friendly interface and real-time detection, this project empowers users to take proactive action against phishing attacks.

---

## ✨ Features

✅ AI-based phishing classification using Google Gemini  
✅ Fast and intuitive web UI (HTML, CSS, JavaScript)  
✅ Flask backend with CORS support  
✅ Secure API key handling with `.env`  
✅ Auto-launches in your browser after running  
✅ Lightweight, easy to set up, and free to use

---

## 🛠️ Technology Stack

| Technology                | Purpose                              |
|---------------------------|--------------------------------------|
| Python                    | Backend logic                        |
| Flask                     | Web server framework                 |
| Flask-CORS                | Enable CORS requests                 |
| Google Generative AI API  | AI-based email classification        |
| JavaScript, HTML, CSS     | Frontend interface                   |
| python-dotenv             | Load API key securely from `.env`    |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/chandruthehacker/phising-email-detector.git
cd phising-email-detector
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

## 🚀 Usage
1. **Once you run the app, your default browser will automatically open.**

2. **On the webpage:**
   - Paste the email content you want to scan.
   - Click the Analyze Email button.
3. **The AI will instantly evaluate the text and return a result:**
   - 🟥 Phishing
   - ✅ Safe


---

## 🔐 Final Thoughts

>💡 “Cybersecurity is much more than an IT topic—it's a critical part of protecting our digital future.”
---
>🤖 “The future belongs to those who prepare for it today—with tools powered by AI and driven by purpose.”
---
>🧠 “Think before you click. Detect before you risk.”

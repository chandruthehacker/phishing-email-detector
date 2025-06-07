import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS 
import webbrowser
import threading
import time

app = Flask(__name__)
CORS(app)
ENV_FILE = ".env"

def is_api_key_valid(api_key: str) -> bool:
    if not api_key:
        print("❌ API key is empty.")
        return False
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        model.generate_content("Test API key validity.")
        return True
    except Exception as e:
        print(f"❌ Invalid API Key or Error during API key validation: {e}")
        return False

def check_and_set_api_key_interactive():
    load_dotenv(override=True)
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not is_api_key_valid(api_key):
        print("\n--- Google API Key Setup ---")
        print("Google API key not found in .env or is invalid.")
        user_api_key = input("👉 Please enter your Google API key: ").strip()

        if not user_api_key:
            print("❌ API key cannot be empty. Exiting.")
            exit(1) # Exit if no API key is provided
        else:
            if is_api_key_valid(user_api_key):
                print("✅ API key is valid.")
            else:
                print("❌ API key is invalid. Please try again with a correct key.")
                exit(1)

        if not os.path.exists(ENV_FILE):
            with open(ENV_FILE, "w") as f:
                f.write(f"GOOGLE_API_KEY={user_api_key}\n")
        else:
            updated = False
            lines = []
            with open(ENV_FILE, "r") as f:
                lines = f.readlines()
            with open(ENV_FILE, "w") as f:
                for line in lines:
                    if line.strip().startswith("GOOGLE_API_KEY="):
                        f.write(f"GOOGLE_API_KEY={user_api_key}\n")
                        updated = True
                    else:
                        f.write(line)
                if not updated:
                    f.write(f"GOOGLE_API_KEY={user_api_key}\n")

        print(f"✅ API key saved to {ENV_FILE}.")
        os.environ["GOOGLE_API_KEY"] = user_api_key
    else:
        print("✅ Google API Key found and is valid.")

def analyze_email_for_phishing_core(email_content: str) -> str:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return "Error: Google API Key not found. Please set it as an environment variable or in your .env file."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""
    Analyze the following email content to determine its legitimacy, looking for *both* phishing indicators and strong signs of a genuine, non-suspicious message.

    **Phishing Indicators to look for:**
    * Suspicious or deceptive links (e.g., mismatched domain, misspelled domain, redirectors).
    * Overly urgent or threatening language (e.g., "account suspended immediately", "act now or lose access").
    * Requests for sensitive personal information directly in the email (passwords, credit card numbers, SSN).
    * Generic greetings when specific personalization is expected (e.g., "Dear Customer" from a known service that usually uses your name).
    * Obvious misspellings or poor grammar, especially in official-looking communications.
    * Sender discrepancies (e.g., display name not matching email address domain, unexpected sender).
    * Unexpected or unusual attachments.

    **Signs of Legitimacy to prioritize and look for:**
    * Clearly identifiable and correct sender domain (e.g., `@google.com`, `@microsoft.com`).
    * Personalized greeting (when applicable and expected).
    * Content that is expected and relevant to the recipient's known relationship with the sender (e.g., a bill from a service you use).
    * Official and clear links, especially those explicitly encouraging manual navigation or copy-pasting for security (e.g., "log in directly to our website" or "copy/paste this link into your browser"). This specific instruction is a *strong positive indicator* of a security-conscious sender.
    * Professional, clear, and concise tone throughout the email.
    * Provision of alternative, verifiable contact methods (e.g., official support page, phone number listed on their official website).
    * Standard automated notification disclaimers ("Do not reply to this email").

    Provide a clear verdict (choose one from: "Verdict: Legitimate", "Verdict: Suspicious - Proceed with Caution", "Verdict: Likely Phishing") and explain your reasoning concisely, using bullet points for key indicators. Focus on providing *actionable advice* if suspicious.

    Email Content:
    ---
    {email_content}
    ---
    """

    try:
        response = model.generate_content(prompt)
        if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
            return response.candidates[0].content.parts[0].text
        else:
            return "Error: Could not get a valid analysis from the AI. No candidates found or content missing."

    except Exception as e:
        return f"An error occurred during AI analysis: {e}"

@app.route('/analyze-email', methods=['POST'])
def analyze_email_endpoint():
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    email_content = data.get('email_content', '')

    if not email_content:
        return jsonify({"message": "No email content provided"}), 400

    print(f"Received email content for analysis (first 100 chars): {email_content[:100]}...")
    analysis_result = analyze_email_for_phishing_core(email_content)
    print("Analysis complete.")
    return jsonify({"result": analysis_result})

def open_frontend_browser():
    time.sleep(1) 
    html_file_path = os.path.join(os.getcwd(), 'frontend', 'index.html')
    import urllib.parse
    file_url = urllib.parse.urljoin('file:', urllib.request.pathname2url(html_file_path))
    webbrowser.open_new_tab(file_url)
    print(f"🌐 Opening frontend in browser at: {file_url}")


if __name__ == "__main__":
    check_and_set_api_key_interactive()

    print("\nStarting Flask server for email analysis...")
    threading.Thread(target=open_frontend_browser).start()
    app.run(debug=True, port=5000, use_reloader=False)

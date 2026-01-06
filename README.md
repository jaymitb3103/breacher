# 🛡️ BreachRadar Pro

### Advanced Password Hygiene & Breach Detection Tool

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([YOUR_STREAMLIT_APP_LINK_HERE])
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Security](https://img.shields.io/badge/Security-k--Anonymity-green)

**BreachRadar Pro** is a privacy-first cybersecurity tool designed to audit password strength and check for exposure in known data breaches without ever compromising user data.



## 🚀 Live Demo
**[Click here to try the App]([[YOUR_STREAMLIT_APP_LINK_HERE](https://breacher.streamlit.app/)])**

## 🔑 Key Features

* **🕵️ Real-Time Breach Detection:** Queries the **HaveIBeenPwned API** to check if a password has been exposed in known database leaks.
* **🧠 Smart Strength Analysis:** Uses the **zxcvbn** algorithm (by Dropbox) to detect pattern-based weaknesses (names, dates, keyboard walks) and estimates "Time-to-Crack."
* **🎲 Military-Grade Generator:** Generates high-entropy passwords using Python's `secrets` module, ensuring cryptographic randomness.
* **🔒 Privacy-Preserving Architecture:** Implements the **k-Anonymity** model. Your full password **never** leaves your browser/device.

## 🛠️ How it Works (The Security Part)

Trust is critical in security tools. Here is how BreachRadar protects your data:

1.  **Hashing:** When you enter a password, the app converts it into a **SHA-1 hash** locally.
2.  **k-Anonymity:** We only send the **first 5 characters** of that hash to the API.
3.  **Local Matching:** The API returns a list of hundreds of potential matches (hashes starting with those 5 characters).
4.  **Verification:** The app compares the full hash locally. **The API never sees your actual password.**

## 💻 Tech Stack

* **Frontend:** Streamlit (Python)
* **Logic:** Python 3.9
* **Cryptography:** `hashlib`, `secrets`
* **Algorithms:** `zxcvbn` (Password strength estimation)
* **API:** HaveIBeenPwned (HIBP)

## ⚙️ Installation (Run Locally)

1.  Clone the repo:
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/breach-radar.git
    cd breach-radar
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the app:
    ```bash
    streamlit run app.py
    ```

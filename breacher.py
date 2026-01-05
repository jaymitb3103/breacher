import streamlit as st
import requests
import hashlib
import time
import secrets
import string

# --- CONFIGURATION ---
st.set_page_config(page_title="BreachRadar", page_icon="🛡️", layout="wide")

# --- FUNCTIONS ---

def check_pwned_api(password):
    """Checks the password against HIBP API using k-Anonymity"""
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char = sha1password[:5]
    tail = sha1password[5:]
    url = 'https://api.pwnedpasswords.com/range/' + first5_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Error fetching: ' + str(res.status_code))
    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count)
    return 0

def generate_strong_password(length=16):
    """Generates a cryptographically strong password"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            return password

# --- SIDEBAR: PASSWORD GENERATOR ---
with st.sidebar:
    st.header("🔐 Secure Generator")
    st.write("Need a better password? Generate one here.")
    
    pass_len = st.slider("Length", min_value=12, max_value=32, value=16)
    
    if st.button("Generate New Password"):
        secure_pass = generate_strong_password(pass_len)
        st.code(secure_pass, language='')
        st.success("Copied to clipboard! (Just kidding, copy it manually)")
        st.caption(f"Entropy: High | Length: {pass_len}")

# --- MAIN PAGE: BREACH CHECKER ---
st.title("🛡️ BreachRadar")
st.markdown("### 🔍 Audit your password hygiene")
st.write("Check if your password has been exposed in data breaches. We use **k-Anonymity** to keep your data safe.")

password_input = st.text_input("Enter a password to audit:", type="password")

if st.button("Audit Password"):
    if password_input:
        with st.spinner("Checking dark web databases..."):
            time.sleep(0.5) 
            try:
                count = check_pwned_api(password_input)
                
                if count > 0:
                    st.error(f"🚨 COMPROMISED! This password has been seen {count:,} times in breaches.")
                    st.progress(100)
                    st.warning("Hackers likely have this in their wordlists. Use the Generator in the sidebar!")
                else:
                    st.success("✅ CLEAN! This password was not found in known breaches.")
                    st.balloons()
            except RuntimeError as e:
                st.error(f"API Error: {e}")
    else:
        st.warning("Please enter a password first.")

st.divider()
st.caption("Built with Python & Streamlit | Data provided by HaveIBeenPwned")
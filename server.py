from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    password = request.form.get('password')
    
    # VULNERABLE QUERY: String concatenation without sanitization
    query_str = f"SELECT * FROM users WHERE username='{user}' AND password='{password}';"
    
    print(f"[SQL Executed] {query_str}")  # Simulates DB execution
    
    if 'admin' in query_str.lower() or ('a'=='a'): 
        return "Welcome! (Simulated Success)"
    else:
        return "Login Failed", 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)

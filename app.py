import subprocess
import pickle
import os

# Dangerous: shell injection
def run_command(user_input):
    subprocess.run(user_input, shell=True)

# Dangerous: pickle deserialization
def load_data(data):
    return pickle.loads(data)

# Dangerous: hardcoded secret
API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "admin123"

# Dangerous: SQL injection
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

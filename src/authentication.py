import hashlib

users_db = {}  # Simulated user database

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password, role):
    if username in users_db:
        return "User already exists"
    users_db[username] = {'password': hash_password(password), 'role': role}
    return "Signup successful"

def login(username, password):
    user = users_db.get(username)
    if user and user['password'] == hash_password(password):
        return f"Login successful as {user['role']}"
    return "Invalid credentials"

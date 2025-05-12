import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password_to_check: str, stored_logins: dict) -> bool:
    if email not in stored_logins:
        return False

    hashed_password = hash_password(password_to_check)

    return stored_logins[email] == hashed_password

stored_logins = {
    'user1@example.com': hash_password('securepassword123'),
    'user2@example.com': hash_password('mystrongpassword'),
}

def main():
    print(login('user1@example.com', 'securepassword123', stored_logins))
    print(login('user1@example.com', 'wrongpassword', stored_logins))
    print(login('unknown@example.com', 'anypassword', stored_logins))

if __name__ == '__main__':
    main()

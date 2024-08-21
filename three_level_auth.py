import time

# Logging function to track authentication attempts
def log_attempt(logfile, message):
    with open(logfile, "a") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

# Simple class to manage sessions
class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        self.sessions[user_id] = time.time()
        log_attempt("authentication.log", f"Session created for User {user_id}")
        print(f"Session created for User {user_id}")

    def terminate_session(self, user_id):
        if user_id in self.sessions:
            log_attempt("authentication.log", f"Session terminated for User {user_id}")
            print(f"Session terminated for User {user_id}")
            del self.sessions[user_id]
        else:
            print(f"No active session found for User {user_id}")

# Rate limiting mechanism
class RateLimiter:
    def __init__(self, max_attempts, window_seconds):
        self.max_attempts = max_attempts
        self.window_seconds = window_seconds
        self.attempts = {}

    def is_allowed(self, user_id):
        now = time.time()
        if user_id in self.attempts:
            self.attempts[user_id] = [timestamp for timestamp in self.attempts[user_id] if now - timestamp < self.window_seconds]
            if len(self.attempts[user_id]) >= self.max_attempts:
                log_attempt("authentication.log", f"Rate limit exceeded for User {user_id}")
                return False
        else:
            self.attempts[user_id] = []

        self.attempts[user_id].append(now)
        return True

# Function to simulate hashing (unique but simple)
def simple_hash(text):
    hash_value = 0
    for char in text:
        hash_value = (hash_value * 31 + ord(char)) % 1000000007
    return hash_value

# Three-Level Authentication system
class ThreeLevelAuthSystem:
    def __init__(self):
        self.users = {}
        self.rate_limiter = RateLimiter(max_attempts=3, window_seconds=60)
        self.session_manager = SessionManager()

    def register_user(self, user_id, pass_level1, pass_level2, pass_level3):
        self.users[user_id] = (
            simple_hash(pass_level1),
            simple_hash(pass_level2),
            simple_hash(pass_level3),
        )
        log_attempt("authentication.log", f"User {user_id} registered")
        print(f"User {user_id} registered successfully!")

    def authenticate_user(self, user_id, pass_level1, pass_level2, pass_level3):
        if user_id not in self.users:
            log_attempt("authentication.log", f"User {user_id} not found")
            print("Authentication failed: User not found.")
            return False

        if not self.rate_limiter.is_allowed(user_id):
            print("Rate limit exceeded. Please try again later.")
            return False

        stored_pass1, stored_pass2, stored_pass3 = self.users[user_id]
        if (
            stored_pass1 == simple_hash(pass_level1)
            and stored_pass2 == simple_hash(pass_level2)
            and stored_pass3 == simple_hash(pass_level3)
        ):
            log_attempt("authentication.log", f"User {user_id} authenticated successfully")
            print("Access granted!")
            self.session_manager.create_session(user_id)
            return True
        else:
            log_attempt("authentication.log", f"Authentication failed for User {user_id}")
            print("Access denied: Incorrect passwords.")
            return False

    def logout_user(self, user_id):
        self.session_manager.terminate_session(user_id)

def main():
    auth_system = ThreeLevelAuthSystem()

    while True:
        print("\nThree-Level Password System")
        print("1. Register a new user")
        print("2. Authenticate a user")
        print("3. Logout a user")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            pass_level1 = input("Enter first-level password: ")
            pass_level2 = input("Enter second-level password: ")
            pass_level3 = input("Enter third-level password: ")
            auth_system.register_user(user_id, pass_level1, pass_level2, pass_level3)

        elif choice == "2":
            user_id = input("Enter user ID: ")
            pass_level1 = input("Enter first-level password: ")
            pass_level2 = input("Enter second-level password: ")
            pass_level3 = input("Enter third-level password: ")
            auth_system.authenticate_user(user_id, pass_level1, pass_level2, pass_level3)

        elif choice == "3":
            user_id = input("Enter user ID: ")
            auth_system.logout_user(user_id)

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

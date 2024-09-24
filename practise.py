
def sign_in_simulation():
    # Predefined username and password
    correct_username = "MANASA"
    correct_password = "1234"

    print("Welcome to the Sign-In Page")

    # Get user input
    username = input("Enter your username: ").strip().upper()
    password = input("Enter your password: ")

    # Check if the credentials are correct
    if username == correct_username and password == correct_password:
        print("Sign-in successful!")
    else:
        print("Invalid username or password. Please try again.")

# Run the sign-in simulation
if __name__ == "__main__":
    sign_in_simulation()

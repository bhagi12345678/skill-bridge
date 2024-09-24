from twilio.rest import Client

def sign_in_simulation():
    # Predefined username and password
    correct_username = "BHARGAVI"
    correct_password = "0506"

    print("Welcome to the Sign-In Page")

    for attempt in range(2):  # Allow 2 attempts in total
        # Get user input
        username = input("Enter your username: ").strip().upper()  # Normalize username
        password = input("Enter your password: ")

        # Basic validation for empty input
        if not username or not password:
            print("Username and password cannot be empty. Please try again.")
            continue

        # Check if the credentials are correct
        if username == correct_username and password == correct_password:
            print("Sign-in successful!")
            send_successful_sign_in_sms()  # Call function to send SMS
            return  # Exit the function on successful sign-in
        else:
            if attempt < 1:  # If not the last attempt
                print("Invalid username or password. Please try again.")
            else:
                print("Invalid username or password. No attempts remaining.")
    print("Sign-In failed please contact customer support!")


def send_successful_sign_in_sms():
    # Twilio authentication details (included directly for testing)
    account_sid = "ACefb5a45c2810cbc85085a2b90108a0a0"
    auth_token = "1133c89f7a030dd3ea1717b9e97f4210"
    client = Client(account_sid, auth_token)

    # Send an SMS when the user signs in successfully
    message = client.messages.create(
        body="Sign-in successful for BHARGAVI.",
        from_="+18319997657",  # Your Twilio phone number
        to="+91 0000000000",  # Your phone number
    )

    # Print confirmation
    print(f"Message sent: {message.body}")


# Run the sign-in simulation
if __name__ == "__main__":
    sign_in_simulation()

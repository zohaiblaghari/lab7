def login(user_credentials, username , password):
    if username in user_credentials and user_credentials[username] == password:
        print("Welcome,", username + "!")
    else:
        print("Incorrect username or password, please try again.")

if __name__ == "__main__":
    user_credentials = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }

    username = input("Enter your username:")
    password = input("Enter your password:")

    login(user_credentials, username, password)
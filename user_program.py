def save_user(username, age):
    try:
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")
    except Exception as e:
        print("Error saving to file:", e)


def display_users():
    try:
        with open("users.txt", "r") as file:
            print("\nSaved Users:")
            print(file.read())
    except FileNotFoundError:
        print("\nNo users found yet.")
    except Exception as e:
        print("Error reading file:", e)


try:
    username = input("Enter username: ").strip()

    if username == "":
        raise ValueError("Username cannot be empty.")

    age_input = input("Enter age: ")
    age = int(age_input)

    if age <= 0:
        raise ValueError("Age must be positive.")

    save_user(username, age)
    display_users()

except ValueError as ve:
    print("Input Error:", ve)

finally:
    print("System complete.")
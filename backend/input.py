def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

if __name__ == "__main__":
    user_name, user_age = get_user_input()
    print("Input received successfully")
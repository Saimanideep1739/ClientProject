from input import get_user_input

def display_output(name, age):
    print("----- User Details -----")
    print("Name:", name)
    print("Age:", age)

if __name__ == "__main__":
    name, age = get_user_input()
    display_output(name, age)

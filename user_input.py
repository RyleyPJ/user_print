def get_user_input():
    name = input("Enter your name")
    age = input("Enter your age")
    return name, age

def print_greeting(name, age):
    print(f"Hello {name}! You are {age} years old")

# Main program
    
    if __name__ == "__main__":
        # Get's user input
        user_name, user_age = get_user_input()

        # Prints personalized greeting

        print_greeting(user_name, user_age)
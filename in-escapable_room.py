def start_room():
    print("You are in a locked room. There is a door with a keypad and a table with a note.")
    print("What would you like to do?")
    print("1. Read the note")
    print("2. Inspect the keypad")
    print("3. Try to open the door")

    choice = input("> ")

    if choice == "1":
        read_note()
    elif choice == "2":
        inspect_keypad()
    elif choice == "3":
        try_door()
    else:
        print("Invalid choice. Try again.")
        start_room()

def read_note():
    print("The note says: 'The key to escape is the sum of the first four prime numbers.'")
    start_room()

def inspect_keypad():
    print("The keypad requires a 2-digit code.")
    print("Enter the code:")

    code = input("> ")
    
    if code == "17":  # The sum of the first four prime numbers (2, 3, 5, 7)
        print("The door unlocks! You have escaped the room.")
    else:
        print("Incorrect code. Try again.")
        start_room()

def try_door():
    print("The door is locked. You need to find the code to unlock it.")
    start_room()

def main():
    print("Welcome to the Escape Room Game!")
    start_room()

if __name__ == "__main__":
    main()

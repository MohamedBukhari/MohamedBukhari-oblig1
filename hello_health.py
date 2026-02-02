print("Mini Status Checker")

while True:
    status = input("Enter a number (1, 2, or 3) or q to quit: ")

    if status == "q":
        print("Goodbye!")
        break
    elif status == "1":
        print(f"Status {status}: System is running normally.")
    elif status == "2":
        print(f"Status {status}: System needs attention.")
    else:
        print(f"Status {status}: Invalid input, try again.")
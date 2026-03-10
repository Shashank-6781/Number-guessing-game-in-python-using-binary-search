def guessnumber(startRange, endRange):

    if startRange > endRange:
        return True
    
    mid = (startRange + endRange)/ 2

    print(f"Is the number {mid}? (Y/N): ", end = "")
    user = input().strip()

    if user in ("Y", "y"):
        print("Coungratulations!, You guessed the number.")
        return False
    
    elif user in ("N", "n"):
        print(f"Is the actual number greater than the {mid}? (Y/N): ", end = "")
        user = input().strip()

        if user in ("Y", "y"):
            return guessnumber(mid + 1, endRange)
        elif user in ("N", "n"):
            return guessnumber(startRange, mid - 1)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            return guessnumber(startRange, endRange)

    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        return guessnumber(startRange, endRange)

if __name__ == "__main__":
    print("Number Guessing Game inn Python")

    startRange = int(input("Enter the Start Range: "))
    endRange = int(input("Enter the End Range: "))

    print(f"Think of a number between {startRange} and {endRange}. I will try to guess it!")

    out = guessnumber(startRange, endRange)

    if out:
        print("Couldn't guess it correcty. Are you sure you answered it correctly!!!")


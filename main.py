def main():
    num = int(input("Enter a number : "))
    if num%2 == 0 and num%3 != 0:
        print ("The number is divisible by 2 but not 3.")
    elif num%2 != 0 and num%3 == 0:
        print ("The number is divisible by 3 but not 2.")
    elif num%2 == 0 and num%3 == 0:
        print ("The number is divisible by 2 and 3 both.")
    else:
        print("The number is neither divisible by 2 nor by 3.")

while True:
    main()

    continuity = input("Want to continue? (yes: y, no: n)): ")
    
    match continuity:
        case "y": continue
        case "n": print("\nThanks for using the program. Have a good day!"); input(); break

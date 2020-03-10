def main():
    
    # Create and initialise choice to an invalid choice
    choice = ""

    print("Welcome to the cyber-security program!")
    print()

    # Input validation loop
    while choice != "4":
        # Display the menu options
        print("""Please choose from the following options:

1 - Perform a port scan
2 - Brute force a password
3 - Set up firewall
4 - Quit
""")

        choice = input("Please enter your choice: ")

        # Switch user towards correct action
        if choice == "1":
            print("You chose option 1")
        elif choice == "2":
            print("You chose option 2")
        elif choice == "3":
            print("You chose option 3")
        elif choice == "4":
            print("Bye! It was nice to meet you.")
        else:
            print("Invalid choice, make sure you pick \
            between 1 and 4 only")
        




if __name__=="__main__":
    main()
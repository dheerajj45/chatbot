from colorama import Fore, init

# Initialize colorama for colored text
init(autoreset=True)


def transport_chatbot():
    # Greet and ask for user's name
    user_name = input(
        "Hello! Welcome to Transport Helpdesk. Please enter your name: ")
    print(f"\nHi {user_name}! How can I assist you today?")

    while True:
        # Display menu options
        print("\nPlease choose an option (1-7):")
        print("1. Address Update Related")
        print("2. Regarding No-Show")
        print("3. Profile Suspension")
        print("4. Transport Charges")
        print("5. Cut-off Time to Book Cab")
        print("6. Other")
        print("7. Exit")

        # Get user input with error handling
        choice = input("\nEnter your choice: ").strip()

        # Check for exit first
        if choice == '7':
            print(Fore.GREEN + "\nThank you for reaching out. Have a great day!")
            break  # Exit the loop and end the program

        try:
            # Convert input to integer
            choice = int(choice)
        except ValueError:
            print(Fore.RED + "\nInvalid input! Please enter a number between 1-7.")
            continue  # Skip to next loop iteration

        # Handle valid numeric choices
        if choice == 1:
            print(Fore.CYAN + "\nAddress Update Response:")
            print("- Update your address in TalentKonnect.")
            print("- Post updating, you'll receive an auto-generated email.")
            print(
                "- Share that email with the transport team along with latitude & longitude.")
        elif choice == 2:
            print(Fore.CYAN + "\nNo-Show Policy:")
            print("- If you encounter 3 no-shows in a 30-day cycle from the 1st no-show, your profile will be suspended.")
            print(
                "- Post approval from your respective Business COO, the profile will be reactivated.")
            print(
                "- If you have 0 no-shows in the next 30 days after the 1st no-show, it will be waived off.")
            print("- Note: Only login cab no-shows count toward suspension.")
        elif choice == 3:
            print(Fore.CYAN + "\nProfile Suspension:")
            print("- Profile suspension occurs due to 3 no-shows within 30 days.")
            print("- To reactivate, seek approval from your Business COO.")
        elif choice == 4:
            print(Fore.CYAN + "\nTransport Charges:")
            print("- Charges are deducted after cab usage.")
            print(
                "- Example: If you use the cab in January, charges will be deducted in February's payroll.")
        elif choice == 5:
            print(Fore.CYAN + "\nCut-off Time to Book/Cancel Cab:")
            print("- Book or cancel login cabs by 17:00hrs the day prior.")
        elif choice == 6:
            print(Fore.CYAN + "\nOther Queries:")
            print("- Please reach out to the transport team at xyz.com.")
        else:
            print(Fore.RED + "\nInvalid choice. Please select a number between 1-7.")


# Run the chatbot
if __name__ == "__main__":
    transport_chatbot()

# while loop

print("\n== Library Menu ==")
print("1.Library hour for today ")
print("2.Library Facility")
print("3.Find book")
print("E - Exit")
choice = input("Input your choice: ")

while choice != "E" and choice != "e":                                                                 #later in the loop, menu has to be display in order to escape the while loop
    if choice == "1":
        print("\nMonday-Friday\t\t07:00 am - 10-00 pm\nSaturday-Sunday\t\t09:00 am - 09:00 pm")
    elif choice == "2":
        print("\nThe library has 5 floors\nThe library has more than 30000 books in total\nThe library has elevator")
    elif choice == "3":
        print("\nThere are five subjects\n M-Math\n P-Physic\n P-Physhcology\n E-Economic\n B-Business")
        subject = input("Input the initial subject: ")
        if subject == "M" or subject == "P" or subject == "E" or subject == "B":
            title = input("Input the title of the book: ")
            if len(title) != 0:
                print("\nThe book is available in library\nCome and ask one of library assistants for assistance")
        else:
            print("Invalid subject initial")

    else:
        print("Invalid input")

    print("\n== Library Menu ==")
    print("1.Library hour for today ")
    print("2.Library Facility")
    print("3.Find book")
    print("E - exit")
    choice = input("Input your choice: ")


if choice == "E" or choice == "e":
    print("\nThank you for checking our library\n\tHave a good day!")




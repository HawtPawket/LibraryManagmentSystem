import mainUI




while True:
    print("\nWelcome to the Library Management System!\n\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit\n")
    try:
        choice = int(input("Please pick an option to continue: "))
        if choice not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid option. (1-5)")        
        elif choice == 1:
            mainUI.book_operations()
        elif choice == 2:
            mainUI.user_operations()
        elif choice == 3:
            mainUI.author_operations()
        elif choice == 4:
            mainUI.genre_operations()
        elif choice == 5:
            print("You are now exiting the Library Management System...")
            break
    except Exception as e:
        print(e)


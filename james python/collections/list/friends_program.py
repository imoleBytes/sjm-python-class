friends = ['Maleek', 'Praise', 'Esther', 'Clinton', 'David']

print("Welcome Facebook")
name = input("State your Name: ")

while True:
    print("""
        1.  Show Friends
        2.  Add a friend
        3.  Show Number of Friends
        4.  Edit Name of Friend
        5.  Remove a friend
    """)
    
    option = input(f"{name}, Select an option: (1-5) ")

    if option == "1":
        print(f"These are your friends: {friends}")
    elif option == "2":
        names = input("Add Friends name: (comma separated)")

        names_l = names.split(",")
        for i in names_l: # ["james"]
            friends.append(i)

        # friends.append(f_name)
        print("Friends Name added successfully...")
    elif option == "3":
        num = len(friends)
        print(f"You have {num} friends.")
    elif option == "4":
        friend_pos = int(input(f"Choose the index of the Friend You want to rename: (1-{len(friends)}): ")) - 1
        new_name = input("Enter friend's New Name: ")

        friends[friend_pos] = new_name

        print("Friends Name updated successfully...")
    
    elif option == "5":
        name_to_remove = input("Name of Friend to remove: ")
        friends.remove(name_to_remove)
        print("Friend removed successfully")
    else:
        print("Invalid command, be responsible, dumbass!")








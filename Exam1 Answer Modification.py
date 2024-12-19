library_name="My library"
action_list_for_library=['# list',
                         '# search',
                         '# register',
                         '# delete',
                         '# quit']
decoration=("-"*20)
wrong_input="Wrong input"
registering_book_list=[]
registered_book_list=[]
input_validation=False
while input_validation!=True:
    print(library_name)
    print(decoration)
    count=1
    for i in action_list_for_library:
        print(i)
        count=count+1
    print(decoration)

    menu_select=input("Please select a menu:")
    if menu_select=="list":
        if not registering_book_list:
            print(decoration*2)
            print("There is no book registered in the list yet.")
            print(decoration*2)
        else:
            count=1
            for k in registering_book_list:
                str_count=str(count)
                print("["+(str_count)+"]"+" "+k)
                # registered_book_list.append("["+(str_count)+"]"+" "+k)
                count=count+1
    elif menu_select=="search":
        to_search=input("Enter the book name to search:")
        searched_list=[]
        for match in registered_book_list:
            if to_search in match:
                searched_list.append(match)
        if len(searched_list)!=0:
            for j in searched_list:
                print(j)
        else:
            print("no book is found")
    elif menu_select=="register":
        input_validation=True
        while input_validation==True:
            to_register=input("Enter the book name to register. If you are done, just press the Enter key to go back to menu:")
            if to_register=="":
                input_validation=False
            else:
                registering_book_list.append(to_register)
                count=1
                for book_name in registering_book_list:
                    registered_book_list.append("["+str(count)+"]"+" "+book_name)
                    count=count+1
    elif menu_select=="delete":
        to_delete=input("Enter the book number or its full name to delete:")
        if to_delete.isnumeric():        
            if int(to_delete)>0 and int(to_delete)<=len(registering_book_list):
                print_book_name=registering_book_list[int(to_delete)-1]
                ask_to_confirm=input("Please confirm to delete "+print_book_name+" (y):")
                if ask_to_confirm=="y":
                    registering_book_list.pop(int(to_delete)-1)
                    print(print_book_name+ " has been successfully deleted from the list.")
                elif ask_to_confirm=="n":
                    print("Canceled")
                else:
                    print("Canceled")
            else:
                print(decoration)
                print(wrong_input)
                print(decoration)
        elif to_delete.isalpha():
            if to_delete in registering_book_list:
                registering_book_list.remove(to_delete)
                print(to_delete+ " has been successfully deleted from the list.")
            else:
                print(decoration)
                print(wrong_input)
                print(decoration)
    elif menu_select=="quit":
        input_validation=True
        print("Quit")
    else:
        input_validation=False


    
   


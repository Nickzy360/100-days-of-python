todolist = [ ]
menu = ['1.Add','2.Remove','3.Show list', '4.Exit']
print(menu)
while True:
    option = int(input("Choose an option "))

    if option == 1:
        add = input("input what you want to add: ")
        todolist.append(add)    
    elif option == 2:
        remover = int(input("input which one you want to remove: "))
        todolist.pop(remover)
    elif option == 3:
        print(todolist)
    else:
        print("Exit")  
        break

# Abhay Prasanna Rao

import sys
import pickle

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    global itemFound
    itemFound=False
    global keyName
    keyName=""
    global index
    index = -1
    for i in todoList:
        if item in todoList[i]:
            keyName=i
    if keyName=="":
        sys.exit
    else:
        index=[n.index(item) for m, n in todoList.items() if item in n]
        itemFound=True
    return itemFound, keyName, index

def addItem(item, todoList):
    checkItem(item, todoList)
    toList="backlog"
    if itemFound == False:
        todoList[toList] += [item]
    else:
        print(f"{item} already exists in {keyName} at index {index}")
    return todoList

def deleteItem(item, todoList):
    checkItem(item, todoList)
    if itemFound == True:
        todoList[keyName].remove(item)
    else:
        print(f"{item} doesn't exist in todolist")
    return itemFound, todoList

def moveItem(item, toList, todoList):
    deleteItem(item, todoList)
    if itemFound==True:
        todoList[toList]+=[item]  
    return todoList

def printTODOList(todoList):
    for i in todoList:
            key=i
            print (f"{key}: {todoList[i]}")
    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            item=str(input("Enter the item to add: "))
            addItem(item, todoList)
            printTODOList(todoList)
            pass

        elif choice == "m":
            while True:
                item= str(input("Enter the item to move: "))
                checkItem(item, todoList)
                if itemFound==True:
                    while True:
                        toList=str(input(f"Enter the list to add {item} to: "))
                        check=""
                        for i in todoList:
                            if toList==i:
                                check=i       
                        if check==toList:            
                            moveItem(item, toList, todoList)
                            break
                        else:
                            print("The key you entered does not exist. Please enter a new key")
                    printTODOList(todoList)
                    break
                else:
                    print("The item you entered does not exist. Please enter a different item.")
            pass
        elif choice == "d":
            item=str(input("enter the item to delete: "))
            deleteItem(item, todoList)
            printTODOList(todoList)
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    taskOver = False

    print("TaskFlow: The Ultimate TODO List Manager")
    print()
    
    print("Name: Abhay Prasanna Rao")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()
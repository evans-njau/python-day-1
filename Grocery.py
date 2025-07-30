Grocery_List = []

while True:
  print("Choose an option:")
  print("1. Add item")
  print("2. Remove item")
  print("3. View list")
  print("4. Sort list")
  print("5. Search item")
  print("6. Exit")

  choice = int(input("Make a choice: "))
  if(choice == 1):
    name = str(input("Add a grocery: "))
    Grocery_List.append(name)
    print(f"{name} added")
  elif(choice == 2):
    name = str(input("Name of item to remove"))    
    if name in Grocery_List:
        Grocery_List.remove(name)
        print(f"{name} removed!")
    else:
        print("item not found")    
  elif(choice == 3):
    for grocery in Grocery_List:
        print(grocery)
  elif(choice == 4):
    Grocery_List.sort()
    print("list sorted alphabetically") 
  elif(choice == 5):
    item = str(input("Input item to search: ")) 
    if item in Grocery_List:
        print(f"{item} is in the list.")
    else:
        print(f"{item} not found")                
  elif(choice == 6):
    print("Exiting grocery store Goodbye!") 

    break 
  else:
    print("Invalid choice choose between 1-6")          
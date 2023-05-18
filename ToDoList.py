# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MCambra,5.17.2023,Added code per each section prompt
# ------------------------------------------------------------------------ #

# ---- Data / Main Variables ---- #
# Declare variables and constants
objFileName = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection

# ---- Begin Processing ---- #
# Step 1 - When the program starts, Load from ToDoFile.txt into a python Dictionary.
objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Welcome to your To-Do-List!
    ----- MAIN MENU -----
    1.) Display current data
    2.) Add a new item
    3.) Remove an existing item
    4.) Save Data to File
    5.) Exit Program
    """)
    strChoice = str(input("What would you like to do? [Options 1 - 5]: "))

    print()  # Blank line

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("----- CURRENT ITEMS -----")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("-------------------------")
        continue  # Back to Main Menu

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = str(input("Please name the task:  ")).strip()
        strPriority = str(input("What is the priority? [high|low]: ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)

        #Step 4a - Show the current items in the table
        print("----- CURRENT ITEMS -----")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("-------------------------")
        continue  # Back to Main Menu

    # Step 5 - Remove a new item to the list/Table
    elif strChoice == '3':
        #Step 5a - Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]      # Deletes the matching item
                blnItemRemoved = True
            intRowNumber += 1

        #Step 5b - Update user on the status
        if blnItemRemoved == True:
            print("The task has left the building!")
        else:
            print("Sorry, I could not find that task. :(")

        #Step 5c - Show the current items in the table
        print("----- CURRENT ITEMS -----")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("-------------------------")
        continue  # Back to Main Menu

    # Step 6 - Save tasks to the ToDoFile.txt file
    elif strChoice == '4':
        #Step 5a - Show the current items in the table
        print("----- CURRENT ITEMS -----")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("-------------------------")

        #Step 5b - Ask if they want save that data
        if "y" == str(input("Save this data to the file? (y/n): ")).strip().lower():
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")     # Writes only the items
            objFile.close()
            input("Data has been saved! Press the </ENTER> key to return to the Main Menu.")
        else:
            print("""
            Oh No! The data was NOT Saved!
            Don't worry! I still have the old stuff!""")
            input("Press the </ENTER> key to return to menu.")
        continue  # Back to Main Menu

    elif strChoice == '5':
        break   # Exit the program

# ---- End Processing ---- #
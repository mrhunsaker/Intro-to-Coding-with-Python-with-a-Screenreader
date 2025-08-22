Curriculum: Introduction to Computer Science with Python for Visually Impaired Students
Unit 0: Setting Up Your Accessible Python Development Environment
Unit Goal: To guide students through installing all necessary software and configuring their development environment (VS Code and their screen reader) to be efficient and accessible for Python programming.
Lesson 0.1: Installing Python and Visual Studio Code
Student Materials:
     Outline:
         Why these tools are essential for programming.
         Step-by-step instructions for downloading and running the Python 3 installer, with specific accessibility notes (e.g., "Add Python to PATH" checkbox).
         Step-by-step instructions for downloading and running the VS Code installer, with specific accessibility notes (e.g., "Add to PATH" checkbox).
         How to verify installations using a basic command in the system terminal (python3 --version, code --version).
     Skills Checklist:
         [ ] I can successfully download the Python 3 installer for my operating system.
         [ ] I can run the Python installer and correctly select the "Add Python to PATH" option.
         [ ] I can successfully download the VS Code installer for my operating system.
         [ ] I can run the VS Code installer and correctly select the "Add to PATH" option.
         [ ] I can open my computer's system terminal (Command Prompt/PowerShell/Terminal).
         [ ] I can verify Python's installation by running python3 --version in the terminal.
         [ ] I can verify VS Code's installation by running code --version in the terminal.
Lesson 0.2: Configuring Your Screen Reader for VS Code
Student Materials:
     Outline:
         Introduction to VS Code's "Screen Reader Optimized Mode" and how to toggle it.
         Understanding the "Accessible View" and its purpose (Shift + Alt + F2).
         Emphasizing keyboard-first navigation: using Tab, Shift+Tab, and Arrow keys.
         The importance of the Status Bar and how to access its information.
         Specific, step-by-step instructions for configuring indentation announcement (or beeps) in NVDA, JAWS, and VoiceOver.
         Practice navigating code with indentation to hear the screen reader feedback.
     Skills Checklist:
         [ ] I can identify and toggle VS Code's "Screen Reader Optimized Mode" using the Command Palette.
         [ ] I can open and close the "Accessible View" to access hidden information.
         [ ] I can navigate between different VS Code panes (editor, sidebar, panel) using Tab and Shift+Tab.
         [ ] I can navigate line by line and character by character within the editor using arrow keys.
         [ ] I can locate and listen to information in the VS Code Status Bar.
         [ ] I can configure my specific screen reader (NVDA/JAWS/VoiceOver) to announce or beep on indentation changes.
         [ ] I can confidently interpret my screen reader's feedback regarding code indentation.
Lesson 0.3: Setting Up Your VS Code Workspace
Student Materials:
     Outline:
         How to open the Extensions View in VS Code (Ctrl + Shift + X).
         Step-by-step for searching and installing the essential "Python" extension by Microsoft.
         Step-by-step for searching and installing the recommended "Pylance" extension.
         The importance of organizing projects in dedicated workspace folders.
         How to create a new folder for Python projects.
         Two methods for opening a project folder in VS Code (code . from terminal, or "Open Folder" command).
         Detailed keyboard shortcuts for navigating key VS Code areas: Activity Bar, Explorer, Editor Group, Panel, and the powerful Command Palette.
     Skills Checklist:
         [ ] I can open the Extensions View in VS Code.
         [ ] I can search for and install the "Python" extension by Microsoft.
         [ ] I can search for and install the "Pylance" extension.
         [ ] I can create a new folder on my computer for Python projects.
         [ ] I can open a specific folder as a workspace in VS Code.
         [ ] I can navigate the Activity Bar, Explorer, Editor, and Panel using keyboard shortcuts.
         [ ] I can effectively use the Command Palette (Ctrl + Shift + P) to find and execute commands.
Lesson 0.4: Python Environments and Terminal Usage
Student Materials:
     Outline:
         How to create, save, and open a new Python file (.py).
         Running a basic Python script (print("Hello!")) using the system terminal.
         Running the same script using the integrated terminal within VS Code.
         The concept of Python virtual environments: why they are important for project isolation.
         Step-by-step instructions for creating a virtual environment using python3 -m venv .venv.
         Instructions for activating the virtual environment on Windows (Command Prompt/PowerShell) and macOS/Linux.
         How to deactivate a virtual environment.
         Crucially, how to "Select Interpreter" in VS Code to ensure it uses your virtual environment's Python.
         Installing Python packages (libraries) like requests using pip within the active virtual environment.
         Verifying installed packages using pip list.
     Skills Checklist:
         [ ] I can create a new Python file (.py) in VS Code.
         [ ] I can save a Python file into my project folder.
         [ ] I can write a simple print() statement in a Python file.
         [ ] I can run a Python script from my system terminal.
         [ ] I can open and run a Python script from the integrated terminal in VS Code.
         [ ] I understand why virtual environments are useful.
         [ ] I can create a new virtual environment within my project folder.
         [ ] I can activate and deactivate a virtual environment specific to my operating system.
         [ ] I can select the correct Python interpreter (my virtual environment) within VS Code.
         [ ] I can install Python packages using pip into my active virtual environment.
         [ ] I can list installed packages using pip list.
Unit 1: Foundations of Computing and Getting Started with Python
Unit Goal: To introduce basic computer science concepts and the fundamentals of writing and executing simple Python programs.
Lesson 1.1: Welcome to Computer Science
Student Materials:
     Outline:
         Definition of computer science: what it studies.
         Distinction between hardware (physical parts) and software (programs).
         What is a "program" in the context of a computer?
         Introduction to programming languages (like Python) as a way to "talk" to computers.
         The role of the programmer.
     Skills Checklist:
         [ ] I can define what computer science is.
         [ ] I can distinguish between computer hardware and software.
         [ ] I can explain what a computer program is.
         [ ] I can identify Python as a programming language.
Lesson 1.2: Your First Python Program: "Hello World!"
Student Materials:
     Outline:
         The print() function: its purpose and basic syntax.
         Writing the "Hello World!" program.
         Saving a Python file (.py extension).
         Executing the Python script from the terminal (revisiting skills from Unit 0).
         Understanding that print() outputs text to the terminal.
     Skills Checklist:
         [ ] I can write a print() statement in Python.
         [ ] I can save a Python file with the .py extension.
         [ ] I can execute a Python script from the terminal.
         [ ] I can understand that the output of print() appears in the terminal.
Lesson 1.3: Variables and Simple Data Types
Student Materials:
     Outline:
         The concept of a variable as a container for storing information.
         Rules for naming variables (e.g., no spaces, can't start with a number).
         Introduction to string data type (text, enclosed in quotes).
         Introduction to integer data type (whole numbers).
         Introduction to float data type (numbers with decimal points).
         Assigning values to variables using the = operator.
         Using print() to display variable values.
         Performing simple arithmetic operations (+, -, *, /) with numbers.
     Skills Checklist:
         [ ] I can define what a variable is in programming.
         [ ] I can create a valid variable name in Python.
         [ ] I can assign a string value to a variable.
         [ ] I can assign an integer value to a variable.
         [ ] I can assign a float value to a variable.
         [ ] I can use print() to display the value of a variable.
         [ ] I can perform basic addition, subtraction, multiplication, and division with numbers in Python.
Unit 2: Writing Simple Programs and Numeric Computations
Unit Goal: To deepen understanding of the software development process and work effectively with numeric data and basic mathematical functions.
Lesson 2.1: The Software Development Process
Student Materials:
     Outline:
         Introduction to the structured approach of building software.
         Phases of software development:
             Problem Solving/Analysis: Understanding what needs to be done.
             Design: Planning how to solve the problem (e.g., what steps, what data).
             Implementation/Coding: Writing the actual Python code.
             Testing: Checking if the code works as expected and finding bugs.
             Maintenance: Updating and improving the code over time.
         Emphasis on iterative development (doing small cycles of these steps).
     Skills Checklist:
         [ ] I can describe the purpose of the software development process.
         [ ] I can list and briefly explain the main phases of software development.
         [ ] I understand that problem-solving and design happen before writing code.
Lesson 2.2: Elements of Programs: Expressions and Assignment
Student Materials:
     Outline:
         What is an "expression" in Python (something that produces a value, like 3 + 5).
         How Python evaluates expressions.
         The assignment statement (=): storing the result of an expression into a variable.
         Understanding variable reassignment (a variable can hold different values over time).
     Skills Checklist:
         [ ] I can identify an expression in Python code.
         [ ] I can predict the result of simple Python expressions.
         [ ] I can explain how the assignment operator (=) works.
         [ ] I can demonstrate how to update the value stored in a variable.
Lesson 2.3: Input and Output Revisited
Student Materials:
     Outline:
         Using the input() function to get data from the user.
         Understanding that input() always returns a string.
         Prompting the user with clear, descriptive messages in input().
         Formatting output with print():
             Concatenating strings (using +).
             Using f-strings (formatted string literals) for easy variable inclusion (e.g., f"My name is {name}.").
     Skills Checklist:
         [ ] I can use the input() function to ask the user for information.
         [ ] I can provide a clear prompt message to the user when using input().
         [ ] I remember that input() returns a string, even for numbers.
         [ ] I can combine text and variable values in a print() statement using f-strings.
Lesson 2.4: Computing with Numbers and Type Conversions
Student Materials:
     Outline:
         Detailed review of integer (int) and float (float) types.
         When to use int (counting, whole items) vs. float (measurements, money).
         Converting between types:
             int(value): Converting to an integer (truncates decimals).
             float(value): Converting to a float.
             str(value): Converting to a string.
         Importance of type conversion for performing calculations on user input.
         Order of operations (PEMDAS/BODMAS) in Python.
     Skills Checklist:
         [ ] I can identify when to use an integer versus a float.
         [ ] I can convert a string to an integer using int().
         [ ] I can convert a string to a float using float().
         [ ] I can convert a number to a string using str().
         [ ] I can correctly apply type conversions to perform calculations on user input.
         [ ] I understand and can apply the order of operations in Python expressions.
Lesson 2.5: Using the Math Library
Student Materials:
     Outline:
         The concept of modules in Python: reusable code collections.
         How to import a module (e.g., import math).
         Accessing functions and constants within the math module using dot notation (e.g., math.pi, math.sqrt()).
         Common math functions: math.sqrt(), math.pow(), math.ceil(), math.floor().
         Application: Solving simple geometric or scientific problems.
     Skills Checklist:
         [ ] I can explain what a Python module is.
         [ ] I can import the math module into my program.
         [ ] I can use math.pi and math.e constants.
         [ ] I can calculate the square root of a number using math.sqrt().
         [ ] I can use math.pow() for exponentiation.
         [ ] I can use math.ceil() to round up and math.floor() to round down.
Unit 3: Control Flow: Decisions and Loops
Unit Goal: To enable students to control program execution flow using conditional statements and definite loops.
Lesson 3.1: Boolean Expressions and if Statements
Student Materials:
     Outline:
         Introduction to Boolean values: True and False.
         Comparison operators: == (equal to), != (not equal to), < (less than), > (greater than), <= (less than or equal to), >= (greater than or equal to).
         What is a Boolean expression (an expression that evaluates to True or False).
         The if statement: executing code only if a condition is True.
         Understanding the indentation of the code block under if.
     Skills Checklist:
         [ ] I can identify True and False as Boolean values.
         [ ] I can use comparison operators to create Boolean expressions.
         [ ] I can write a basic if statement.
         [ ] I can correctly indent the code block belonging to an if statement.
         [ ] I can predict whether an if block will execute based on its condition.
Lesson 3.2: Chained Conditionals (elif, else)
Student Materials:
     Outline:
         The else statement: executing code if the if condition is False.
         The elif statement: checking multiple conditions sequentially.
         Understanding the order of if, elif, and else blocks.
         Logical operators: and, or, not for combining Boolean expressions.
     Skills Checklist:
         [ ] I can use an else statement to provide an alternative path for an if condition.
         [ ] I can use elif to check multiple conditions in order.
         [ ] I can use the and operator to combine conditions where both must be true.
         [ ] I can use the or operator to combine conditions where at least one must be true.
         [ ] I can use the not operator to negate a Boolean expression.
         [ ] I can write code that makes decisions based on multiple conditions.
Lesson 3.3: Introduction to Lists
Student Materials:
     Outline:
         What is a list: an ordered collection of items.
         Creating lists using square brackets [].
         Items in a list can be of different data types.
         Accessing individual items by their index (position), starting from 0.
         Accessing items from the end of the list using negative indices.
         Modifying items in a list.
     Skills Checklist:
         [ ] I can create a list in Python.
         [ ] I can understand that lists are ordered collections.
         [ ] I can access individual items in a list using their index.
         [ ] I can access list items from the end using negative indices.
         [ ] I can change the value of an item at a specific index in a list.
Lesson 3.4: Iterating with for Loops
Student Materials:
     Outline:
         The concept of iteration: performing an action repeatedly for each item in a sequence.
         The for loop: iterating over elements in a list or characters in a string.
         The range() function for generating a sequence of numbers to loop a specific number of times.
         Understanding the indentation of the code block under for.
         Using the loop variable.
     Skills Checklist:
         [ ] I can explain the purpose of a for loop.
         [ ] I can write a for loop to iterate over items in a list.
         [ ] I can write a for loop to iterate over characters in a string.
         [ ] I can use the range() function to control how many times a loop runs.
         [ ] I can correctly indent the code block belonging to a for loop.
Lesson 3.5: Basic String Operations
Student Materials:
     Outline:
         Concatenating strings using the + operator.
         Finding the length of a string using len().
         Common string methods:
             .upper(): Converts to uppercase.
             .lower(): Converts to lowercase.
             .strip(): Removes leading/trailing whitespace.
             .replace(old, new): Replaces occurrences of a substring.
         Understanding that string methods return a new string, they don't modify the original string in place.
     Skills Checklist:
         [ ] I can combine two or more strings using concatenation.
         [ ] I can find the length of a string using len().
         [ ] I can convert a string to all uppercase using .upper().
         [ ] I can convert a string to all lowercase using .lower().
         [ ] I can remove extra spaces from the beginning or end of a string using .strip().
         [ ] I can replace specific parts of a string using .replace().
         [ ] I understand that string methods create new strings rather than changing the original.
Unit 4: Data Structures: Lists and Dictionaries
Unit Goal: To provide a deeper understanding of lists and introduce dictionaries for storing and organizing data.
Lesson 4.1: More on Lists
Student Materials:
     Outline:
         Adding elements to a list:
             .append(item): Adds to the end.
             .insert(index, item): Inserts at a specific position.
         Removing elements from a list:
             del list[index]: Removes by index.
             .pop(index): Removes by index and returns the item (useful for using the removed item).
             .remove(value): Removes the first occurrence of a specific value.
         Understanding when to use each removal method.
     Skills Checklist:
         [ ] I can add an item to the end of a list using .append().
         [ ] I can insert an item at a specific position in a list using .insert().
         [ ] I can remove an item from a list by its index using del.
         [ ] I can remove an item by its index and retrieve its value using .pop().
         [ ] I can remove the first occurrence of a specific value from a list using .remove().
Lesson 4.2: Organizing Lists
Student Materials:
     Outline:
         Sorting a list permanently: .sort() method.
             Default alphabetical/numerical ascending order.
             Sorting in reverse order: .sort(reverse=True).
         Sorting a list temporarily: sorted() function.
             Returns a new sorted list, leaves original unchanged.
         Reversing the order of a list: .reverse().
         Finding the length of a list: len().
     Skills Checklist:
         [ ] I can sort a list permanently in ascending order using .sort().
         [ ] I can sort a list permanently in descending order.
         [ ] I can get a temporarily sorted version of a list using sorted().
         [ ] I can reverse the current order of a list using .reverse().
         [ ] I can find out how many items are in a list using len().
Lesson 4.3: Tuples: Immutable Lists
Student Materials:
     Outline:
         Introduction to tuples: ordered collections similar to lists.
         Defining tuples using parentheses ().
         Key difference: tuples are immutable (cannot be changed after creation).
         When to use tuples (for data that shouldn't change, like coordinates or fixed settings).
         Accessing items in a tuple by index (same as lists).
         Iterating over tuples with for loops.
     Skills Checklist:
         [ ] I can create a tuple in Python.
         [ ] I can explain the main difference between a list and a tuple (mutability).
         [ ] I can identify appropriate situations for using a tuple.
         [ ] I can access items in a tuple by their index.
         [ ] I can iterate over a tuple using a for loop.
Lesson 4.4: Introducing Dictionaries
Student Materials:
     Outline:
         What is a dictionary: an unordered collection of key-value pairs.
         Creating dictionaries using curly braces {}.
         Understanding keys (unique identifiers) and values (the data associated with the key).
         Accessing values using their keys (e.g., my_dict["key"]).
         Adding new key-value pairs to a dictionary.
         Modifying existing values.
         Removing key-value pairs using del.
     Skills Checklist:
         [ ] I can create a dictionary in Python.
         [ ] I can explain what a key-value pair is.
         [ ] I can access a value in a dictionary using its key.
         [ ] I can add a new key-value pair to an existing dictionary.
         [ ] I can modify the value associated with an existing key.
         [ ] I can remove a key-value pair from a dictionary using del.
Lesson 4.5: Looping Through Dictionaries
Student Materials:
     Outline:
         Iterating over a dictionary's keys using a for loop.
         Using .values() to iterate only over the values.
         Using .items() to iterate over both keys and values simultaneously (as a pair).
         Understanding the order of items when iterating (typically insertion order in modern Python, but not guaranteed in older versions).
     Skills Checklist:
         [ ] I can loop through all the keys in a dictionary.
         [ ] I can loop through all the values in a dictionary.
         [ ] I can loop through both the keys and values of a dictionary at the same time.
         [ ] I can perform actions for each key, value, or key-value pair in a dictionary.
Unit 5: User Input and while Loops
Unit Goal: To enable students to interact more dynamically with users and control program flow using indefinite loops.
Lesson 5.1: How the input() Function Works
Student Materials:
     Outline:
         Recap of input() for getting user data.
         Confirming that input() always returns a string, regardless of what the user types.
         Importance of type conversion (int(), float()) when numeric input is needed.
         Handling prompts and making them clear for screen reader users.
     Skills Checklist:
         [ ] I can effectively use input() to get user data.
         [ ] I can confirm that input()'s return value is always a string.
         [ ] I can convert user input to a numeric type when necessary.
         [ ] I can write clear and concise prompts for user input.
Lesson 5.2: The while Loop in Action
Student Materials:
     Outline:
         Introduction to while loops: repeating code as long as a condition is true.
         Distinction from for loops (definite vs. indefinite iteration).
         Defining the loop condition (a Boolean expression).
         Ensuring the condition eventually becomes false to avoid infinite loops.
         Incrementing/decrementing a counter within the loop to control repetitions.
         Understanding the indentation of the code block under while.
     Skills Checklist:
         [ ] I can explain the difference between a for loop and a while loop.
         [ ] I can write a basic while loop.
         [ ] I can define the condition that controls a while loop.
         [ ] I can make sure my while loop has a way to stop (avoiding infinite loops).
         [ ] I can correctly indent the code block belonging to a while loop.
Lesson 5.3: Using Flags and break to Exit Loops
Student Materials:
     Outline:
         Using a "flag" variable (a Boolean variable) to control while loop execution.
         The break statement: immediately exiting the current loop, regardless of the condition.
         When to use break (e.g., when a specific event occurs, like a "quit" command).
     Skills Checklist:
         [ ] I can use a Boolean "flag" variable to control a while loop.
         [ ] I can use the break statement to exit a loop early.
         [ ] I can decide when break is an appropriate tool for loop control.
Lesson 5.4: Using continue in Loops
Student Materials:
     Outline:
         The continue statement: skipping the rest of the current iteration and moving to the next iteration of the loop.
         When to use continue (e.g., processing certain items but skipping others based on a condition).
     Skills Checklist:
         [ ] I can use the continue statement to skip the rest of the current loop iteration.
         [ ] I can identify scenarios where continue would be useful.
Lesson 5.5: Avoiding Infinite Loops
Student Materials:
     Outline:
         Recap: What an infinite loop is (a loop that never ends).
         Common causes of infinite loops (e.g., condition never becomes false, forgetting to update a counter).
         How to stop an infinite loop in the terminal (Ctrl + C).
         Strategies for preventing infinite loops during development.
     Skills Checklist:
         [ ] I can define what an infinite loop is.
         [ ] I can identify common causes of infinite loops.
         [ ] I know how to stop a running Python program that is in an infinite loop.
         [ ] I can write while loops that are guaranteed to terminate.
Unit 6: Functions
Unit Goal: To enable students to organize and reuse code by defining and using functions.
Lesson 6.1: Defining Functions
Student Materials:
     Outline:
         The concept of code reusability and organization.
         Syntax for defining a function using def keyword.
         Function naming conventions.
         Understanding parameters (placeholders for inputs) in the function definition.
         The importance of indentation for the function body.
         Calling (executing) a function by its name followed by parentheses.
     Skills Checklist:
         [ ] I can explain why functions are useful for organizing code.
         [ ] I can define a simple function in Python.
         [ ] I can use parameters to specify what inputs a function expects.
         [ ] I can correctly indent the code block within a function.
         [ ] I can call (execute) a function by its name.
Lesson 6.2: Passing Arguments
Student Materials:
     Outline:
         Distinction between parameters (in definition) and arguments (values passed during call).
         Positional arguments: arguments are matched to parameters by their order.
         Keyword arguments: specifying arguments by parameter name (order doesn't matter).
         When to use positional vs. keyword arguments.
     Skills Checklist:
         [ ] I can differentiate between a parameter and an argument.
         [ ] I can pass arguments to a function using positional order.
         [ ] I can pass arguments to a function using keyword arguments.
         [ ] I can choose the appropriate method for passing arguments based on the situation.
Lesson 6.3: Return Values
Student Materials:
     Outline:
         Understanding that functions can produce a result.
         The return statement: sending a value back from a function.
         Difference between print() (displays) and return (sends back for use).
         Storing returned values in variables.
         Functions that don't explicitly return a value implicitly return None.
     Skills Checklist:
         [ ] I can use the return statement to send a value back from a function.
         [ ] I can explain the difference between print() and return.
         [ ] I can store the returned value of a function in a variable.
         [ ] I understand that functions without a return statement implicitly return None.
Lesson 6.4: Functions with Lists and Dictionaries
Student Materials:
     Outline:
         Passing lists as arguments to functions.
         Understanding that changes made to a list inside a function will affect the original list (because lists are mutable).
         Passing dictionaries as arguments to functions.
         Returning lists or dictionaries from functions.
         Making a copy of a list (list[:]) or dictionary (dict.copy()) if you don't want the original to be modified.
     Skills Checklist:
         [ ] I can pass a list as an argument to a function.
         [ ] I can pass a dictionary as an argument to a function.
         [ ] I understand that modifying a list/dictionary inside a function affects the original.
         [ ] I can return a list or a dictionary from a function.
         [ ] I can create a copy of a list or dictionary to avoid unintended modifications.
Lesson 6.5: Arbitrary Number of Arguments
Student Materials:
     Outline:
         Using *args to accept an arbitrary number of positional arguments (they are collected into a tuple).
         Using **kwargs to accept an arbitrary number of keyword arguments (they are collected into a dictionary).
         When *args and **kwargs are useful (e.g., creating flexible functions).
     Skills Checklist:
         [ ] I can define a function that accepts an arbitrary number of positional arguments using *args.
         [ ] I can define a function that accepts an arbitrary number of keyword arguments using **kwargs.
         [ ] I can explain scenarios where *args or **kwargs would be beneficial.
Unit 7: Classes and Object-Oriented Programming
Unit Goal: To introduce the basics of Object-Oriented Programming (OOP) by defining and using classes, attributes, and methods.
Lesson 7.1: Why Learn About Classes?
Student Materials:
     Outline:
         Introduction to Object-Oriented Programming (OOP) as a programming paradigm.
         Analogy: Classes as blueprints or templates, objects as instances built from those blueprints.
         Key OOP concepts: objects, classes, encapsulation (bundling data and methods), abstraction (hiding complexity).
         Benefits of OOP: code organization, reusability, modularity.
     Skills Checklist:
         [ ] I can explain the basic idea of Object-Oriented Programming.
         [ ] I can describe a class as a blueprint.
         [ ] I can describe an object as an instance of a class.
         [ ] I can state at least two benefits of using OOP.
Lesson 7.2: Creating and Using a Class
Student Materials:
     Outline:
         Syntax for defining a simple class using the class keyword.
         Class naming conventions (CamelCase).
         The __init__ method: special method called when an object is created.
             Its purpose: to initialize the object's attributes (data).
             The self parameter: referring to the current instance of the object.
         Defining attributes (variables) within __init__ using self.attribute_name.
         Creating an instance (object) of a class.
     Skills Checklist:
         [ ] I can define a basic Python class.
         [ ] I can define the __init__ method within a class.
         [ ] I understand the purpose of the self parameter in class methods.
         [ ] I can define attributes for an object within the __init__ method.
         [ ] I can create an instance (object) of a class.
Lesson 7.3: Working with Attributes and Methods
Student Materials:
     Outline:
         Accessing object attributes using dot notation (e.g., my_object.attribute).
         Modifying attribute values directly.
         Defining methods (functions) within a class.
             Methods always take self as their first parameter.
             Calling methods on an object (e.g., my_object.method()).
         Using methods to update attribute values.
     Skills Checklist:
         [ ] I can access an object's attributes.
         [ ] I can modify an object's attribute directly.
         [ ] I can define a method within a class.
         [ ] I can call a method on an object.
         [ ] I can use a method to change an object's attribute.
Lesson 7.4: Inheritance
Student Materials:
     Outline:
         The concept of inheritance: creating a new class (child/subclass) based on an existing one (parent/superclass).
         Benefits of inheritance: code reuse, creating specialized versions of classes.
         Syntax for defining a child class that inherits from a parent.
         Using super().__init__() to call the parent class's __init__ method.
         Adding new attributes and methods to a child class.
         Overriding (redefining) methods from the parent class in the child class.
     Skills Checklist:
         [ ] I can explain the concept of inheritance in OOP.
         [ ] I can define a child class that inherits from a parent class.
         [ ] I can use super().__init__() to properly initialize inherited attributes.
         [ ] I can add new attributes and methods to a child class.
         [ ] I can override a parent method in a child class.
Lesson 7.5: Instances as Attributes
Student Materials:
     Outline:
         The concept of "composition": one class containing an instance of another class as an attribute.
         When to use composition vs. inheritance (is-a vs. has-a relationship).
         Examples: A Car object might have a Engine object.
         Accessing attributes and methods of the nested instance.
     Skills Checklist:
         [ ] I can explain the concept of composition in OOP.
         [ ] I can identify scenarios where composition is more appropriate than inheritance.
         [ ] I can create an instance of one class and assign it as an attribute to another class.
         [ ] I can access attributes and call methods of a nested object.
Unit 8: Files and Exceptions
Unit Goal: To enable students to interact with files for persistent data storage and to handle common programming errors gracefully.
Lesson 8.1: Reading from a File
Student Materials:
     Outline:
         The concept of persistent storage: data remaining even after the program closes.
         Opening a file for reading ("r" mode).
         The with open(...) statement: ensures files are automatically closed.
         Reading the entire content of a file (.read()).
         Reading line by line (.readline(), or iterating directly over the file object).
         Reading all lines into a list (.readlines()).
         Removing newline characters (.strip()).
     Skills Checklist:
         [ ] I can explain why persistent storage is important.
         [ ] I can open a file for reading using with open().
         [ ] I can read the entire content of a file into a string.
         [ ] I can read a file line by line using a for loop.
         [ ] I can remove leading/trailing whitespace, including newlines, from strings using .strip().
Lesson 8.2: Writing to a File
Student Materials:
     Outline:
         Opening a file for writing ("w" mode) and appending ("a" mode).
             "w" mode: creates a new file or overwrites an existing one.
             "a" mode: adds content to the end of an existing file without deleting it.
         Writing strings to a file using .write().
         Adding newline characters (\n) for proper formatting.
         Writing multiple lines from a list using .writelines().
     Skills Checklist:
         [ ] I can open a file for writing (overwriting) using "w" mode.
         [ ] I can open a file for appending using "a" mode.
         [ ] I can write a string to a file.
         [ ] I can add new lines to a file.
         [ ] I can write multiple lines from a list to a file.
Lesson 8.3: Exceptions: Handling Errors
Student Materials:
     Outline:
         What is an "exception" (an error that occurs during program execution).
         Why handle exceptions (prevent crashes, provide graceful feedback).
         The try-except block:
             Code that might cause an error goes in the try block.
             Code to handle the error goes in the except block.
         Common exception types: ValueError, ZeroDivisionError, FileNotFoundError.
         Catching specific exception types.
     Skills Checklist:
         [ ] I can explain what an exception is in programming.
         [ ] I can explain why it's important to handle exceptions.
         [ ] I can write a try-except block.
         [ ] I can catch specific types of exceptions (e.g., ValueError).
         [ ] I can provide a helpful message to the user when an error occurs.
Lesson 8.4: The else Block and finally Block
Student Materials:
     Outline:
         The else block in try-except: executes only if no exception occurred in the try block.
         The finally block in try-except: executes regardless of whether an exception occurred or not (useful for cleanup).
     Skills Checklist:
         [ ] I can use an else block with try-except for code that runs only on success.
         [ ] I can use a finally block with try-except for code that always runs.
Lesson 8.5: Storing Data with JSON
Student Materials:
     Outline:
         Introduction to JSON (JavaScript Object Notation) as a common format for data exchange.
         JSON's relationship to Python dictionaries and lists.
             JSON Objects {} map to Python Dictionaries {}.
             JSON Arrays [] map to Python Lists [].
             JSON basic types (string, number, boolean, null) map to Python types.
         Using the json module:
             json.dump(data, file_object): Writes Python data to a JSON file.
             json.load(file_object): Reads JSON data from a file into Python.
         Saving and loading complex data structures (lists of dictionaries, etc.).
     Skills Checklist:
         [ ] I can explain what JSON is and why it's used.
         [ ] I can relate JSON objects and arrays to Python dictionaries and lists.
         [ ] I can use json.dump() to save Python data to a JSON file.
         [ ] I can use json.load() to load JSON data from a file into a Python object.
         [ ] I can save and load lists of dictionaries using JSON.
Unit 9: Testing Your Code and Introduction to Data Analysis
Unit Goal: To enable students to write unit tests for their code and explore basic text-based data analysis concepts.
Lesson 9.1: Testing a Function
Student Materials:
     Outline:
         The importance of testing: ensuring code works as expected, catching bugs early.
         Introduction to unit testing: testing individual functions or small code units.
         The unittest module: Python's built-in testing framework.
         Basic structure of a test class inheriting from unittest.TestCase.
         Test methods starting with test_.
         Assertion methods: self.assertEqual(a, b), self.assertTrue(condition), self.assertFalse(condition).
         Running tests from the terminal (python -m unittest my_tests.py).
     Skills Checklist:
         [ ] I can explain why testing is important in programming.
         [ ] I can create a basic test class using unittest.TestCase.
         [ ] I can define test methods within a test class.
         [ ] I can use self.assertEqual() to check for expected results.
         [ ] I can use self.assertTrue() and self.assertFalse() for boolean conditions.
         [ ] I can run unit tests from the terminal.
Lesson 9.2: Testing a Class
Student Materials:
     Outline:
         Applying unit testing principles to classes.
         Creating an instance of the class within a test method.
         Testing class attributes and methods using assertions.
         The setUp() method: runs before each test method to set up test fixtures.
     Skills Checklist:
         [ ] I can write tests for a Python class.
         [ ] I can create an object of the class being tested within a test method.
         [ ] I can test the attributes and methods of an object.
         [ ] I can use the setUp() method to prepare my tests.
Lesson 9.3: Introduction to Random Numbers
Student Materials:
     Outline:
         The concept of randomness in computing (pseudo-randomness).
         The random module: import random.
         Generating random integers: random.randint(a, b) (inclusive).
         Generating random floats: random.random() (0.0 to 1.0).
         Choosing random elements from a list: random.choice(list).
     Skills Checklist:
         [ ] I can import the random module.
         [ ] I can generate a random integer within a specified range.
         [ ] I can generate a random floating-point number.
         [ ] I can select a random item from a list.
Lesson 9.4: Analyzing Text Data
Student Materials:
     Outline:
         Basic text analysis goals: counting words, characters, specific phrases.
         Reading text from files (revisiting file I/O).
         Splitting text into words (.split()).
         Counting word occurrences using dictionaries.
         Basic string cleaning (e.g., removing punctuation).
         Printing frequencies or summaries.
     Skills Checklist:
         [ ] I can read text content from a file.
         [ ] I can split a string of text into individual words.
         [ ] I can use a dictionary to count the frequency of words or characters.
         [ ] I can perform basic cleaning on text data (e.g., removing punctuation).
Lesson 9.5: Working with CSV Data (Text-based)
Student Materials:
     Outline:
         Introduction to CSV (Comma Separated Values) as a common tabular data format.
         Understanding that each line is a record, and values are separated by commas.
         Reading CSV files line by line using basic file I/O.
         Manually splitting lines by comma (.split(',')).
         Accessing specific "columns" (parts of the split line).
         Performing simple calculations or filtering on CSV data.
         (Optional, if time permits) Introduction to the csv module for more robust parsing.
     Skills Checklist:
         [ ] I can explain what CSV data is.
         [ ] I can read a CSV file line by line.
         [ ] I can split a line of CSV data into individual values.
         [ ] I can access specific values from a CSV record based on their position.
         [ ] I can perform basic analysis (e.g., sum, count) on numeric data from a CSV file.
Unit 10: Project-Based Learning: Building Text-Based Applications
Unit Goal: To integrate learned concepts by building a larger, interactive text-based application.
Lesson 10.1: Designing Your Project
Student Materials:
     Outline:
         The importance of project planning before coding.
         Breaking down a large problem into smaller, manageable sub-problems (modules, functions, classes).
         Defining project features and user interactions.
         Planning data structures (which lists, dictionaries, or classes will be needed).
         Designing the overall program flow.
         Thinking about accessible input/output design for screen readers.
     Skills Checklist:
         [ ] I can break down a larger problem into smaller, manageable parts.
         [ ] I can identify the key features required for a project.
         [ ] I can plan which data structures will be most suitable for my project's data.
         [ ] I can outline the main steps or flow of my program.
         [ ] I can consider user interaction and feedback during the design phase.
Lesson 10.2: Building a Text-Based Adventure Game (Part 1)
Student Materials:
     Outline:
         Representing game "rooms" using classes or dictionaries (e.g., description, exits).
         Implementing player movement between rooms (e.g., "north", "south").
         Managing the player's current location.
         Basic command parsing from user input.
         Displaying room descriptions clearly to the user.
     Skills Checklist:
         [ ] I can design a way to represent different locations in a text-based game.
         [ ] I can implement player movement based on user commands.
         [ ] I can update and track the player's current location.
         [ ] I can parse simple commands from user input.
         [ ] I can clearly describe the player's surroundings to them.
Lesson 10.3: Building a Text-Based Adventure Game (Part 2)
Student Materials:
     Outline:
         Adding items to rooms and player inventory.
         Implementing "take" and "drop" commands.
         Creating simple puzzles (e.g., needing a key for a door).
         Tracking game state (e.g., if a door is open, if an item has been used).
         Implementing win/lose conditions.
     Skills Checklist:
         [ ] I can add items to locations and manage a player's inventory.
         [ ] I can implement commands for picking up and dropping items.
         [ ] I can design and implement a simple puzzle in the game.
         [ ] I can manage and update the game's overall state.
         [ ] I can define and implement win or lose conditions for the game.
Lesson 10.4: Developing a Command-Line Tool
Student Materials:
     Outline:
         Choosing a simple, useful utility to build (e.g., a simple to-do list manager, a contact book).
         Designing the main menu and options for the tool.
         Using loops to keep the tool running until the user quits.
         Implementing functions for each major operation (add, view, edit, delete).
         Saving and loading data to/from a file (JSON or plain text) for persistence.
     Skills Checklist:
         [ ] I can choose and define the scope of a simple command-line utility.
         [ ] I can design an interactive menu system for a tool.
         [ ] I can use a while loop to maintain continuous user interaction.
         [ ] I can break down the tool's functionality into separate functions.
         [ ] I can implement file I/O to save and load data for my tool.
Lesson 10.5: Refinement and User Experience
Student Materials:
     Outline:
         Importance of clear prompts and feedback for screen reader users.
         Consistent formatting of output.
         Handling invalid input gracefully (revisiting exceptions).
         Providing helpful error messages.
         Adding "help" commands or instructions.
         Testing the application thoroughly with a screen reader.
     Skills Checklist:
         [ ] I can ensure my program's prompts are clear and unambiguous for screen reader users.
         [ ] I can provide consistent and descriptive feedback to the user after actions.
         [ ] I can handle common invalid inputs using try-except blocks.
         [ ] I can provide informative error messages.
         [ ] I can add help or instructions to my text-based application.
         [ ] I can test my application using a screen reader to identify accessibility issues.
Unit 11: Capstone Project - Accessible Personal Data Manager
Unit Goal: To integrate all learned concepts to develop a fully functional, screen-reader-accessible graphical application.
Lesson 11.1: Introduction to NiceGUI and Project Overview
Student Materials:
     Outline:
         Introduction to GUI (Graphical User Interface) concepts: event-driven programming.
         Overview of NiceGUI as the chosen framework and its advantages for accessibility.
         Walkthrough of the provided app_skeleton.py: understanding basic ui.button, ui.input, ui.label, ui.column, ui.row, and ui.tabs.
         How NiceGUI elements often map to accessible HTML elements.
         The purpose of aria_label and other accessibility attributes in the skeleton.
         Demonstration of navigating the skeleton GUI with a screen reader.
         Review of the project requirements: Add, View, Edit, Delete, Save/Load.
     Skills Checklist:
         [ ] I can run the provided NiceGUI skeleton application.
         [ ] I can navigate the skeleton GUI using my screen reader.
         [ ] I understand the purpose of the basic NiceGUI elements in the skeleton.
         [ ] I can explain what event-driven programming means in a GUI context.
         [ ] I understand the core functional requirements for the Capstone project.
Lesson 11.2: Data Model and Storage
Student Materials:
     Outline:
         Designing the Python class (e.g., Contact, Book, Task) to represent a single item of data for the manager.
         Defining the attributes for this class (name, phone, email, etc.).
         Review of how to manage a collection of these items in Python (a list of objects or dictionaries).
         Implementing the load_data() function to read JSON data from data.json into the all_items list.
         Implementing the save_data() function to write the all_items list to data.json.
         Consideration of error handling for file operations (empty file, corrupted JSON).
     Skills Checklist:
         [ ] I can design a Python class or dictionary structure to represent a single data item for my manager.
         [ ] I can create a list to hold all instances of my data items.
         [ ] I can implement a function to load data from a data.json file.
         [ ] I can implement a function to save the current data to a data.json file.
         [ ] I can handle basic json.JSONDecodeError and FileNotFoundError during data loading/saving.
Lesson 11.3: Implementing "Add Item" Functionality
Student Materials:
     Outline:
         Connecting the ui.input elements from the GUI to Python variables (accessing .value).
         Implementing the on_click handler for the "Add Item" button.
         Logic:
             Retrieve values from input fields.
             Perform basic input validation (e.g., required fields).
             Create a new instance of your data item class/dictionary.
             Add the new item to the all_items list.
             Clear the input fields for the next entry.
             Provide accessible feedback using ui.notify().
             Call update_item_display() to refresh the visible list.
     Skills Checklist:
         [ ] I can retrieve values from ui.input fields.
         [ ] I can connect a button's on_click event to a Python function.
         [ ] I can implement logic to create a new data item from GUI inputs.
         [ ] I can add the new item to the application's data list.
         [ ] I can clear the input fields after an item is added.
         [ ] I can use ui.notify() to provide accessible success/error messages.
         [ ] I can trigger the update_item_display() function to refresh the GUI.
Lesson 11.4: Displaying and Managing Items
Student Materials:
     Outline:
         Implementing the update_item_display() function:
             Clearing the existing display (items_display_column.clear()).
             Looping through the all_items list.
             For each item, dynamically creating ui.label or ui.card elements to display its attributes clearly.
             Populating the ui.select dropdown with options (e.g., item names) for selection.
             Ensuring the displayed information is easy for a screen reader to interpret (e.g., clear labels, grouping related info).
     Skills Checklist:
         [ ] I can dynamically update the GUI to display all items from the all_items list.
         [ ] I can clear existing GUI elements before re-rendering the list.
         [ ] I can display each item's details in a clear and structured way.
         [ ] I can populate the ui.select dropdown with the titles/names of existing items.
         [ ] I can ensure the displayed information is accessible and descriptive for a screen reader.
Lesson 11.5: Implementing "Edit" and "Delete" Functionality
Student Materials:
     Outline:
         Implementing edit_selected_item_logic():
             Finding the selected item in all_items based on the dropdown's value.
             Populating the "Edit Selected Item" input fields with the chosen item's data.
         Implementing update_item_logic() for the "Update Item" button:
             Finding the selected item.
             Updating its attributes with new values from the edit input fields.
             Calling update_item_display() and providing feedback.
         Implementing delete_selected_item_logic() for the "Delete Item" button:
             Finding and removing the selected item from all_items.
             Calling update_item_display() and providing feedback.
     Skills Checklist:
         [ ] I can retrieve the currently selected item from the ui.select dropdown.
         [ ] I can find a specific item in the all_items list based on its unique identifier.
         [ ] I can pre-populate input fields with data from a selected item for editing.
         [ ] I can update an item's attributes based on new input values.
         [ ] I can remove a selected item from the all_items list.
         [ ] I can ensure all edit and delete actions refresh the display and provide accessible notifications. 
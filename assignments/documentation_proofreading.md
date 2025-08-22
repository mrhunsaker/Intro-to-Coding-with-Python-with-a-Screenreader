
Unit 1: Foundations of Computing and Getting Started with Python
## Lesson 1.1: Welcome to Computer Science
Proofreading Assignment (No code to proofread in this conceptual lesson).
## Lesson 1.2: Your First Python Program: "Hello World!"
Proofreading Assignment:
     Scenario: You typed out your "Hello World!" program but made a few common mistakes. Your screen reader might point out "unexpected character" or "unmatched parenthesis" errors.
     Code to Proofread:print("Hello World"print "My name is Python")print("Nice to meet you!"
     Errors to Find:
         Missing closing parenthesis on the first print() call.
         print used as a statement instead of a function on the second line (missing parentheses).
         Missing closing parenthesis on the third print() call.
     Goal: Fix all syntax errors so the program runs and prints three lines of output.
## Lesson 1.3: Variables and Simple Data Types
Proofreading Assignment:
     Scenario: You were trying to store some information and perform a simple calculation, but there are typos. Listen carefully for error messages related to names not being defined or syntax errors.
     Code to Proofread:greeting = "Hi there"name = "Alex"print(greeting + name)num1 = 5num2 = 2.5result = num1 * num2print("Result is: " + result) # Type error heremy_variable = "This is a string"print(my_variable2nd_number = 10 # Invalid variable name
     Errors to Find:
         Type error when concatenating a string with a number (result).
         Missing closing parenthesis on the last print() call.
         Invalid variable name (2nd_number).
     Goal: Correct all errors so the program runs without crashing and prints the concatenation and the correct result.
Unit 2: Writing Simple Programs and Numeric Computations
## Lesson 2.1: The Software Development Process
Proofreading Assignment (No code to proofread in this conceptual lesson).
## Lesson 2.2: Elements of Programs: Expressions and Assignment
Proofreading Assignment:
     Scenario: You're trying to perform some calculations and store results, but Python is complaining about syntax or undefined variables.
     Code to Proofread:x = 10y = x + 5print(y)# Calculation errortotal = x + y * 2print(Total) # NameError due to capitalization# Assignment mistakeanother_value + 7 = 15 # Assignment target errorcurrent_score = 50current_score += 10 # This line is correctprint(current_score)
     Errors to Find:
         NameError: Total should be total.
         SyntaxError: Assignment target error (another_value + 7 = 15).
     Goal: Fix the NameError and SyntaxError so the program runs without crashing.
## Lesson 2.3: Input and Output Revisited
Proofreading Assignment:
     Scenario: You're building a small program to greet the user, but something's off with the input or output formatting.
     Code to Proofread:name = input("Enter your name: ")age = input("Enter your age") # Missing colon/spaceprint("Hello, " name) # SyntaxError: missing + or commaprint(f"You are " + age + " years old.")print(f"Next year you will be {age + 1} years old.") # This will be a TypeError if age isn't converted
     Errors to Find:
         A stylistic/clarity error: age = input("Enter your age") should have a colon and space for better readability.
         SyntaxError: print("Hello, " name) needs a + or a comma.
         TypeError: age + 1 will fail because age is a string.
     Goal: Correct all errors to ensure the program runs, accepts input, and prints correctly formatted messages.
Documentation Assignment:
     Scenario: The following code works, but it's not clear what each part does or what the overall purpose is.
     Code to Document:user_name = input("What is your name? ")user_city = input("Which city are you from? ")print(f"Hello, {user_name} from {user_city}!")
     Task: Add a docstring for the entire script (at the very top) describing its purpose. Add inline comments explaining what each input() line does and what the print() statement achieves.
     Goal: Make the code understandable to someone reading it for the first time.
## Lesson 2.4: Computing with Numbers and Type Conversions
Proofreading Assignment:
     Scenario: You're trying to create a simple calculator, but type issues and operator precedence are causing incorrect results or crashes.
     Code to Proofread:num_str1 = input("Enter first number: ")num_str2 = input("Enter second number: ")sum_result = num_str1 + num_str2 # String concatenation instead of additionprint(f"Sum: {sum_result}")product_result = int(num_str1) * float(num_str2)print(f"Product: {product_result}")incorrect_avg = (num_str1 + num_str2) / 2 # TypeError and logical errorprint(f"Incorrect Average: {incorrect_avg}")final_val = 10 + 5 * 2 # Order of operationsprint(f"Final value: {final_val}")
     Errors to Find:
         Logical Error: sum_result performs string concatenation.
         TypeError and Logical Error: incorrect_avg tries to add strings then divide.
     Goal: Fix the logical errors so sum_result and incorrect_avg perform correct numeric calculations.
Documentation Assignment:
     Scenario: This code converts temperatures, but it's not well-explained.
     Code to Document:celsius_str = input("Enter temperature in Celsius: ")celsius_float = float(celsius_str)fahrenheit = (celsius_float * 9/5) + 32print(f"{celsius_float}°C is {fahrenheit}°F")
     Task: Add a docstring to explain the script's overall function. Add inline comments explaining each step: input, conversion, calculation, and output.
     Goal: Clearly document the temperature conversion process.
## Lesson 2.5: Using the Math Library
Proofreading Assignment:
     Scenario: You're using the math module, but you're making mistakes with importing, function calls, or arguments.
     Code to Proofread:import mathvalue = 64sqrt_val = math.squareroot(value) # Typo in function nameprint(f"Square root: {sqrt_val}")power_val = math.pow(3, 2)print(f"3 to the power of 2: {power_val}")pi_val = math.PI # Incorrect casing for constantprint(f"Value of PI: {pi_val}")# Rounding examplenum_to_round = 7.6rounded_down = math.floor(num_to_round)print(f"Rounded down: {rounded_down}")result_ceil = math.ceil("4.2") # TypeError: argument must be a real numberprint(f"Ceiling: {result_ceil}")
     Errors to Find:
         AttributeError: math.squareroot (should be sqrt).
         AttributeError: math.PI (should be math.pi).
         TypeError: math.ceil() called with a string.
     Goal: Fix all errors so the program runs and performs the intended mathematical operations.
Documentation Assignment:
     Scenario: The following code calculates the hypotenuse of a right triangle.
     Code to Document:import mathside_a = 3side_b = 4hypotenuse = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))print(f"The hypotenuse is: {hypotenuse}")
     Task: Add a docstring explaining the script's purpose (using Pythagorean theorem). Add inline comments for the import, variable definitions, and the hypotenuse calculation line.
     Goal: Clearly document the calculation of the hypotenuse.
Unit 3: Control Flow: Decisions and Loops
## Lesson 3.1: Boolean Expressions and if Statements
Proofreading Assignment:
     Scenario: You're writing a conditional statement, but indentation and comparison operators are causing issues. Listen for "indentation error" messages.
     Code to Proofread:age = 17if age >= 18:print("You are an adult.") # Incorrect indentationelse: print("You are a minor.")score = 85if score = 85: # Assignment instead of comparison print("Score is exactly 85.")name = "Bob"if name != "Alice" print("Not Alice.") # SyntaxError: missing colon
     Errors to Find:
         IndentationError: First print is incorrectly indented.
         SyntaxError (or NameError depending on context): if score = 85 should be ==.
         SyntaxError: if name != "Alice" is missing a colon.
     Goal: Fix all errors so the program runs and the conditional logic works as intended.
Documentation Assignment:
     Scenario: This code checks if a number is positive.
     Code to Document:number = -5if number > 0: print("The number is positive.")else: print("The number is not positive.")
     Task: Add a docstring explaining the script's purpose. Add inline comments for the if and else blocks, explaining their conditions and actions.
     Goal: Document the conditional check for a positive number.
## Lesson 3.2: Chained Conditionals (elif, else)
Proofreading Assignment:
     Scenario: You're building a grading system, but the chained conditionals are messy due to indentation or logical errors.
     Code to Proofread:grade = 75if grade >= 90: print("Grade: A")elif grade >= 80:print("Grade: B") # Incorrect indentationelif grade >= 70: print("Grade: C")else: print("Grade: F")temp = 25is_raining = Trueif temp > 20 and is_raining = True: # Assignment instead of comparison for is_raining print("Warm and rainy.")elif temp < 10 or not is_raining: print("Cold or not raining.")
     Errors to Find:
         IndentationError: print("Grade: B") is incorrectly indented.
         SyntaxError (or NameError): is_raining = True in the if condition should be ==.
     Goal: Correct all errors, including the indentation and comparison operator, to ensure correct grading and weather condition checks.
Documentation Assignment:
     Scenario: This code checks the time of day and prints a greeting.
     Code to Document:hour = 14 # 2 PMif hour < 12: print("Good morning!")elif hour < 18: print("Good afternoon!")else: print("Good evening!")
     Task: Add a docstring for the script. Add inline comments explaining the conditions for "Good morning," "Good afternoon," and "Good evening."
     Goal: Document the time-based greeting logic.
## Lesson 3.3: Introduction to Lists
Proofreading Assignment:
     Scenario: You're creating and accessing lists, but common mistakes with brackets and indexing are causing issues.
     Code to Proofread:fruits = ["apple", "banana", "cherry" # Missing closing bracketnumbers = [1, 2, 3, 4]first_fruit = fruits[0]print(first_fruit)second_number = numbers[2] # Accessing the third elementprint(second_number)last_fruit = fruits[len(fruits)] # IndexError: out of boundsprint(last_fruit)fruits[1] = "grape"print(fruits)
     Errors to Find:
         SyntaxError: fruits list is missing a closing bracket.
         IndexError: fruits[len(fruits)] attempts to access an index out of bounds.
     Goal: Fix the syntax error and the IndexError so the program runs and list operations are correct.
Documentation Assignment:
     Scenario: This code defines a list of colors and prints the second color.
     Code to Document:colors = ["red", "green", "blue", "yellow"]print(colors[1])
     Task: Add a docstring explaining the list's purpose. Add an inline comment next to the print() statement explaining what colors[1] accesses.
     Goal: Document list creation and element access.
## Lesson 3.4: Iterating with for Loops
Proofreading Assignment:
     Scenario: Your for loops aren't iterating correctly due to indentation, missing colons, or incorrect range() usage.
     Code to Proofread:items = ["pen", "notebook", "eraser"]for item in items # Missing colon print(item) # Incorrect indentation# Loop with rangefor i in range(5) # Missing colonprint(i) # Incorrect indentation# Loop with incorrect rangefor j in range(1, 1): # This loop won't run print(f"J is {j}")# Correct loop (for comparison)for k in range(3): print(f"K is {k}")
     Errors to Find:
         SyntaxError: Missing colons after for statements.
         IndentationError: Code blocks under for are incorrectly indented.
         Logical Error: range(1, 1) results in an empty sequence.
     Goal: Fix all errors so both loops run correctly and the indentation is proper.
Documentation Assignment:
     Scenario: This code prints numbers from 0 to 4 using a for loop.
     Code to Document:for number in range(5): print(number)
     Task: Add a docstring for the script. Add an inline comment explaining what range(5) does and what the loop iterates over.
     Goal: Document a basic for loop with range().
## Lesson 3.5: Basic String Operations
Proofreading Assignment:
     Scenario: You're working with strings, but method calls, assignments, or concatenation are causing problems.
     Code to Proofread:message = " Hello Python! "clean_message = message.strip # Missing parentheses for method callprint(clean_message)long_text = "This is a long sentence."upper_text = long_text.toupper() # Typo in method nameprint(upper_text)name = "Alice"age = 30greeting = "My name is " + name + " and I am " + str(age) + " years old."print(greeting)# Replacement errorsentence = "I like apples, do you like apples?"new_sentence = sentence.replace("apple", "banana") # Correctprint(new_sentence)bad_replace = sentence.replace("oranges", "grapes") # No error, but doesn't do anythingprint(bad_replace)len_of_msg = len[message] # TypeError: len() expects an iterable, not a list of one itemprint(len_of_msg)
     Errors to Find:
         TypeError or AttributeError: message.strip needs ().
         AttributeError: long_text.toupper() should be long_text.upper().
         TypeError: len[message] should be len(message).
     Goal: Fix all errors so string operations work as intended.
Documentation Assignment:
     Scenario: This code cleans and capitalizes a user's input.
     Code to Document:user_input = input("Enter a phrase: ")cleaned_input = user_input.strip().upper()print(f"Cleaned and capitalized: {cleaned_input}")
     Task: Add a docstring explaining the script's purpose. Add inline comments explaining the steps of getting input, stripping whitespace, and converting to uppercase.
     Goal: Document string cleaning and transformation.
Unit 4: Data Structures: Lists and Dictionaries
## Lesson 4.1: More on Lists
Proofreading Assignment:
     Scenario: You're trying to modify a list, but you're making mistakes with methods or indexing.
     Code to Proofread:my_list = [10, 20, 30, 40, 50]my_list.add(60) # Incorrect method for adding to endprint(my_list)my_list.insert(1, "hello") # Correctprint(my_list)del my_list[len(my_list)] # IndexError: deleting out of boundsprint(my_list)removed_item = my_list.pop() # Correctprint(f"Removed: {removed_item}, List: {my_list}")my_list.remove(20) # Correctprint(my_list)my_list.remove(99) # ValueError: not in listprint(my_list)
     Errors to Find:
         AttributeError: my_list.add() (should be append()).
         IndexError: del my_list[len(my_list)] tries to delete beyond the list's bounds.
         ValueError: my_list.remove(99) if 99 is not in the list.
     Goal: Fix the AttributeError and IndexError. Handle the potential ValueError with a try-except block, printing a message if the item isn't found.
Documentation Assignment:
     Scenario: This code demonstrates several ways to modify a list.
     Code to Document:shopping_list = ["milk", "bread"]shopping_list.append("eggs")shopping_list.insert(0, "cheese")del shopping_list[1]print(shopping_list)
     Task: Add a docstring explaining the list modifications. Add inline comments for append(), insert(), and del to explain what each line does.
     Goal: Document common list modification methods.
## Lesson 4.2: Organizing Lists
Proofreading Assignment:
     Scenario: You're trying to sort and reverse lists, but misusing methods or forgetting argument names.
     Code to Proofread:names = ["Charlie", "Bob", "Alice"]names.sort(True) # TypeError: sort() takes no positional argumentsprint(names)numbers = [5, 1, 8, 2]sorted_numbers = sorted(numbers) # Correctprint(sorted_numbers)original_numbers = [9, 3, 7]original_numbers.reverse # Missing parentheses for method callprint(original_numbers)length_of_list = len[numbers] # TypeError: len() takes a single argumentprint(length_of_list)
     Errors to Find:
         TypeError: names.sort(True) (should be reverse=True).
         TypeError or AttributeError: original_numbers.reverse needs ().
         TypeError: len[numbers] should be len(numbers).
     Goal: Fix all errors so the list sorting and reversing operations work correctly.
Documentation Assignment:
     Scenario: This code sorts a list of scores and prints it in both ascending and descending order.
     Code to Document:scores = [95, 80, 75, 90]scores.sort()print("Ascending:", scores)scores.sort(reverse=True)print("Descending:", scores)
     Task: Add a docstring explaining the sorting operations. Add inline comments explaining what each sort() call does.
     Goal: Document in-place list sorting.
## Lesson 4.3: Tuples: Immutable Lists
Proofreading Assignment:
     Scenario: You're using tuples, but trying to modify them or using incorrect syntax.
     Code to Proofread:coordinates = (10, 20, 30] # SyntaxError: mixed parentheses and bracketsprint(coordinates)first_coord = coordinates[0]print(first_coord)coordinates[1] = 25 # TypeError: tuples are immutableprint(coordinates)# Looping through a tuplefor coord in coordinates: print(coord)
     Errors to Find:
         SyntaxError: coordinates definition uses mixed brackets.
         TypeError: coordinates[1] = 25 attempts to modify an immutable tuple.
     Goal: Fix the SyntaxError and explain why the TypeError occurs, then comment out the line causing the TypeError.
Documentation Assignment:
     Scenario: This code defines a tuple of weekdays and prints them.
     Code to Document:weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")for day in weekdays: print(day)
     Task: Add a docstring explaining what a tuple is and its purpose in this code. Add an inline comment for the for loop explaining its function.
     Goal: Document tuple creation and iteration.
## Lesson 4.4: Introducing Dictionaries
Proofreading Assignment:
     Scenario: You're working with dictionaries, but making mistakes with curly braces, keys, or access.
     Code to Proofread:person = {"name": "Alice", "age": 25 # Missing closing curly braceprint(person)person["city"] = "New York" # Adding a new key-value pairprint(person)print(person[Name]) # NameError: string literal needed for keydel person["age"] # Correctprint(person)person["age"] = "twenty-five" # Correct, but perhaps unintended typeprint(person)
     Errors to Find:
         SyntaxError: person dictionary is missing a closing curly brace.
         NameError: person[Name] should use a string literal "name".
     Goal: Fix the syntax error and the NameError so dictionary operations are correct.
Documentation Assignment:
     Scenario: This code defines a dictionary for a student's profile and prints some of its details.
     Code to Document:student_profile = { "id": 101, "name": "Jane Doe", "major": "Computer Science", "gpa": 3.8}print(f"Student Name: {student_profile['name']}")student_profile["gpa"] = 3.9print(f"Updated GPA: {student_profile['gpa']}")
     Task: Add a docstring explaining what a dictionary is and its use here. Add inline comments explaining how to access data, and how to update a value.
     Goal: Document dictionary creation, access, and modification.
## Lesson 4.5: Looping Through Dictionaries
Proofreading Assignment:
     Scenario: You're trying to loop through dictionary keys, values, or items, but common errors are occurring.
     Code to Proofread:inventory = {"apple": 10, "banana": 5, "orange": 8}for item in inventory: # Loops through keys print(item)for count in inventory.value(): # Typo in method name print(count)for k, v in inventory.items # Missing parentheses for method call print(f"{k}: {v}")# Intentional logical error (no error, just doesn't do what's expected)for key in inventory.values(): print(key) # This will print values, not keys
     Errors to Find:
         AttributeError: inventory.value() should be inventory.values().
         TypeError or AttributeError: inventory.items needs ().
     Goal: Fix the AttributeError and TypeError. Discuss the logical error for extra credit.
Documentation Assignment:
     Scenario: This code iterates through a dictionary of product prices.
     Code to Document:product_prices = { "laptop": 1200, "mouse": 25, "keyboard": 75}for product, price in product_prices.items(): print(f"The {product} costs ${price}.")
     Task: Add a docstring for the script. Add inline comments explaining the use of .items() and how product and price variables are assigned in the loop.
     Goal: Document iterating through dictionary items.
Unit 5: User Input and while Loops
## Lesson 5.1: How the input() Function Works
Proofreading Assignment:
     Scenario: You're taking user input, but not handling types correctly, leading to crashes.
     Code to Proofread:name = input("Enter your name ") # Missing colon/space for prompt styleprint(f"Hello, {name}!")age_str = input("Enter your age: ")next_year_age = age_str + 1 # TypeError: can't add int to strprint(f"Next year you will be {next_year_age} years old.")# Another input scenariofav_num = int(input("What is your favorite number?")) # No space after promptprint(f"Your favorite number is {fav_num}.")
     Errors to Find:
         Stylistic: Missing colon/space in first input() prompt.
         TypeError: age_str + 1 needs age_str converted to int.
         Stylistic: Missing space in third input() prompt.
     Goal: Fix the TypeError and improve the stylistic prompts for better user experience.
Documentation Assignment:
     Scenario: This code asks the user for two numbers and prints their sum.
     Code to Document:num1_str = input("Enter the first number: ")num2_str = input("Enter the second number: ")num1 = int(num1_str)num2 = int(num2_str)total = num1 + num2print(f"The sum is: {total}")
     Task: Add a docstring for the script. Add inline comments explaining the purpose of each input() call, the type conversions, and the calculation.
     Goal: Document the process of taking numeric input from the user.
## Lesson 5.2: The while Loop in Action
Proofreading Assignment:
     Scenario: Your while loop isn't behaving as expected, either running infinitely or not at all, due to condition errors or forgotten updates.
     Code to Proofread:count = 0while count < 3 # Missing colon print(f"Count is {count}") # Missing increment, will be infinite loopnum = 5while num > 0: print(f"Num is {num}") num = num - 1 # Correctprint("Loop finished.")# Another loop examplescore = 10while score > 10: # This loop will never run print("Score is too high.") score -= 1
     Errors to Find:
         SyntaxError: Missing colon after while condition.
         Logical Error: The first while loop is missing an increment and will be infinite.
         Logical Error: The third while loop's condition is score > 10, but score starts at 10, so it never runs.
     Goal: Fix the SyntaxError and the logical errors so both while loops run as intended (one for 3 iterations, one for 0 iterations).
Documentation Assignment:
     Scenario: This code counts down from 5 and prints "Blastoff!".
     Code to Document:countdown = 5while countdown > 0: print(countdown) countdown -= 1print("Blastoff!")
     Task: Add a docstring for the script. Add inline comments explaining the loop's condition, the print() statement, and the decrement.
     Goal: Document a basic countdown while loop.
## Lesson 5.3: Using Flags and break to Exit Loops
Proofreading Assignment:
     Scenario: You're trying to control a loop with a flag or break, but syntax errors or logical mistakes are preventing it from working.
     Code to Proofread:active = Truewhile active: command = input("Enter command (quit to exit): ") if command == "quit" active = False # Missing colon for if statement print(f"You entered: {command}")# Another break examplewhile True: secret_word = input("Guess the secret word: ") if secret_word == "python": break # Correct else: print("Incorrect guess, try again!") print("This line should not be reached after correct guess if break works.") # Logical errorprint("You guessed correctly!")
     Errors to Find:
         SyntaxError: Missing colon after if command == "quit".
         Logical Error: The print("This line should not be reached...") will be printed before the loop breaks.
     Goal: Fix the SyntaxError. Explain why the logical error occurs and how break behaves (it exits immediately, so the print after else won't run).
Documentation Assignment:
     Scenario: This code keeps asking for input until the user types "stop".
     Code to Document:while True: user_input = input("Say something (or 'stop' to quit): ") if user_input.lower() == 'stop': break print(f"You said: {user_input}")print("Program ended.")
     Task: Add a docstring for the script. Add inline comments explaining the while True loop, the if condition, and the break statement.
     Goal: Document a while True loop with a break condition.
## Lesson 5.4: Using continue in Loops
Proofreading Assignment:
     Scenario: You're using continue to skip certain iterations, but it's not quite working due to syntax or logical placement.
     Code to Proofread:numbers = [1, 2, 3, 4, 5, 6]for num in numbers: if num % 2 != 0 # Missing colon continue print(f"{num} is an even number.")# Another continue examplei = 0while i < 5: i += 1 if i == 3: continue print(f"Current value: {i}") # This prints 3
     Errors to Find:
         SyntaxError: Missing colon after if num % 2 != 0.
         Logical Error: In the while loop, print(f"Current value: {i}") is inside the if block, so it will print 3 before continue is reached, or the print statement is indented too far. It should be after the if block, but not affected by continue. The print should be at the same indentation level as the if.
     Goal: Fix the SyntaxError. Correct the logical flow of the while loop so that 3 is skipped entirely from the print output.
Documentation Assignment:
     Scenario: This code processes numbers, skipping negatives.
     Code to Document:data = [10, -3, 5, -8, 20]for item in data: if item < 0: print("Skipping negative number.") continue print(f"Processing positive number: {item}")
     Task: Add a docstring for the script. Add inline comments explaining the if condition for skipping and the continue statement's effect.
     Goal: Document the use of continue in a loop.
## Lesson 5.5: Avoiding Infinite Loops
Proofreading Assignment:
     Scenario: You've written some while loops, but one or more are designed to be infinite. Your task is to identify which one and explain why.
     Code to Proofread:# Loop 1counter = 0while counter < 5: print(f"Counter: {counter}") # Missing increment here!# Loop 2user_input = ""while user_input != "exit": user_input = input("Type 'exit' to stop: ") if user_input == "quit": # User types 'quit', but the loop checks for 'exit' print("Did you mean 'exit'?") # Missing condition to break if user types 'exit'# Loop 3game_on = Truewhile game_on: player_hp = 100 if player_hp <= 0: game_on = False # This condition will never be met inside the loop print("Game running...")
     Errors to Find:
         Logical Error: Loop 1 is missing counter += 1, leading to an infinite loop.
         Logical Error: Loop 2's if condition doesn't end the loop; it just prints a message. The loop condition (user_input != "exit") does work, so it's not strictly infinite if "exit" is typed, but the quit logic is flawed. The real problem is if they type anything other than "exit", the loop continues indefinitely.
         Logical Error: Loop 3's player_hp is reset to 100 on each iteration, so player_hp <= 0 is never met, leading to an infinite loop.
     Goal: Identify the two truly infinite loops and explain why. Fix them by adding the necessary statements (counter += 1, break or user_input.lower() check, updating player_hp outside the loop or decrementing it).
Documentation Assignment:
     Scenario: This code simulates a program running indefinitely until stopped manually.
     Code to Document:# This loop will run forever until you stop it (e.g., Ctrl+C in terminal)while True: print("Program is running...") # Imagine complex operations here # For demonstration, we'll just delay a bit import time time.sleep(1) # Wait for 1 second
     Task: Add a docstring to clearly state this is an example of an infinite loop and how to stop it. Add an inline comment explaining while True.
     Goal: Document the concept and handling of an intentional infinite loop for demonstration.
Unit 6: Functions
## Lesson 6.1: Defining Functions
Proofreading Assignment:
     Scenario: You're defining functions, but misusing def, forgetting parameters, or having indentation issues.
     Code to Proofread:# Function 1def greet name: # SyntaxError: missing parentheses for parameters print(f"Hello, {name}!")# Function 2def say_hello():print("Hello there!") # Incorrect indentation# Function 3# This function won't be callablemy_function(): # SyntaxError: def keyword missing print("Inside my function.")greet("Alice")say_hello()my_function() # NameError: my_function not defined
     Errors to Find:
         SyntaxError: def greet name: needs (name):.
         IndentationError: print("Hello there!") is incorrectly indented.
         SyntaxError: my_function(): is missing def.
         NameError: Resulting from the previous syntax error.
     Goal: Fix all syntax and indentation errors so all functions are correctly defined and callable.
Documentation Assignment:
     Scenario: This code defines a simple greeting function.
     Code to Document:def display_greeting(person_name): """ Prints a personalized greeting. """ print(f"Greetings, {person_name}!")display_greeting("World")
     Task: Ensure the docstring for display_greeting is clear. Add an inline comment for the print statement and the function call.
     Goal: Document a basic function definition and call.
## Lesson 6.2: Passing Arguments
Proofreading Assignment:
     Scenario: You're calling functions, but passing arguments incorrectly (positional vs. keyword, too many/few).
     Code to Proofread:def describe_pet(animal_type, pet_name): print(f"I have a {animal_type}.") print(f"Its name is {pet_name}.")describe_pet("dog", "Buddy") # Correct positionaldescribe_pet(pet_name="Lucy", "cat") # SyntaxError: positional argument follows keyword argumentdescribe_pet("parrot") # TypeError: missing 1 required positional argumentdef make_shirt(size, message="I love Python"): print(f"Making a {size}-sized shirt with message: '{message}'")make_shirt("large", message="Hello") # Correct keywordmake_shirt(size="medium") # Correct keyword with defaultmake_shirt("small", "My custom message", "extra_arg") # TypeError: too many arguments
     Errors to Find:
         SyntaxError: describe_pet(pet_name="Lucy", "cat") has a positional argument after a keyword.
         TypeError: describe_pet("parrot") is missing an argument.
         TypeError: make_shirt(...) has too many arguments.
     Goal: Fix all TypeError and SyntaxError issues by providing the correct number and type of arguments or correcting the argument passing style.
Documentation Assignment:
     Scenario: This code calculates the area of a rectangle.
     Code to Document:def calculate_rectangle_area(length, width): """ Calculates the area of a rectangle. """ area = length * width return arearoom_area = calculate_rectangle_area(10, 5)print(f"The room area is: {room_area}")
     Task: Ensure the docstring is clear and explains parameters. Add inline comments explaining the calculation and the function call.
     Goal: Document a function with parameters and its usage.
## Lesson 6.3: Return Values
Proofreading Assignment:
     Scenario: You're trying to get values back from functions, but misusing return or expecting print() to return.
     Code to Proofread:def add_numbers(a, b): sum_val = a + b print(sum_val) # Prints, but doesn't returnresult1 = add_numbers(5, 3)print(f"Result of add_numbers: {result1}") # This will print Nonedef multiply_numbers(x, y): return x * yproduct = multiply_numbers(4, 2)print(f"Product: {product}") # Correctdef get_greeting(name): greeting_msg = f"Hello, {name}!" # Missing return statementfinal_greeting = get_greeting("Charlie")print(f"Final greeting: {final_greeting}") # This will print None
     Errors to Find:
         Logical Error: add_numbers prints but doesn't return, so result1 will be None.
         Logical Error: get_greeting is missing a return statement, so final_greeting will be None.
     Goal: Modify add_numbers and get_greeting to correctly return their calculated values, so the print statements show the intended output.
Documentation Assignment:
     Scenario: This code defines a function to capitalize a string and return it.
     Code to Document:def capitalize_string(text): """ Converts the given text to uppercase and returns it. """ return text.upper()my_text = "python programming"capitalized = capitalize_string(my_text)print(f"Original: {my_text}, Capitalized: {capitalized}")
     Task: Ensure the docstring for capitalize_string clearly explains what it returns. Add inline comments for the return statement and the function call.
     Goal: Document a function with a return value.
## Lesson 6.4: Functions with Lists and Dictionaries
Proofreading Assignment:
     Scenario: You're passing lists/dictionaries to functions, but unexpected modifications or incorrect copies are happening.
     Code to Proofread:def add_item_to_list(my_list_param, item): my_list_param.append(item)data_list = [1, 2, 3]add_item_to_list(data_list, 4) # This will modify data_listprint(f"Original list after func call: {data_list}") # This will be [1, 2, 3, 4]def process_dict(my_dict_param): my_dict_param["status"] = "processed" return my_dict_paramconfig = {"version": 1.0, "active": True}new_config = process_dict(config)print(f"Original config after func call: {config}") # This will also be modifiedprint(f"New config: {new_config}")def append_to_copy(original_list, value): new_list = original_list # This creates a reference, not a copy new_list.append(value) return new_listnumbers = [10, 20]modified_numbers = append_to_copy(numbers, 30)print(f"Original numbers after copy func: {numbers}") # This will be [10, 20, 30]
     Errors to Find:
         Logical Error: add_item_to_list directly modifies data_list (lists are mutable).
         Logical Error: process_dict directly modifies config (dictionaries are mutable).
         Logical Error: new_list = original_list creates a reference, not a copy.
     Goal: Explain the logical errors related to mutability. Modify append_to_copy to use original_list[:] to truly create a copy. Discuss how to explicitly copy lists/dictionaries if the original should remain unchanged.
Documentation Assignment:
     Scenario: This code defines a function that takes a list of numbers and returns a new list with each number doubled.
     Code to Document:def double_numbers_in_list(numbers_list): """ Doubles each number in the input list and returns a new list. """ doubled_list = [] for num in numbers_list: doubled_list.append(num * 2) return doubled_listmy_nums = [1, 2, 3]doubled_result = double_numbers_in_list(my_nums)print(f"Original: {my_nums}, Doubled: {doubled_result}")
     Task: Ensure the docstring for double_numbers_in_list is clear about input, output, and side effects. Add inline comments explaining the loop and appending to the new list.
     Goal: Document a function that processes a list and returns a new list.
## Lesson 6.5: Arbitrary Number of Arguments
Proofreading Assignment:
     Scenario: You're using *args and **kwargs, but misplacing them or forgetting the correct number of asterisks.
     Code to Proofread:def sum_all_numbers(*nums): total = 0 for num in nums: total += num return totalprint(sum_all_numbers(1, 2, 3, 4)) # Correctdef create_profile(name, **details): profile = {"name": name} for key, value in details.items(): profile[key] = value return profile# Error: positional argument after keyword argument when using **kwargs implicitlyuser_profile = create_profile("Bob", age=30, "city": "London") # SyntaxError# Error: forgetting the double asterisk for kwargsdef log_info(level, msg, args): # args will be treated as a single positional argument print(f"[{level}] {msg} - {args}")log_info("INFO", "User login", user="admin", id=123) # TypeError: log_info() got unexpected keyword argument 'user'
     Errors to Find:
         SyntaxError: create_profile call has a positional argument after a keyword argument within the **details part.
         TypeError: log_info function definition is missing ** for kwargs.
     Goal: Fix the SyntaxError by correcting the argument passing for create_profile. Fix the TypeError by adding ** to args in log_info's definition.
Documentation Assignment:
     Scenario: This code defines a function that can accept any number of ingredients and print them.
     Code to Document:def make_salad(*ingredients): """ Creates a salad from an arbitrary number of ingredients. """ print("Ingredients for your salad:") for ingredient in ingredients: print(f"- {ingredient}")make_salad("lettuce", "tomato", "cucumber", "dressing")make_salad("spinach", "feta")
     Task: Ensure the docstring for make_salad clearly explains the use of *ingredients. Add an inline comment explaining how *ingredients collects arguments.
     Goal: Document a function that uses *args.
Unit 7: Classes and Object-Oriented Programming
## Lesson 7.1: Why Learn About Classes?
Proofreading Assignment (No code to proofread in this conceptual lesson).
## Lesson 7.2: Creating and Using a Class
Proofreading Assignment:
     Scenario: You're defining a class and creating objects, but syntax errors or self issues are popping up.
     Code to Proofread:class Car: # Missing colon def __init__(self, make, model): self.make = make model = model # This 'model' is a local variable, not an attribute def display_info(self): print(f"Make: {self.make}, Model: {self.model}") # NameError: self.model not definedmy_car = Car("Toyota", "Camry")my_car.display_info()
     Errors to Find:
         SyntaxError: Missing colon after class Car.
         Logical Error: model = model in __init__ means self.model is never created.
         AttributeError (or NameError depending on Python version): self.model accessed in display_info but not defined.
     Goal: Fix the SyntaxError and the logical error in __init__ to correctly assign self.model.
Documentation Assignment:
     Scenario: This code defines a Dog class and creates a dog object.
     Code to Document:class Dog: """ Represents a dog with a name and age. """ def __init__(self, name, age): self.name = name self.age = age def bark(self): """ Makes the dog bark. """ print(f"{self.name} says Woof!")my_dog = Dog("Buddy", 3)my_dog.bark()
     Task: Ensure the docstring for the Dog class explains its purpose. Ensure the docstring for bark explains what it does. Add inline comments explaining attribute assignment in __init__ and the object creation/method call.
     Goal: Document a simple class with attributes and methods.
## Lesson 7.3: Working with Attributes and Methods
Proofreading Assignment:
     Scenario: You're trying to access or modify attributes and call methods, but often forget self. or confuse local variables.
     Code to Proofread:class Robot: def __init__(self, name): self.name = name self.power = 100 def decrease_power(amount): # Missing self parameter power -= amount # NameError: power not defined print(f"{self.name} power is now {self.power}") # AttributeError: self not defined def get_name(): # Missing self parameter return name # NameError: name not definedmy_robot = Robot("R2D2")print(my_robot.name)my_robot.decrease_power(10)print(my_robot.get_name())
     Errors to Find:
         TypeError: decrease_power and get_name are missing the self parameter.
         NameError: Inside decrease_power, power should be self.power.
         NameError: Inside get_name, name should be self.name.
     Goal: Fix all methods by adding self as the first parameter and using self.attribute when accessing attributes.
Documentation Assignment:
     Scenario: This code defines a Circle class with methods to calculate area and circumference.
     Code to Document:import mathclass Circle: """ Represents a circle and provides methods for calculations. """ def __init__(self, radius): self.radius = radius def calculate_area(self): """ Calculates the area of the circle. """ return math.pi * self.radius**2 def calculate_circumference(self): """ Calculates the circumference of the circle. """ return 2 * math.pi * self.radiusmy_circle = Circle(5)print(f"Area: {my_circle.calculate_area()}")
     Task: Ensure docstrings for Circle, calculate_area, and calculate_circumference are clear. Add inline comments explaining attribute assignment in __init__ and the calculation formulas.
     Goal: Document a class with mathematical methods.
## Lesson 7.4: Inheritance
Proofreading Assignment:
     Scenario: You're implementing inheritance, but common mistakes with super() or attribute access are causing issues.
     Code to Proofread:class Animal: def __init__(self, name): self.name = name def speak(self): return "Unknown sound"class Dog(Animal): def __init__(self, name, breed): super().__init__(name) self.breed = breed def speak(self): return "Woof!"class Cat(Animal): def __init__(self, name, color): self.name = name # Forgetting super().__init__() self.color = color def speak(self): return "Meow!"my_dog = Dog("Buddy", "Golden Retriever")print(my_dog.speak())my_cat = Cat("Whiskers", "black")print(my_cat.speak())print(my_cat.name) # This will work, but it's not ideal for inheritanceprint(my_dog.breed)
     Errors to Find:
         Logical Error/Best Practice: In Cat's __init__, self.name = name directly assigns rather than calling super().__init__(name). While this doesn't cause an error for name, it bypasses any other initialization Animal might have. It's a common oversight.
     Goal: Modify Cat's __init__ to correctly use super().__init__(name) for proper inheritance. Explain why super() is preferred.
Documentation Assignment:
     Scenario: This code defines a Vehicle class and a Car class that inherits from Vehicle.
     Code to Document:class Vehicle: """ A generic class to represent a vehicle. """ def __init__(self, brand): self.brand = brand def get_brand(self): """Returns the brand of the vehicle.""" return self.brandclass Car(Vehicle): """ Represents a car, inheriting from Vehicle. """ def __init__(self, brand, model): super().__init__(brand) # Initialize parent class self.model = model def get_model(self): """Returns the model of the car.""" return self.modelmy_car = Car("Toyota", "Camry")print(f"Brand: {my_car.get_brand()}, Model: {my_car.get_model()}")
     Task: Ensure docstrings are present for both classes and their methods. Add an inline comment explaining super().__init__() in the Car class.
     Goal: Document a basic inheritance setup.
## Lesson 7.5: Instances as Attributes
Proofreading Assignment:
     Scenario: You're using composition, but misremembering how to access attributes of the nested object.
     Code to Proofread:class Engine: def __init__(self, fuel_type): self.fuel_type = fuel_type def start(self): return f"Engine running on {self.fuel_type}."class Car: def __init__(self, make, model, engine_type): self.make = make self.model = model self.engine = Engine(engine_type) # Correct composition def get_engine_fuel(): # Missing self parameter return self.engine.fuel_type # AttributeError: self not defined def car_start_sound(self): return self.engine.start # Missing parentheses for method callmy_car = Car("Honda", "Civic", "Gasoline")print(f"Car engine fuel: {my_car.get_engine_fuel()}")print(f"Car starts: {my_car.car_start_sound()}")
     Errors to Find:
         TypeError: get_engine_fuel is missing self.
         AttributeError: If previous error fixed, self.engine.start is missing () for the method call.
     Goal: Fix the TypeError by adding self to get_engine_fuel. Fix the AttributeError by adding () to self.engine.start.
Documentation Assignment:
     Scenario: This code models a Book that has a Author.
     Code to Document:class Author: """ Represents an author with a name. """ def __init__(self, name): self.name = name def get_name(self): """Returns the author's name.""" return self.nameclass Book: """ Represents a book with a title and an Author instance. """ def __init__(self, title, author_name): self.title = title self.author = Author(author_name) # Composition: Book 'has a' Author def get_book_info(self): """Returns information about the book and its author.""" return f"'{self.title}' by {self.author.get_name()}"author1 = Author("Jane Austen")book1 = Book("Pride and Prejudice", author1.name)print(book1.get_book_info())
     Task: Ensure docstrings for both classes and their methods are clear. Add an inline comment explaining the composition in Book.__init__ and how self.author.get_name() accesses the nested object's method.
     Goal: Document a class demonstrating composition.
Unit 8: Files and Exceptions
## Lesson 8.1: Reading from a File
Proofreading Assignment:
     Scenario: You're trying to read from a file, but common errors like FileNotFoundError or incorrect method usage are occurring.
     Code to Proofread:# Assuming 'non_existent_file.txt' does not existwith open("non_existent_file.txt", "r") as file: # FileNotFoundError if not handled content = file.read() print(content)# Assuming 'my_data.txt' exists with "Line 1\nLine 2\n"with open("my_data.txt", "r") as f: lines = f.readline() # This only reads one line print(lines) all_lines = f.readall() # AttributeError: 'io.TextIOWrapper' object has no attribute 'readall' print(all_lines)# To prepare for proofreading, create a file named 'my_data.txt' with some content# Example content for my_data.txt:# Line 1# Line 2# Line 3
     Errors to Find:
         FileNotFoundError: For non_existent_file.txt.
         Logical Error: f.readline() only reads one line. The intention was likely to read all.
         AttributeError: f.readall() is not a valid method (should be f.read() or f.readlines()).
     Goal: Handle the FileNotFoundError with a try-except block. Correct the logical error to read all lines. Fix the AttributeError.
Documentation Assignment:
     Scenario: This code reads the entire content of a file named sample.txt.
     Code to Document:# Ensure 'sample.txt' exists in the same directory as this script# with some text content.with open("sample.txt", "r") as file: content = file.read() print(content)
     Task: Add a docstring for the script. Add inline comments explaining with open(), the "r" mode, and .read().
     Goal: Document reading an entire file.
## Lesson 8.2: Writing to a File
Proofreading Assignment:
     Scenario: You're writing to files, but using the wrong modes or forgetting newlines.
     Code to Proofread:# Writing a new filewith open("output.txt", "r") as file: # Wrong mode for writing file.write("Hello, world!")# Appending to a filewith open("log.txt", "w") as log_file: # Wrong mode, will overwrite log_file.write("First log entry.") log_file.write("Second log entry.") # Missing newline# This part should be correct if the first parts are fixed# Ensure 'new_output.txt' is readywith open("new_output.txt", "a") as f: f.write("Appended line.\n")
     Errors to Find:
         UnsupportedOperation: open("output.txt", "r") cannot be used for writing.
         Logical Error: open("log.txt", "w") will overwrite. It should be "a" for appending if multiple calls are intended to add.
         Logical Error: log_file.write("Second log entry.") is missing a newline, so it will append on the same line.
     Goal: Fix the UnsupportedOperation by changing the file mode. Change the log.txt open mode to append. Add a newline character to the second log entry.
Documentation Assignment:
     Scenario: This code writes two lines to a new file called my_notes.txt.
     Code to Document:with open("my_notes.txt", "w") as file: file.write("This is the first line.\n") file.write("This is the second line.\n")print("Notes written to my_notes.txt")
     Task: Add a docstring for the script. Add inline comments explaining the "w" mode and the use of \n.
     Goal: Document writing to a file.
## Lesson 8.3: Exceptions: Handling Errors
Proofreading Assignment:
     Scenario: You're trying to handle exceptions, but either not catching the right one, or the try-except block is placed incorrectly.
     Code to Proofread:# Division by zerotry: result = 10 / 0except ValueError: # Wrong exception type print("Caught a value error!")print("Program continues after division.")# File not foundtry: with open("non_existent.txt", "r") as f: content = f.read() print(content)except ZeroDivisionError: # Wrong exception type print("Caught a division by zero error!")# Invalid input for int()user_input_num = input("Enter a number: ")result = int(user_input_num) # Error will occur outside try-except if not numerictry: print(f"Your number is: {result}")except ValueError: print("Invalid input for number.")
     Errors to Find:
         Logical Error: First try-except block catches ValueError for a ZeroDivisionError.
         Logical Error: Second try-except block catches ZeroDivisionError for a FileNotFoundError.
         Logical Error: Third try-except block places the int() conversion outside the try, so ValueError won't be caught correctly.
     Goal: Correctly identify and handle ZeroDivisionError and FileNotFoundError. Move the int() conversion into the try block for the third scenario.
Documentation Assignment:
     Scenario: This code attempts a division and handles a potential ZeroDivisionError.
     Code to Document:try: numerator = 10 denominator = int(input("Enter a denominator: ")) result = numerator / denominator print(f"Result: {result}")except ZeroDivisionError: print("Error: Cannot divide by zero!")except ValueError: print("Error: Invalid input. Please enter a valid number.")
     Task: Add a docstring for the script. Add inline comments explaining the try block, each except block, and the specific errors they catch.
     Goal: Document robust error handling for division.
## Lesson 8.4: The else Block and finally Block
Proofreading Assignment:
     Scenario: You're using else and finally with try-except, but they're not always placed or behaving as expected.
     Code to Proofread:# Scenario 1: else blockdef safe_divide(a, b): try: result = a / b except ZeroDivisionError: print("Division by zero error!") else: # This else should be for the try, not just print print(f"Division successful: {result}") finally: # This finally should be for the try, not just print print("Safe divide function finished.")safe_divide(10, 2)safe_divide(10, 0)# Scenario 2: finally blockfile_name = "data.txt" # Assume this file existstry: f = open(file_name, "r") content = f.read() print(content)except FileNotFoundError: print(f"File {file_name} not found.")finally: f.close() # This will cause NameError if FileNotFoundError occurs and f isn't defined
     Errors to Find:
         Logical Error: In safe_divide, the else and finally are not properly aligned with the try block in Python syntax. They are part of the try-except construct.
         NameError: In the file handling scenario, if FileNotFoundError occurs, f is never assigned, so f.close() in finally will raise a NameError.
     Goal: Correct the indentation and placement of else and finally in safe_divide. Modify the file handling finally block to only close f if it was successfully opened (e.g., by initializing f = None before the try).
Documentation Assignment:
     Scenario: This code attempts to open and read a file, always printing a completion message.
     Code to Document:file_path = "existing_file.txt" # Assume this file existstry: with open(file_path, "r") as f: content = f.read() print(f"File content: {content}")except FileNotFoundError: print(f"Error: {file_path} not found.")else: print("File reading was successful.")finally: print("File operation attempted.")
     Task: Add a docstring for the script. Add inline comments for the try, except, else, and finally blocks, explaining when each block executes.
     Goal: Document the full try-except-else-finally structure.
## Lesson 8.5: Storing Data with JSON
Proofreading Assignment:
     Scenario: You're trying to save and load data using JSON, but common mistakes with the json module or file handling are occurring.
     Code to Proofread:import jsondata_to_save = {"name": "Test User", "id": 123}# Saving datawith open("user_data.json", "w") as f: f.write(json.dumps(data_to_save)) # Missing newline, also dump() is better# Loading datatry: with open("user_data.json", "r") as f: loaded_data = json.load(f) print(f"Loaded data: {loaded_data}")except json.JSONDecodeError: print("Error: JSON file is corrupted.")except FileNotFoundError: print("Error: JSON file not found.")# Incorrect JSON structure in file# Assume a file named 'bad_data.json' exists with content:# {"item": 10, "value": 20, "extra_comma": } # Malformed JSONtry: with open("bad_data.json", "r") as f: corrupted_data = json.load(f) print(f"Corrupted data: {corrupted_data}")except FileNotFoundError: print("Bad data file not found.")except ValueError: # Wrong exception type for JSON corruption print("Caught a ValueError!")
     Errors to Find:
         Logical/Best Practice: When writing JSON, it's better to use json.dump(data, file_object) directly, rather than json.dumps() and then f.write(). Also, f.write(json.dumps(data_to_save)) won't add a newline, so if you append later, it'll be on the same line.
         Logical Error: The except block for bad_data.json catches ValueError when it should catch json.JSONDecodeError.
     Goal: Change f.write(json.dumps(...)) to json.dump(data_to_save, f). Change the exception type for bad_data.json to json.JSONDecodeError.
Documentation Assignment:
     Scenario: This code saves a list of dictionaries (representing contacts) to a JSON file and then loads it back.
     Code to Document:import jsoncontacts = [ {"name": "Alice", "phone": "111-222-3333"}, {"name": "Bob", "phone": "444-555-6666"}]# Save contacts to JSON filewith open("contacts.json", "w") as f: json.dump(contacts, f, indent=4) # indent makes it human-readable# Load contacts from JSON filewith open("contacts.json", "r") as f: loaded_contacts = json.load(f)print("Loaded Contacts:")for contact in loaded_contacts: print(f"- Name: {contact['name']}, Phone: {contact['phone']}")
     Task: Add a docstring for the script. Add inline comments explaining json.dump() with the indent argument, and json.load().
     Goal: Document saving and loading structured data with JSON.
Unit 9: Testing Your Code and Introduction to Data Analysis
## Lesson 9.1: Testing a Function
Proofreading Assignment:
     Scenario: You've written tests for a function, but some assertions are wrong or the test setup is flawed.
     Code to Proofread:import unittestdef is_even(number): return number % 2 == 0class TestEvenNumbers(unittest.TestCase): def test_positive_even(self): self.assertFalse(is_even(4)) # This assertion is incorrect! def test_negative_even(self): self.assertTrue(is_even(-2)) # Correct def test_odd(self): self.assertTrue(is_even(7)) # This assertion is incorrect! def test_zero(self): self.assertNotEqual(is_even(0), False) # Correct, but perhaps assert True is clearer
     Errors to Find:
         Logical Error in Test: test_positive_even uses assertFalse when is_even(4) should be True.
         Logical Error in Test: test_odd uses assertTrue when is_even(7) should be False.
     Goal: Correct the assertions in test_positive_even and test_odd to accurately reflect the expected outcomes of is_even.
Documentation Assignment:
     Scenario: This code provides unit tests for a simple addition function.
     Code to Document:import unittestdef add(a, b): """Adds two numbers together.""" return a + bclass TestAddFunction(unittest.TestCase): """ Tests the add() function for various scenarios. """ def test_positive_numbers(self): """Test with two positive numbers.""" self.assertEqual(add(2, 3), 5) def test_negative_numbers(self): """Test with two negative numbers.""" self.assertEqual(add(-1, -5), -6) def test_zero(self): """Test with zero.""" self.assertEqual(add(0, 7), 7)if __name__ == '__main__': unittest.main()
     Task: Ensure the docstring for add is clear. Ensure docstrings for the TestAddFunction class and each test method (test_positive_numbers, etc.) clearly describe their purpose. Add an inline comment for unittest.main().
     Goal: Document a simple unit test suite.
## Lesson 9.2: Testing a Class
Proofreading Assignment:
     Scenario: You're testing a class, but forgetting self in assertions or setting up setUp incorrectly.
     Code to Proofread:import unittestclass Player: def __init__(self, name, health): self.name = name self.health = health def take_damage(self, amount): self.health -= amount if self.health < 0: self.health = 0class TestPlayer(unittest.TestCase): def setUp(): # Missing self parameter self.player = Player("Hero", 100) # NameError: self not defined def test_initial_health(self): assertEqual(self.player.health, 100) # Missing self. prefix def test_take_damage(self): self.player.take_damage(20) self.assertEqual(self.player.health, 80) # Correct def test_health_does_not_go_below_zero(self): self.player.take_damage(150) self.assertEqual(self.player.health, 0) # Correct
     Errors to Find:
         TypeError: setUp() is missing self.
         NameError: self.player is not defined in setUp because self is missing.
         NameError: assertEqual is missing self. prefix.
     Goal: Fix the TypeError in setUp. Add self. where necessary for assertEqual and self.player in setUp.
Documentation Assignment:
     Scenario: This code tests a BankAccount class.
     Code to Document:import unittestclass BankAccount: """ A simple bank account class. """ def __init__(self, initial_balance): self.balance = initial_balance def deposit(self, amount): self.balance += amount def withdraw(self, amount): if self.balance >= amount: self.balance -= amount return True return Falseclass TestBankAccount(unittest.TestCase): """ Tests the BankAccount class. """ def setUp(self): """Set up a fresh account for each test.""" self.account = BankAccount(100) def test_deposit(self): """Test depositing money.""" self.account.deposit(50) self.assertEqual(self.account.balance, 150) def test_withdraw_sufficient_funds(self): """Test withdrawing with enough funds.""" self.assertTrue(self.account.withdraw(30)) self.assertEqual(self.account.balance, 70)if __name__ == '__main__': unittest.main()
     Task: Ensure docstrings are present and clear for the class, setUp, and all test methods. Add inline comments explaining key assertions.
     Goal: Document a class's unit tests.
## Lesson 9.3: Introduction to Random Numbers
Proofreading Assignment:
     Scenario: You're generating random numbers, but misusing random module functions or ranges.
     Code to Proofread:import random# Generating a random integerrand_int = random.randint(1, 10) # Correctprint(f"Random integer: {rand_int}")# Generating a random floatrand_float = random.randfloat() # AttributeError: 'module' object has no attribute 'randfloat'print(f"Random float: {rand_float}")# Choosing from a listcolors = ["red", "green", "blue"]chosen_color = random.choice[colors] # TypeError: choice() takes no keyword argumentsprint(f"Chosen color: {chosen_color}")# Logical error: range for randintalways_ten = random.randint(10, 9) # This will raise ValueError because lower bound is > upper boundprint(f"Always ten: {always_ten}")
     Errors to Find:
         AttributeError: random.randfloat() should be random.random().
         TypeError: random.choice[colors] should be random.choice(colors).
         ValueError: random.randint(10, 9) has incorrect bounds.
     Goal: Fix all AttributeError, TypeError, and ValueError by using the correct random functions and argument syntax.
Documentation Assignment:
     Scenario: This code simulates rolling a six-sided die multiple times.
     Code to Document:import randomprint("Rolling a 6-sided die 5 times:")for _ in range(5): # Loop 5 times roll = random.randint(1, 6) # Generate a random integer between 1 and 6 print(f"Roll: {roll}")
     Task: Add a docstring for the script. Add inline comments explaining random.randint() and the purpose of the loop.
     Goal: Document random number generation for a simulation.
## Lesson 9.4: Analyzing Text Data
Proofreading Assignment:
     Scenario: You're analyzing text, but misusing string methods or counting logic.
     Code to Proofread:text = "Hello world. This is a test. Hello again."# Counting wordswords = text.split(" ") # Correctword_count = len(words)print(f"Word count: {word_count}")# Counting specific word (case sensitive)hello_count = words.count("Hello") # Correct, but case sensitiveprint(f"Count of 'Hello': {hello_count}")# Trying to remove punctuation and countcleaned_text = text.replace(".", "").replace(",", "").lower()cleaned_words = cleaned_text.split() # Correct, splits by whitespacetest_count = cleaned_words.count("test.") # Logical error: 'test.' won't be in cleaned_wordsprint(f"Count of 'test': {test_count}")# Counting characterschar_count = len[text] # TypeError: len() takes a single argumentprint(f"Character count: {char_count}")
     Errors to Find:
         Logical Error: test_count searches for "test." after punctuation has been removed.
         TypeError: len[text] should be len(text).
     Goal: Fix the TypeError. Correct the logical error in test_count by ensuring the search term is also cleaned (e.g., cleaned_words.count("test")).
Documentation Assignment:
     Scenario: This code counts the occurrences of each word in a given sentence.
     Code to Document:sentence = "The quick brown fox jumps over the lazy dog dog."words = sentence.lower().replace(".", "").split() # Convert to lowercase, remove punctuation, split into wordsword_counts = {}for word in words: word_counts[word] = word_counts.get(word, 0) + 1 # Increment count for each word, defaulting to 0print("Word Frequencies:")for word, count in word_counts.items(): print(f"'{word}': {count}")
     Task: Add a docstring for the script. Add inline comments explaining the steps of cleaning and splitting the sentence, how the word_counts dictionary is built, and the final output loop.
     Goal: Document a basic word frequency analysis.
## Lesson 9.5: Working with CSV Data (Text-based)
Proofreading Assignment:
     Scenario: You're parsing CSV data manually, but getting incorrect splits or type conversion issues.
     Code to Proofread:# Assume 'grades.csv' exists with content:# Name,Math,Science# Alice,90,85# Bob,75,92# Charlie,100,88file_content = """Name,Math,Science
Alice,90,85 Bob,75,92 Charlie,100,88"""
lines = file_content.split('\n') header = lines[0].split(',') # Correct for line in lines[1:]: parts = line.split(';') # Incorrect delimiter for split if len(parts) == len(header): # This condition might hide the error if len is same name = parts[0] math_grade = int(parts[1]) science_grade = float(parts[2]) # Correct conversion print(f"Name: {name}, Math: {math_grade}, Science: {science_grade}") else: print(f"Skipping malformed line: {line}") ```* **Errors to Find:** 1. Logical Error: `line.split(';')` uses the wrong delimiter (should be `,`). This will cause `IndexError` or `ValueError` later if not caught by `len(parts) == len(header)`.* **Goal:** Change the delimiter in `line.split()` to `,`. Explain how such an error would manifest (e.g., `IndexError` when trying to access `parts[1]`).
Documentation Assignment:
     Scenario: This code reads a simple CSV of product inventory and prints each product and its quantity.
     Code to Document:# Assume 'inventory.csv' exists with content:# Product,Quantity# Apple,100# Banana,50# Orange,75file_content = """Product,Quantity
Apple,100 Banana,50 Orange,75"""
lines = file_content.strip().split('\n') # Read all lines and split header = lines[0].split(',') # Get header (Product, Quantity) print(f"--- {header[0]} | {header[1]} ---") # Print header for line in lines[1:]: # Iterate over data rows, skipping header parts = line.split(',') # Split each line by comma product_name = parts[0] quantity = int(parts[1]) # Convert quantity to integer print(f"{product_name} | {quantity}") ```* **Task:** Add a **docstring** for the script. Add **inline comments** explaining `strip()`, `split('\n')`, identifying the header, looping through data rows, splitting by comma, and type conversion for quantity.* **Goal:** Document the process of manually parsing a CSV file.
Unit 10: Project-Based Learning: Building Text-Based Applications
## Lesson 10.1: Designing Your Project
Proofreading Assignment (No code to proofread in this conceptual lesson).
## Lesson 10.2: Building a Text-Based Adventure Game (Part 1)
Proofreading Assignment:
     Scenario: You're setting up your game's rooms and movement, but making dictionary access or conditional errors.
     Code to Proofread:rooms = { "start": {"description": "You are in a dimly lit cave.", "exits": {"north": "forest", "east": "river"}}, "forest": {"description": "You are in a dense forest.", "exits": {"south": "start"}}, "river": {"description": "A river flows quickly here.", "exits": {"west": "start"} # Missing closing curly brace for 'river' room and for 'rooms' dictionary}current_room = "start"while True: room_info = rooms[current_room] print(room_info["desc"]) # KeyError: 'desc' instead of 'description' print("Exits:", list(room_info["exits"].keys())) command = input("What do you do? ").lower() if command in room_info["exits"]: current_room = room_info.exits[command] # AttributeError: 'dict' object has no attribute 'exits' elif command == "quit": break else: print("Invalid command.")
     Errors to Find:
         SyntaxError: Missing closing curly brace(s) for the river room and the rooms dictionary.
         KeyError: room_info["desc"] should be room_info["description"].
         AttributeError: room_info.exits[command] should be room_info["exits"][command].
     Goal: Fix all SyntaxError, KeyError, and AttributeError issues.
Documentation Assignment:
     Scenario: This code sets up a simple game room and allows the player to look around.
     Code to Document:game_rooms = { "hall": { "description": "You are in a grand hall with high ceilings.", "exits": {"north": "kitchen", "south": "garden"} }}player_location = "hall"print(f"Current location: {player_location}")current_room_details = game_rooms[player_location]print(current_room_details["description"])print(f"Available exits: {', '.join(current_room_details['exits'].keys())}")
     Task: Add a docstring explaining the structure of game_rooms. Add inline comments for player_location, accessing room details, and displaying the description and exits.
     Goal: Document the setup and basic description of a game room.
## Lesson 10.3: Building a Text-Based Adventure Game (Part 2)
Proofreading Assignment:
     Scenario: You're adding inventory and item interaction to your game, but mismanaging list/dictionary operations or conditional logic.
     Code to Proofread:rooms = { "start": {"description": "A dark cave.", "items": ["torch", "rock"], "exits": {"north": "forest"}}, "forest": {"description": "A dense forest.", "items": [], "exits": {"south": "start"}}}player_inventory = []current_room = "start"while True: room_items = rooms[current_room]["items"] print(f"You see: {', '.join(room_items) if room_items else 'nothing'}.") command = input("Action? ").lower().split() if len(command) < 2: print("Need more info.") continue action = command[0] item_name = command[1] if action == "take": if item_name in room_items: room_items.remove(item_name) # This modifies the original room_items in dict player_inventory.append(item_name) print(f"You took the {item_name}.") else: print("That item is not here.") elif action == "drop": if item_name in player_inventory: player_inventory.remove(item_name) rooms[current_room]["items"].add(item_name) # AttributeError: 'list' object has no attribute 'add' print(f"You dropped the {item_name}.") else: print("You don't have that item.") elif action == "go": if item_name in rooms[current_room]["exits"]: current_room = rooms[current_room]["exits"][item_name] else: print("You can't go that way.") else: print("Unknown command.") print(f"Your inventory: {', '.join(player_inventory) if player_inventory else 'empty'}.")
     Errors to Find:
         AttributeError: rooms[current_room]["items"].add(item_name) should be append() because it's a list.
     Goal: Fix the AttributeError. Explain that list.add() is not a method and list.append() should be used.
Documentation Assignment:
     Scenario: This code simulates picking up and dropping an item in a simple game.
     Code to Document:current_room_items = ["key", "map"]player_inventory = []item_to_take = "key"if item_to_take in current_room_items: current_room_items.remove(item_to_take) player_inventory.append(item_to_take) print(f"You took the {item_to_take}.")else: print("Item not found in room.")print(f"Room items now: {current_room_items}")print(f"Your inventory: {player_inventory}")item_to_drop = "map"if item_to_drop in player_inventory: player_inventory.remove(item_to_drop) current_room_items.append(item_to_drop) print(f"You dropped the {item_to_drop}.")else: print("Item not in your inventory.")
     Task: Add a docstring for the script. Add inline comments explaining the "take" and "drop" logic, including list .remove() and .append() methods.
     Goal: Document basic item interaction in a game.
## Lesson 10.4: Developing a Command-Line Tool
Proofreading Assignment:
     Scenario: You're building a to-do list tool, but persistence is broken due to incorrect JSON handling or file modes.
     Code to Proofread:import jsonTODOS_FILE = "todos.json"def load_todos(): try: with open(TODOS_FILE, "r") as f: return json.load(f) except FileNotFoundError: return [] except json.JSONDecodeError: print("Warning: Corrupted todos.json, starting with empty list.") return []def save_todos(todos): with open(TODOS_FILE, "a") as f: # Should be "w" to overwrite, not append json.dump(todos, f, indent=4)todos = load_todos()while True: print("\n--- To-Do List ---") print("1. Add To-Do") print("2. View To-Dos") print("3. Save and Quit") choice = input("Enter choice: ") if choice == "1": task = input("Enter new task: ") todos.append(task) print("Task added.") elif choice == "2": if not todos: print("No to-dos yet.") for i, task in enumerate(todos): print(f"{i+1}. {task}") elif choice == "3": save_todos(todos) break else: print("Invalid choice.")
     Errors to Find:
         Logical Error: save_todos uses "a" mode for writing JSON. This will append the entire JSON structure to the file, creating invalid JSON. It should be "w" to overwrite.
     Goal: Correct the file mode in save_todos to "w" and explain why appending JSON directly can lead to corrupted files.
Documentation Assignment:
     Scenario: This code provides the core functions for a simple contact manager: adding and viewing contacts.
     Code to Document:contacts = []def add_contact(name, phone): """Adds a new contact to the global contacts list.""" new_contact = {"name": name, "phone": phone} contacts.append(new_contact) print(f"Contact '{name}' added.")def view_contacts(): """Displays all contacts currently stored.""" if not contacts: print("No contacts available.") return print("\n--- Your Contacts ---") for i, contact in enumerate(contacts): print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}")# Main loop (simplified for documentation)add_contact("Alice", "123-4567")add_contact("Bob", "987-6543")view_contacts()
     Task: Add docstrings for add_contact (explaining parameters and action) and view_contacts (explaining its display logic). Add inline comments explaining dictionary creation and list appending in add_contact, and the enumerate loop in view_contacts.
     Goal: Document core functions for a command-line tool.
## Lesson 10.5: Refinement and User Experience
Proofreading Assignment:
     Scenario: You're adding input validation and better error messages, but there are logical flaws or unhandled edge cases.
     Code to Proofread:def get_positive_number(prompt): while True: try: num_str = input(prompt) num = int(num_str) if num > 0: return num else: print("Please enter a positive number.") except ValueError: print("Invalid input. Please enter a whole number.") # Missing handling for empty input, which also raises ValueError # or for just pressing Enterdef main(): age = get_positive_number("Enter your age: ") print(f"You entered age: {age}") # Example of trying to use an invalid choice print("\nMenu: A. Option A, B. Option B") choice = input("Select an option (A/B): ").upper() if choice == "A": print("Option A selected.") elif choice == "B": print("Option B selected.") else: pass # This doesn't inform the user of an invalid choicemain()
     Errors to Find:
         Logical Error: get_positive_number has an except ValueError but doesn't explicitly handle empty input or just hitting Enter, which would re-raise ValueError or enter an infinite loop if not handled correctly.
         Logical Error: In main, the else: pass for invalid menu choice doesn't provide feedback to the user.
     Goal: Modify get_positive_number to ensure int() conversion happens before num > 0 check. For the else: pass in main, replace pass with a meaningful message to the user.
Documentation Assignment:
     Scenario: This code asks for a user's age and provides feedback, ensuring the input is a valid positive number.
     Code to Document:def get_valid_age(): """ Prompts the user for their age and ensures it's a positive integer. Continues prompting until valid input is received. """ while True: try: age_str = input("Please enter your age: ") age = int(age_str) if age > 0: return age else: print("Age must be a positive number. Please try again.") except ValueError: print("Invalid input. Please enter a whole number.")user_age = get_valid_age()print(f"Your age is: {user_age}")
     Task: Ensure the docstring for get_valid_age is thorough (explaining its purpose, input, output, and behavior). Add inline comments within the try and except blocks explaining their roles in validation.
     Goal: Document robust user input validation with clear feedback
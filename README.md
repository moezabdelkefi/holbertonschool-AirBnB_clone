<h1 align="center">AirBnB clone - The console</h1>

![815046647d23428a14ca](https://user-images.githubusercontent.com/113900578/221363211-737846a7-c120-46da-b868-805c28a7ce83.png)

This project is a command-line interface (CLI) for managing data related to a fictional Airbnb-like service. It allows users to create, update, and delete data related to states, cities, places, reviews, and users.

### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

.Create a new object (ex: a new User or a new Place)
.Retrieve an object from a file, a database etc…
.Do operations on objects (count, compute stats, etc…)
.Update attributes of an object
.Destroy an object

### General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function

Execution
.Your shell should work like this in interactive mode:

                                            $ ./console.py
                                            (hbnb) help

                                            Documented commands (type help <topic>):
                                            ========================================
                                            EOF  help  quit

                                            (hbnb) 
                                            (hbnb) 
                                            (hbnb) quit
                                            $
.But also in non-interactive mode: (like the Shell project in C)

                                            $ echo "help" | ./console.py
                                            (hbnb)

                                            Documented commands (type help <topic>):
                                            ========================================
                                            EOF  help  quit
                                            (hbnb) 
                                            $
                                            $ cat test_help
                                            help
                                            $
                                            $ cat test_help | ./console.py
                                            (hbnb)

                                            Documented commands (type help <topic>):
                                            ========================================
                                            EOF  help  quit
                                            (hbnb) 
                                            $
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## Command Interpreter:

### Starting the Command Interpreter
To start the command interpreter, run ./console.py in your terminal.

### Using the Command Interpreter
The command interpreter provides a prompt where users can enter commands to manage the data related to the Airbnb-like service.

The general syntax for a command is command class_id [optional arguments], where command is the action to take (e.g. create, show, destroy, update, all), class_id is the name of the class of data to operate on (e.g. User, State, Place), and optional arguments depend on the specific command and class.

To see a list of available commands, type help.

To get help for a specific command, type help command.

## Examples

Here are some examples of how to use the command interpreter:

                            (hbnb) create User email="test@test.com" password="password" first_name="John" last_name="Doe"
                            This creates a new user with the given email, password, first name, and last name.

                            (hbnb) show User 1234-5678-9012
                            This shows the details of the user with the given ID (1234-5678-9012).

                            (hbnb) update User 1234-5678-9012 email="newemail@test.com"
                            This updates the email of the user with the given ID to newemail@test.com.

                            (hbnb) all State
                            This shows a list of all states in the system.

## Tasks

### Unittests
All your files, classes, functions must be tested with unit tests

                            guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
                            ...................................................................................
                            ...................................................................................
                            .......................
                            ----------------------------------------------------------------------
                            Ran 189 tests in 13.135s

                            OK
                            guillaume@ubuntu:~/AirBnB$

Unit tests must also pass in non-interactive mode

                            guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
                            ...................................................................................
                            ...................................................................................
                            .......................
                            ----------------------------------------------------------------------
                            Ran 189 tests in 13.135s

                            OK
                            guillaume@ubuntu:~/AirBnB$

## flowchart

                                    |  Start   |
                                    +-----+----+
                                        |
                                        v
                            +----------------------------------------+
                            | Display prompt                         |
                            +----------------------+-----------------+
                                                |
                                                v
                            +-----------------------+----------------+
                            | Wait for user input                   |
                            +----------------------+-----------------+
                                                |
                                                v
                            +----------------------------------------+
                            | Parse user input and identify command  |
                            | and arguments                           |
                            +----------------------+-----------------+
                                                |
                                                v
                            +----------------------------------------+
                            | Execute command                        |
                            +----------------------+-----------------+
                                                |
                                                v
                            +-----------------------+----------------+
                            | If command is "quit":                   |
                            |     Exit the console                    |
                            +----------------------+-----------------+
                            | If command is "help":                   |
                            |     Display help text                   |
                            +----------------------+-----------------+
                            | If command is "create":                 |
                            |     Check if class name is valid        |
                            |     Create a new instance of the class  |
                            |     Save the instance to a file         |
                            |     Display the ID of the new instance  |
                            +----------------------+-----------------+
                            | If command is "show":                   |
                            |     Check if class name and ID are valid|
                            |     Retrieve the instance from the file |
                            |     Display the string representation  |
                            |     of the instance                     |
                            +----------------------+-----------------+
                            | If command is "destroy":                |
                            |     Check if class name and ID are valid|
                            |     Delete the instance from the file   |
                            +----------------------+-----------------+
                            | If command is "all":                    |
                            |     Check if class name is valid        |
                            |     Retrieve all instances of the class |
                            |     from the file                       |
                            |     Display the string representation  |
                            |     of each instance                    |
                            +----------------------+-----------------+
                            | If command is "update":                 |
                            |     Check if class name and ID are valid|
                            |     Update the instance with the        |
                            |     provided key-value pairs            |
                            |     Save the updated instance to the    |
                            |     file                                |
                            +----------------------+-----------------+
                            | If command is not recognized:           |
                            |     Display an error message            |
                            +----------------------+-----------------+
                                                |
                                                v
                            +----------------------------------------+
                            | Go back to step 1                       |
                            +----------------------+-----------------+

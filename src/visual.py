def print_user_commands(commands):
    """Print list of user commands and their descriptions"""
    for c in commands:
        print("{0}{1}".format(c, commands[c]))
    print

def clear_screen():
    """Clears the console.

    UPDATE TO BE CROSS-PLATFORM"""

    import os
    os.system('clear')

def print_title_bar():
    """Prints the double-skunk title bar"""
    print("====DOUBLE-SKUNK=============================")


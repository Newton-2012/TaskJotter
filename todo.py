import time

# ANSI Color Codes
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def line_break(n):
    print("-" * n)

# Checks for Empty List
def is_list_empty():
    try:
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
            lines = [line for line in lines if line.strip()]
            return len(lines) == 0
    except FileNotFoundError:
        return True

# Fake Loading for Aesthetics
def fake_loading(text="Loading", dots=9, delay=0.3, done_text="Done!"):
    print(text, end="", flush=True)
    for _ in range(dots):
        print(".", end="", flush=True)
        time.sleep(delay)
    print(done_text)

# Reads the list and checks for empty
def read_list():
    line_break(45)
    if is_list_empty():
        print(RED + "Empty List." + RESET)
        line_break(45)
        return
    with open('tasks.txt', 'r') as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}. {line.strip()}")
    line_break(45)

# Lets you add new items to the list (1 line per input)
def new_item():
    line_break(45)
    item = input(MAGENTA + "Enter New Item: " + RESET)
    with open("tasks.txt", "a") as f:
        f.write(item + "\n")
        fake_loading("Uploading", dots=12, delay=0.1, done_text="Done!")
        print(GREEN + "Item Added." + RESET)
    line_break(45)

# Erase items via index
def erase_item():
    line_break(45)
    if is_list_empty():
        print(RED + "Empty List." + RESET)
        line_break(45)
    with open("tasks.txt", "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")

    line_break(45)

    try:
        index = int(input(MAGENTA + "Enter the line number to delete: " + RESET)) - 1

        if 0 <= index < len(lines):
            del lines[index]
            with open("tasks.txt", "w") as f:
                f.writelines(lines)
            fake_loading("Editing", dots=12, delay=0.1, done_text="Done!")
            print(GREEN + f"Item successfully deleted at index {index + 1}." + RESET)
        else:
            print(RED + "Line non existent." + RESET)
    except ValueError:
        print(RED + "Value entered not an integer." + RESET)
    line_break(45)

# Command Center
def commands():
    while True:
        cmd = input(YELLOW + "Enter Command>>> " + RESET)
        if cmd == ":i":
            new_item()
        elif cmd == ":v":
            read_list()
        elif cmd == ":d":
            erase_item()
        elif cmd == ":h":
            print("Commands:\n:v - View all items in list\n:i - Enter new item\n:d - Delete item\n:h - Help Menu\n:q - Quit Program")
        elif cmd == ":q":
            line_break(45)
            fake_loading("Closing Application", dots=12, delay=0.05, done_text="")
            return
        else:
            print(RED + "Unknown command. Type :h for help." + RESET)
    
def main():
    line_break(45)
    print("Copyright (c) 2025 Newton2012 - MIT License")
    fake_loading("Starting Program")
    line_break(45)
    print(BLUE + "TasksJotter - Version 1.0.0" + RESET)
    line_break(45)
    commands()

if __name__ == "__main__":
    main()
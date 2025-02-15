#!/usr/bin/env python3
"""_summary_
"""
import re
import json


def make_all_numbers():
    """function that make all the cell-phone numbers in UY"""
    with open("all_number.txt", "w") as file:
        for n in range(91, 100):
            for i in range(1000000):
                file.write(f"{n:03}{i:06}" + "\n")


def forbidden_numbers():
    """not to call !!!
       write a valid number; like a: 099123456
    """
    try:
        number = input("write a valid number; like a: 099123456 > ")
        pattern = r"^09[1-9]\d{6}$"
        if re.match(pattern, number):
            with open("forbidden_numers.txt", "a") as file:
                file.write(number + "\n")
            print("The number has been saves succesfully.")
        else:
            print("Error: The number is not in the correct format (e.g., 099123456).")
    except ValueError:
        print("Error: input a valid number; like a: 099123456")


def agent_numbers():
    """this is for append a agent numers
    """
    try:
        agent_name = input("Enter the agent's name: ")
        number = input("write a valid number; like a: 099123456 > ")

        # regex for validate a number
        pattern = r"^09[1-9]\d{6}$"
        if re.match(pattern, number):
            try:
                with open("agent_numbers.json", "r") as file:
                    agent_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                agent_data = {}

            agent_data[agent_name] = number

            with open("agent_numbers.json", "w") as file:
                json.dump(agent_data, file, indent=4)
            print(f"The number for agent {agent_name} has been saved successfully.")
        else:
            print("Error: The number is not in the correct format (e.g., 099123456).")
    except ValueError:
        print("Error: Invalid input")

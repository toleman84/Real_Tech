#!/usr/bin/env python3
"""console for Real Tech - Call Center

    Returns:
        _type_: _description_
"""
import cmd

from call_center import forbidden_numbers, agent_numbers


class CallCenter(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """
    intro = "Welcome to the Call Center! Type help or ? to list commands.\n"
    prompt = "(call_to_all) "

    def do_exit(self, arg):
        """To exit the program

        Args:
            arg (_type_): _description_
        """
        print("Goodbye!")
        return True

    def do_empty_line(self):
        """_summary_
        """
        return True
    
    def do_help(self, arg):
        return super().do_help(arg)
    
    def do_EOF(self, arg):
        """_summary_
        """
        print("Goodbye! [EOF]")
        return True

    def do_forbidden_numbers(self, arg):
        """Calls the forbidden_numbers function"""
        forbidden_numbers()

    def do_agent_numbers(self, arg):
        """this is for append a agent numers

        Args:
            arg (_type_): _description_
        """
        agent_numbers()


if __name__ == "__main__":
    CallCenter().cmdloop()

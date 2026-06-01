// src/bye.py
"""
Goodbye module for the Hello World application.

This module provides a function to bid farewell and exit the application.
"""


def say_goodbye() -> None:
    """
    Prints a goodbye message and exits the application.
    
    Returns:
        None
        
    Raises:
        SystemExit: Always exits with code 0 after printing the message.
    """
    print("Goodbye!")
    raise SystemExit(0)
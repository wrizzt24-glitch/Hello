// src/main.py
"""
Main entry point for the Hello World application.

This script demonstrates the usage of the hello module functions.
"""

import argparse
import sys


def main() -> None:
    """
    Main function that executes the Hello World application.
    
    Returns:
        None
        
    Raises:
        Any exceptions raised by the hello module functions.
        SystemExit: When --bye flag is passed.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Hello World Application",
        prog="main.py"
    )
    parser.add_argument(
        "--bye",
        action="store_true",
        help="Print goodbye message and exit"
    )
    
    args = parser.parse_args()
    
    # Handle --bye flag
    if args.bye:
        from bye import say_goodbye
        say_goodbye()
        return
    
    # Import here to allow direct execution of this module
    from hello import say_hello, say_hello_to
    
    # Print classic hello world
    say_hello()
    
    # Print personalized greetings
    say_hello_to("World")
    say_hello_to("Python Developer")
    say_hello_to("Valhalla Team")


if __name__ == "__main__":
    main()
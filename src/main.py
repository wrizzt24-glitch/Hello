# src/main.py
"""
Main entry point for the Hello World application.

This script demonstrates the usage of the hello module functions.
"""


def main() -> None:
    """
    Main function that executes the Hello World application.
    
    Returns:
        None
        
    Raises:
        Any exceptions raised by the hello module functions.
    """
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
# src/hello.py
"""
Hello World module with greeting functions.

This module provides functions to print greetings to the console.
"""


def say_hello() -> None:
    """
    Print the classic "Hello, World!" message to the console.
    
    Returns:
        None
        
    Example:
        >>> say_hello()
        Hello, World!
    """
    print("Hello, World!")


def say_hello_to(name: str) -> None:
    """
    Print a personalized greeting to the specified name.
    
    Args:
        name: The name of the person to greet. Must be a non-empty string.
        
    Raises:
        ValueError: If name is None, empty, or contains only whitespace.
        TypeError: If name is not a string.
        
    Example:
        >>> say_hello_to("Alice")
        Hello, Alice!
    """
    # Input validation
    if not isinstance(name, str):
        raise TypeError(f"Expected string for name, got {type(name).__name__}")
    
    if not name or not name.strip():
        raise ValueError("Name cannot be empty or whitespace")
    
    # Sanitize input - strip whitespace and capitalize properly
    clean_name = name.strip()
    
    print(f"Hello, {clean_name}!")


if __name__ == "__main__":
    # Allow running this module directly for testing
    say_hello()
    say_hello_to("World")
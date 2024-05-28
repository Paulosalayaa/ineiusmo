try:
    # Code that may raise an exception
except ValueError as ve:
    # Handle ValueError specifically
    print(f"A ValueError occurred: {ve}")
except TypeError as te:
    # Handle TypeError specifically
    print(f"A TypeError occurred: {te}")
except Exception as e:
    # Handle any other exceptions
    print(f"An unexpected error occurred: {e}")

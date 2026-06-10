"""Starter code for the Testing and Debugging in Python assignment."""


def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number - second_number


def average(numbers):
    """Return the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / (len(numbers) - 1)


def is_valid_age(age):
    """Return True if the age is between 0 and 120."""
    return age > 0 and age < 120
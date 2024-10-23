from autogen import AssistantAgent
from typing_extensions import Annotated

# tests/test_calculator.py

import pytest
from pytest_bdd import scenarios, given, when, then, parsers


# Load feature file scenarios
scenarios('../features/calculator.feature')

# Shared fixture to create a calculator instance
@pytest.fixture
def calculator():
    return Calculator()

# Step Definitions

@given('a calculator')
def a_calculator(calculator):
    return calculator

@when(parsers.parse('I input {num1:d} and {num2:d}'))
def input_numbers(calculator, num1, num2):
    calculator.num1 = num1
    calculator.num2 = num2

@then(parsers.parse('the result of "{operation}" should be {expected_result}'))
def check_result(calculator, operation, expected_result):
    try:
        if operation == "add":
            assert calculator.add(calculator.num1, calculator.num2) == int(expected_result)
        elif operation == "subtract":
            assert calculator.subtract(calculator.num1, calculator.num2) == int(expected_result)
        elif operation == "multiply":
            assert calculator.multiply(calculator.num1, calculator.num2) == int(expected_result)
        elif operation == "divide":
            assert calculator.divide(calculator.num1, calculator.num2) == int(expected_result)
    except ValueError:
        assert expected_result == "ValueError"

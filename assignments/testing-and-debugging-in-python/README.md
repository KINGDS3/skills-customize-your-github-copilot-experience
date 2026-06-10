# 📘 Assignment: Testing and Debugging in Python

## 🎯 Objective

Learn how to verify Python code with automated tests and how to debug failing programs with a structured process. Students will write unit tests, inspect failing output, and fix bugs in a small utility module.

## 📝 Tasks

### 🛠️ Write Unit Tests

#### Description
Create a test file for the starter code using `pytest`. Focus on checking normal behavior, edge cases, and invalid input.

#### Requirements
Completed program should:

- Use `pytest` to test the starter functions
- Include at least 5 tests total
- Cover both successful cases and failure cases
- Use clear test names that describe the behavior being checked

### 🛠️ Find and Fix Bugs

#### Description
Run the starter code and use the tests to identify problems in the implementation. Fix the functions so the tests pass.

#### Requirements
Completed program should:

- Correct the broken function logic in the starter code
- Make sure each function returns the expected result
- Handle invalid input in a predictable way
- Pass all of the tests written for the assignment

### 🛠️ Improve Error Handling

#### Description
Add defensive checks so the program fails cleanly when it receives invalid values.

#### Requirements
Completed program should:

- Raise a helpful error for invalid inputs when appropriate
- Avoid crashing with unclear Python tracebacks
- Keep the code readable and easy to debug
- Show that the tests still pass after the changes
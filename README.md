Certainly! Here's the plain text version:

# Swap Case Python Script

## Description
This Python script provides a simple function, `swap_case`, that swaps the case of each character in a given string. Additionally, it includes a user interface that allows the user to input a string, swap the case, and then decide whether to try again or exit the program.

## How to Use
1. Run the script.
2. Enter the string you want to swap cases when prompted.
3. The script will display the result of swapping the case for each character in the entered string.
4. After viewing the result, you can choose to try again or exit the program.

## Functions

### 1. `swap_case(s: str) -> str`
   - **Input:** 
     - `s`: A string for which you want to swap the case of each character.
   - **Output:** 
     - Returns a new string with the case of each character swapped.

### 2. `try_again() -> None`
   - **Description:** 
     - Allows the user to decide whether to try the case-swapping process again or exit the program.
   - **Input:**
     - User input to determine whether to try again (`"y"`) or exit (`"n"`).
   - **Output:** 
     - Prints the swapped case string if the user chooses to try again.

## Test Cases
### Case 1: Basic Usage
```
assert swap_case("Hello, World!") == "hELLO, wORLD!"
```

### Case 2: Numeric and Special Characters
```
assert swap_case("123!@#") == "123!@#"
```

### Case 3: Mixed Case
```
assert swap_case("MiXeD CaSe") == "mIxEd cAsE"
```

### Case 4: Empty String
```
assert swap_case("") == ""
```

### Case 5: Try Again Function
```python
# Simulate user entering "y" to try again
assert try_again() == None

# Simulate user entering "n" to exit
assert try_again() == None
```

## Note
- The script uses a global variable `first_time` to determine whether it is the first time the user is entering a string. This is used to display the result without asking if the user wants to try again on the first run.

Feel free to use and modify the script as needed for your applications.

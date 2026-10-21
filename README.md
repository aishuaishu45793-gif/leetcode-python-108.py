# 🐍 LeetCode Python Practice (106–110)

## 📌 About This Repository

Welcome to my LeetCode Python practice repository! This repository contains five Python programming exercises designed to strengthen my coding skills, logical thinking, and problem-solving abilities.

Each program focuses on a different programming concept, including string manipulation, mathematical operations, lists, functions, and sorting.

## 🎯 Objectives

* Improve Python programming skills.
* Practice problem-solving and logical thinking.
* Understand Python functions and data structures.
* Learn string manipulation and mathematical operations.
* Build a consistent coding practice portfolio.
* Prepare for technical interviews and coding challenges.

## 💻 Technologies Used

* **Programming Language:** Python 3
* **Code Editor:** Visual Studio Code
* **Version Control:** Git
* **Repository Hosting:** GitHub

## 📂 Projects Included

| No. | Project Name                   | Description                                                 | Concepts                        |
| --- | ------------------------------ | ----------------------------------------------------------- | ------------------------------- |
| 106 | Count Vowels in a String       | Counts vowels in a given string.                            | Strings, loops, functions       |
| 107 | Reverse Words in a String      | Reverses the order of words in a sentence.                  | Strings, lists, slicing         |
| 108 | Find the Missing Number        | Finds a missing number from a sequence ranging from 0 to n. | Lists, arithmetic, functions    |
| 109 | Armstrong Number Checker       | Checks whether a number is an Armstrong number.             | Mathematics, strings, functions |
| 110 | Find the Second Largest Number | Finds the second-largest distinct number in a list.         | Lists, sets, sorting            |

---

## 1. Count Vowels in a String (106)

### Description

Counts the number of vowels (`a`, `e`, `i`, `o`, `u`) in a given string. Both uppercase and lowercase vowels are supported.

### Python Code

```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
```

### Example Output

```text
Enter a string: Hello World
Number of vowels: 3
```

### Concepts Learned

* String handling
* For loops
* Conditional statements
* Functions
* Counting characters

---

## 2. Reverse Words in a String (107)

### Description

Reverses the order of words in a sentence without reversing the characters inside individual words.

### Python Code

```python
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])


sentence = input("Enter a sentence: ")
print("Reversed sentence:", reverse_words(sentence))
```

### Example Output

```text
Enter a sentence: Python is easy
Reversed sentence: easy is Python
```

### Concepts Learned

* String manipulation
* Lists
* Slicing
* The `split()` method
* The `join()` method

---

## 3. Find the Missing Number (108)

### Description

Finds the missing number from a list containing distinct integers from `0` to `n`, with exactly one number missing.

### Python Code

```python
def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


nums = [0, 1, 3, 4, 5]
print("Missing number:", find_missing_number(nums))
```

### Example Output

```text
Missing number: 2
```

### Concepts Learned

* Lists
* The `len()` function
* The `sum()` function
* Arithmetic operations
* Problem-solving techniques

---

## 4. Armstrong Number Checker (109)

### Description

Checks whether a number equals the sum of its digits, with each digit raised to the power of the total number of digits.

For example:

**153 = 1³ + 5³ + 3³**

Therefore, 153 is an Armstrong number.

### Python Code

```python
def is_armstrong(number):
    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return total == number


number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
```

### Example Output

```text
Enter a number: 153
153 is an Armstrong number
```

### Concepts Learned

* Mathematical operations
* String conversion
* Functions
* Conditional statements
* The `sum()` function

---

## 5. Find the Second Largest Number (110)

### Description

Finds the second-largest distinct number in a list. Duplicate values are removed before sorting.

### Python Code

```python
def second_largest(nums):
    unique_nums = list(set(nums))

    if len(unique_nums) < 2:
        return None

    unique_nums.sort(reverse=True)

    return unique_nums[1]


nums = [10, 25, 8, 40, 25, 30]

result = second_largest(nums)

if result is None:
    print("Second largest number does not exist")
else:
    print("Second largest number:", result)
```

### Example Output

```text
Second largest number: 30
```

### Concepts Learned

* Lists and sets
* Removing duplicates
* Sorting
* Functions
* Conditional statements
* Handling special cases

---

## ⚙️ How to Run These Projects

### Prerequisites

Make sure Python 3 and Visual Studio Code are installed on your computer.

### Steps

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Open the Python file you want to run.
4. Open the VS Code terminal.
5. Execute the appropriate command.

For example:

```bash
python 106.py
```

To run the other programs, replace `106.py` with `107.py`, `108.py`, `109.py`, or `110.py`.

**Note:** The filenames above assume that each program is saved using its corresponding

### Part 1

***Problem:***
- Each line contains a sequence of integers
- A sequence is "safe" if it's either strictly increasing or decreasing and if the difference between two subsequent numbers is between 1 and 3
- How many "safe" sequences are there?

***Approach:***
- Define two `range` objects named `increasing` and `decreasing` which define the permissible difference ranges between two subsequent numbers of an increasing or decreasing sequence respectively
- Create a function `is_safe` that takes in a sequence of numbers `seq` and a `safe_range` of permissible steps between two numbers; it will return a boolean value depending on whether or not all steps in the sequence fall in the safe range
- Iterate the lines of the puzzle input, extract the number sequence and feed it into the `is_safe` function twice: once with the `increasing` and once with the `decreasing` safe range
- If at least one of them returns `True` increment the return value by one
- Once the loop is over return the total number of safe sequences

---

### Part 2

***Problem:***
- The same as in part 1, but the requirements are loosened a little bit: is permissible to skip one (and only one) number in the sequence
- How many "safe" sequences are there now?

***Approach:***
- The same basic structure from before with just a tiny modification
- While iterating over your list of sequences, create a nested for-loop which iterates the indices of each sequence and creates a new sequence in which the current index is skipped
- Feed each of these new sequences into the `is_safe` function twice: once with `increasing` and once with `decreasing`
- If any of these modified sequences turn out as valid, increment the return variable (python's `any` function is useful here)
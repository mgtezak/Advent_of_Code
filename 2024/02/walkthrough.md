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
- The same basic structure from before, but the `is_safe` function now needs a boolean flag `allow_skip` which will tell us, whether or not we're still allowed to skip a number in the sequence or whether we have already used up that chance
- We can no longer rely on naive indexing (i. e. `seq[i] - seq[i-1]`) to compare subsequent numbers, because if we skip a number we have to compare the next one to the one before; for this we keep track of the previous un-skipped number in a variable named `prev`
- We also have to keep in mind the edge case of having to skip the first number; we achieve this by making `allow_skip` an argument to the `is_safe` function; this way we can set `allow_skip` to `False` and pass in the sequence starting at the second number to simulate having skipped the first one
- We create the same loop as before but now have to check each sequence 4 times: increasing, decreasing, skipping & not skipping the first number

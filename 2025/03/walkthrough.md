### Part 1

***Problem:***
- Each line of the puzzle input consists of a row of equal length with numbers between 1 and 9
- By default all these numbers are "deactivated"
- We are supposed to activate 2 of them in order to create a maximally large 2-digit number (a so-called "joltage")
- Order matters, the number we use as first digit must come before the second digit within each row
- What is the sum of maximal joltages of each row?

***Approach:***
- Initialize a variable `total` to keep track of the sum
- Iterate the rows
- The first digit needs to be the largest number in the row excluding the last index
- Find its value and its index
- The second digit needs to be the largest number with an index larger than that of the first
- Concatenate them together and add them to `total`
- After the loop return `total`

---

### Part 2

***Problem:***
- Same problem as before but now we activate 12 instead of 2 numbers
- What is now the maximal sum of activated 12-digit numbers?

***Approach:***
- Same outer loop as before
- Within each iteration initialize a string variable `joltage` which keeps track of our number and a string variable `start` which keeps track of the lowest index we are allowed to use for the next digit
- Create an inner loop with a number `i` counting down from 11 to 0, representing the highest negative index we are allowed to use for the next digit
- In each iteration of the inner loop we look for the maximal number in the range specified by the indices `start` and `-i`
- We concatenate that number to `joltage` and use its index + 1 as our new `start` index
- After the inner loop runs through, convert `joltage` to a number and add it to `total`
- After the outer loop return `total`

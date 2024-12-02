### Part 1

***Problem:***
- Two columns of numbers of equal length should each be sorted from smallest to largest
- The sorted columns should then be paired up one by one
- What is the sum of the absolute difference of each pair?

***Approach:***
- Initialize two empty lists (one for each column) and a number variable to keep track of the final return value
- Extract the two numbers of each line and collect them in separate lists 
- Sort each list and create pairs by looping through them in parallel (`zip` is useful here)
- For each pair calculate the absolute difference between the two and add it to the total
- When the loop is done return the total

---

### Part 2

***Problem:***
- For each number of the first column we want to know how often it appears in the second column
- By multiplying the first column's number with its frequency in the second column we attain its score
- What is the sum of all these scores?

***Approach:***
- Initialize two empty dictionaries (one for each column) where the keys will correspond to the unique numbers of a column and the values correspond to their frequency
- Extract the two numbers of each line, increment the value of the first number in the first `dict` and the value of the second number in the second `dict`
- Initialize a variable to keep track of the final return value
- Iterate the set of unique numbers of the first column (i.e. the keys of the first `dict`) 
- Multiply each with its frequency in both the first and second column and add the result to the total
- When the loop is done return the total

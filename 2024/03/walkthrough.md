### Part 1

***Problem:***
- The puzzle input is a long string containing valid and invalid instructions to multiply pairs of numbers
- In order for the instructions to count as valid they have to strictly adhere to the following pattern: `mul(num1,num2)`
- What's the sum of these products?

***Approach:***
- Create a regular expression which matches this pattern and treats the two numbers as capture groups
- Initialize a return variable `total` and search the puzzle input for direct matches (`re.finditer` is useful here)
- Extract the two numbers of each match and add their product to the total
- Return `total`

---

### Part 2

***Problem:***
- The same basic problem as before but now valid matches become disabled if they appear after following pattern: `don't()`
- However, once this pattern appears: `do()`, then multiplications become enabled again
- What's the sum of valid and enabled products?

***Approach:***
- Create two more regular expressions matching `do()` and `don't()`
- Initialize a return variable `total` and a boolean flag `enabled`
- Search the puzzle input for all three expressions simultaneously (combine them using `|`)
- If `do()` or `don't()` is matched, set `enabled` to `True` or `False` respectively; if a multiplication is matched check the current state of `enabled` and if true add the product to the total
- Return `total`

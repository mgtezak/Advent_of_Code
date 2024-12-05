### Part 1

***Problem:***
- The puzzle input is a two dimensional grid made up entirely of the `X`, `M`, `A` & `S`
- Sometimes these letters appear in perfect sequence to form the word: `XMAS`
- This may happen forwards, backwards, horizontally, vertically or diagonally
- How often does `XMAS` appear in these various ways throughtout the grid?

***Approach:***
- Split the puzzle input into individual rows and extract the width and length of the grid
- Create a function named `count`:
    - It takes in a row and a column index and returns the number of times `XMAS` can be formed with these indices as the starting point
    - If there is no `X` at the starting position return `0` straight away
    - There are a maximum of 8 directions (2 horizontal, 2 vertical and 4 diagonal) that need to be checked
    - Be mindful of indexing errors when the starting position is close to one of the edges of the grid
- Iterate through each pair of row/column indices, count up the occurrences of `XMAS` and return the total

---

### Part 2

***Problem:***
- Instead of looking for occurrences of `XMAS` we are now looking for `X`-shaped overlapping occurrences of `MAS`, where there is an `A` in the middle and both diagonals spell out: `MAS` (again backwards spelling is allowed)
- How often does an `X`-shaped `MAS` appear throughtout the grid?

***Approach:***
- Scan the grid for the letter `A` and replace the `count` function with a `check` function, because an `A` can only ever be part of a single `X`-`MAS`
- Because the `A` has to be in the middle of an `X`-`MAS`, we only need to scan the inner rows and columns of grid
- The `check` function has to do three checks:
    - The current position is indeed an `A` 
    - The diagonal neighbors are composed of two `M`s and two `S`s
    - The `M`s and `S`s are not on opposite ends, because that would spell out `SAS` and `MAM` instead of `MAS`
- Count up the occurrences of `X`-`MAS` and return the total


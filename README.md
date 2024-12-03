# advent-2024

Yet another Advent of Code 2024 repository

## Solution Sketches
### Day 1
1. Implementation (sum absolute values of sorted lists)
2. Implementation; I build a dictionary to easily look up the number of occurrences of a number (this is mild overkill for the problem size).
### Day 2
1. I check first that the differences between adjacent values are valid, and then check that the sequence is monotonic.
2. Brute-force over all possible removals (as well as no removals)
### Day 3
1. I use a cursed checking function to look for the multiplication commands
2. Add in an enable flag to turn on and off multiplications
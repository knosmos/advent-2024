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
### Day 4
1. Search for `XMAS` in all 8 directions
2. Look for all the `A`s and match `M` and `S` across them diagonally
### Day 5
1. Brute force rule checking (index both numbers and check if the rule holds)
2. Construct an adjacency list from the conditions and build a topological sorting
### Day 6
1. Use a set to store previously visited positions, and simulate until we run out of bounds
2. For every position, check for infinite loops (if we ever end up in the same position and direction). This code could definitely be optimized, but hey it runs :D
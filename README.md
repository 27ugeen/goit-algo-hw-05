# goit-algo-hw-05

## Substring Search Algorithm Comparison

### Introduction
This project aims to compare the efficiency of three substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt (KMP), and Rabin-Karp. The comparison is based on their execution time when searching for two types of substrings in two different text files.

# Algorithm Performance Analysis

## Individual Text Analysis

### "art1.txt"

- **Boyer-Moore:** 0.127 milliseconds
- **Knuth-Morris-Pratt:** 0.524 milliseconds
- **Rabin-Karp:** 1.298 milliseconds

**Fastest algorithm for "art1.txt":** Boyer-Moore.

### "art2.txt"

- **Boyer-Moore:** 0.228 milliseconds
- **Knuth-Morris-Pratt:** 1.309 milliseconds
- **Rabin-Karp:** 3.302 milliseconds

**Fastest algorithm for "art2.txt":** Boyer-Moore.

## Overall Analysis

### Average Execution Time for Each Algorithm Across Both Texts

- **Boyer-Moore:** 0.177 milliseconds
- **Knuth-Morris-Pratt:** 0.916 milliseconds
- **Rabin-Karp:** 2.300 milliseconds

**Overall Fastest Algorithm:** Boyer-Moore.

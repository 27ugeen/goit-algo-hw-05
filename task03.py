import urllib.request
import timeit

# Implementation of Boyer-Moore algorithm
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0 or m > n:
        return -1

    last = {}
    for i in range(m):
        last[pattern[i]] = i

    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1

# Implementation of Knuth-Morris-Pratt algorithm
def knuth_morris_pratt(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1

    # Compute prefix function
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k

    # Search for pattern in text
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            return i - m + 1

    return -1

# Implementation of Rabin-Karp algorithm
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1

    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if pattern[j] != text[i + j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return -1

# Read the content of the text files
def read_text(filename):
    with open(filename, 'r') as file:
        return file.read()

# Load the contents of the text files
article1_file = "art1.txt"
article2_file = "art2.txt"
article1 = read_text(article1_file)
article2 = read_text(article2_file)

# Measure the execution time of each algorithm for each substring and each text file
for algorithm in [boyer_moore, knuth_morris_pratt, rabin_karp]:
    # Measure the execution time for article1
    substring1_article1 = "У цьому пошуку потрібно знайти"  # Substring that exists in the text
    substring2_article1 = "xyz23fge"  # Substring that does not exist in the text
    execution_time = timeit.timeit(lambda: algorithm(article1, substring1_article1), number=1) * 1000  # Convert to milliseconds
    print(f"{algorithm.__name__} - Substring: '{substring1_article1}', Text Length: {len(article1)}, Execution Time: {execution_time:.3f} milliseconds")
    execution_time = timeit.timeit(lambda: algorithm(article1, substring2_article1), number=1) * 1000  # Convert to milliseconds
    print(f"{algorithm.__name__} - Substring: '{substring2_article1}', Text Length: {len(article1)}, Execution Time: {execution_time:.3f} milliseconds")

    # Measure the execution time for article2
    substring1_article2 = "Искусство программирования, Том 4А"  # Substring that exists in the text
    substring2_article2 = "abc34red"   # Substring that does not exist in the text
    execution_time = timeit.timeit(lambda: algorithm(article2, substring1_article2), number=1) * 1000  # Convert to milliseconds
    print(f"{algorithm.__name__} - Substring: '{substring1_article2}', Text Length: {len(article2)}, Execution Time: {execution_time:.3f} milliseconds")
    execution_time = timeit.timeit(lambda: algorithm(article2, substring2_article2), number=1) * 1000  # Convert to milliseconds
    print(f"{algorithm.__name__} - Substring: '{substring2_article2}', Text Length: {len(article2)}, Execution Time: {execution_time:.3f} milliseconds")


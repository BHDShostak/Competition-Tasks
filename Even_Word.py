"""
In an even word, each letter occurs an even number of times.
Write a function solution that, given a string S consisting of N characters, returns the minimum number of letters that
must be deleted to obtain an even word.
Examples:
1. Given S = "acbcbba", the function should return 1 (one letter b must be deleted).
2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted).
3. Given S = "aaaa", your function should return 0 (there is no need to delete any letters).
Write an e
cient algorithm for the following assumptions:
N is an integer within the range [0..200,000];
string S consists only of lowercase letters (a−z).

"""


def is_even(n):
    if n % 2 == 0:
        return True
    return False


def solution(S):
    letter_counter = {}
    for letter in S:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    odd_letters_counter = 0
    for letter, counter in letter_counter.items():
        if is_even(counter):
            continue
        odd_letters_counter += 1
    return odd_letters_counter

S = "ldfsldkmslmcsc"
print(solution(S))
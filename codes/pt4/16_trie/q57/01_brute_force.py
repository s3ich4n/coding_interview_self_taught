from typing import List


def solution(
    words: List[str]
) -> List[List[int]]:
    def is_palindrome(word):
        return word == word[::-1]

    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                print(word1 + word2)
                output.append([i, j])

    return output


test1 = ["abcd", "dcba", "lls", "s", "sssll"]
print(solution(test1))

test2 = ["bat", "tab", "cat"]
print(solution(test2))

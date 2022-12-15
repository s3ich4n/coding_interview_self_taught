import collections

from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(words: str) -> bool:
        return words == words[::-1]

    def insert(
        self,
        index: int,
        word: str,
    ) -> None:
        """ Input값의 index와 word를 받고, Trie에 추가한다.

        뒤집은 단어에 대해 처리한다.
        """
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                # 문자열 자체가 팰린드롬인 경우?
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(
        self,
        index,
        word: str,
    ) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 로직 (3)
            # 탐색 도중 word_id가 있으며, 나머지 문자가 팰린드롬인 경우
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])

            if not word[0] in node.children:
                return result

            node = node.children[word[0]]
            # 하나씩 잘라가며 무한루프
            word = word[1:]

        # 판별로직 (1)
        # 끝까지 탐색했을 때 word_id가 있는 경우
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별로직 (2)
        # 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


def solution(words: List[str]) -> List[List[int]]:
    trie = Trie()

    for i, word in enumerate(words):
        trie.insert(i, word)

    results = []
    for i, word in enumerate(words):
        # iteration한 결과를 results에 바로 넣는 방식.
        #
        # 리턴값이 List[List[int]] 이고, extend되는 값은 아래와 같다
        # [[1, 3], [2, 1]] 의 [1, 3], [2, 1]이 각각 append 됨
        results.extend(trie.search(i, word))

    return results


# test1 = ["abcd", "dcba", "lls", "s", "sssll"]
# print(solution(test1))

# test2 = ["bat", "tab", "cat"]
# print(solution(test2))

test3 = ["d", "cbbcd", "dcbb", "dcbc", "cbbc", "bbcd"]
print(solution(test3))

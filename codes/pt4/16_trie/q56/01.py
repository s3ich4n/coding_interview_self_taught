import collections


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(
        self,
        word: str,
    ) -> None:
        node = self.root
        for char in word:
            # defaultdict 로직을 추가함으로 인해 불필요해짐
            # if char not in node.children:
            #     node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(
        self,
        word: str,
    ) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        # 단어인지/아닌지 여부를 체크
        return node.word

    def starts_with(
        self,
        word: str,
    ) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        # 진짜 있는 문자열인지만 체크
        return True


t = Trie()
t.insert("apple")
t.insert("appear")
t.insert("abnormal")
t.insert("acquire")
print(t.search("apple"))
print(t.search("application"))
print(t.starts_with("app"))

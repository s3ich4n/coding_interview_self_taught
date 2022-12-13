import collections

from typing import List


test = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


if __name__ == "__main__":
    print(group_anagrams(test))

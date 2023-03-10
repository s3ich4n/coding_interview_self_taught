import collections
import re

from typing import List


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def word_catcher(paragraph: str, banned: List[str]):
    words = [
        word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
        if word not in banned
    ]
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)


def another_word_catcher(
        paragraph: str,
        banned: List[str],
) -> str:
    words = [
        word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
        if word not in banned
    ]

    counts = collections.Counter(words)
    print(counts.most_common(1))
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    answer = word_catcher(
        paragraph=paragraph,
        banned=banned
    )
    print(answer)

    answer2 = another_word_catcher(
        paragraph=paragraph,
        banned=banned
    )
    print(answer2)

def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


s1 = "anagram"
t1 = "nagaram"

print(is_anagram(s1, t1))

s2 = "rat"
t2 = "car"

print(is_anagram(s2, t2))

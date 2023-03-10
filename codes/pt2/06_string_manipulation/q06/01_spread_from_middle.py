class Solution:
    def solution(self, s: str) -> str:
        def _expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) \
                    and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]

        # 뒤집어서 똑같은지 한번 봄.
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""

        # 슬라이싱은 n - 1만큼 리턴함에 유의!!!!!
        for i in range(len(s) - 1):
            # 세 값을 len으로 비교할거다.
            result = max(
                result,
                _expand(i, i + 1),
                _expand(i, i + 2),
                key=len,
            )

        return result


s = Solution()

q1 = "babad"
q2 = "cbbd"
q3 = "aseeffeb"
q4 = "ab"
q5 = "asdfghjklkjhgfdsa"

print(s.solution(q1))
print(s.solution(q2))
print(s.solution(q3))
print(s.solution(q4))
print(s.solution(q5))

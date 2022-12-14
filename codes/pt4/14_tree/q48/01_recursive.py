class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solution(
        self,
        root: TreeNode
    ) -> bool:
        def check(root):
            # 맨 아래(left, right가 None인데 까지 탐색하면) 0 나올 것임
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)

            # 높이 차이가 나면 -1
            #
            # TEST 2-1 처럼, 한번 -1의 결과가 리턴되어버리면 복구할 길이 없으므로
            # 판정은 다 했는데 끝까지 순회는 한다.
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            # 이 외에는 높이에 따라 1 증가
            return max(left, right) + 1

        return check(root) != -1


################
# TEST 1
################
# # lv3
# lv3_r1 = TreeNode(val=15, left=None, right=None)
# lv3_r2 = TreeNode(val=7, left=None, right=None)
# # lv2
# lv2_l = TreeNode(val=9, left=None, right=None)
# lv2_r = TreeNode(val=20, left=lv3_r1, right=lv3_r2)
# # lv1
# lv1 = TreeNode(val=3, left=lv2_l, right=lv2_r)

# s = Solution()

# test1 = s.solution(lv1)
# print(test1)


################
# TEST 2
################

# lv4
# t2_lv4_l1 = TreeNode(val=4, left=None, right=None)
# t2_lv4_l2 = TreeNode(val=4, left=None, right=None)
# # lv3
# t2_lv3_l1 = TreeNode(val=3, left=t2_lv4_l1, right=t2_lv4_l2)
# t2_lv3_l2 = TreeNode(val=3, left=None, right=None)
# # lv2
# t2_lv2_l = TreeNode(val=2, left=t2_lv3_l1, right=t2_lv3_l2)
# t2_lv2_r = TreeNode(val=2, left=None, right=None)
# # lv1
# t2_lv1 = TreeNode(val=1, left=t2_lv2_l, right=t2_lv2_r)

# s = Solution()

# test1 = s.solution(t2_lv1)
# print(test1)


################
# TEST 2 - 1 (2루트 서브트리의 우측노드 3이 없는 경우, 바로 판정이 나는가?)
#   잘 난다!
################

# lv4
t3_lv4_l1 = TreeNode(val=4, left=None, right=None)
t3_lv4_l2 = TreeNode(val=4, left=None, right=None)
# lv3
t3_lv3_l1 = TreeNode(val=3, left=t3_lv4_l1, right=t3_lv4_l2)
# lv2
t3_lv2_l = TreeNode(val=2, left=t3_lv3_l1, right=None)
t3_lv2_r = TreeNode(val=2, left=None, right=None)
# lv1
t3_lv1 = TreeNode(val=1, left=t3_lv2_l, right=t3_lv2_r)

s = Solution()

test1 = s.solution(t3_lv1)
print(test1)

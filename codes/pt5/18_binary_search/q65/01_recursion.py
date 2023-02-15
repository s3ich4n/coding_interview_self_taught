from typing import List


def search(nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            # 강타입일 때는 에러가 있을 수 있음.
            # 원래 (left + right) // 2인데, 이게 오버플로우 나면?
            # 그걸 고친 로직이 이거임. 파이썬은 해당없긴한데 참고하자.
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                return binary_search(mid + 1, right)

            elif nums[mid] > target:
                return binary_search(left, mid - 1)

            else:
                return mid

        else:
            return -1
    
    return binary_search(0, len(nums) - 1)


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(search(nums, target))

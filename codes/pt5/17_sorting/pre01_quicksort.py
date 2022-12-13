def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo

        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)


test1 = [7, 3, 9, 5, 1]

quicksort(test1, 0, len(test1) - 1)

print(test1)

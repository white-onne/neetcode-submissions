class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 오름차순으로 정렬된 배열에서의 중간값의 특징
        # 중간값 기준으로 왼쪽 오른쪽을 나눴을 때 왼쪽의 max<median 이고 오른쪽의 min이 median<min이 됨
        # 수학은 항상 느끼는건데 기본 개념을 잘 알아야 한다. 아무리 세세한거라도 알아둬야 함
        # 얕은 복사. 즉, 한 쪽을 수정하면 다른 쪽도 수정됨
        # 2차원 이상의 배열은 list()가 아닌 copy.deepcopy 사용해야 함
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2
        # 긴 배열을 A로
        if len(B)<len(A):
            A, B = B, A

        # 이해가 안감
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half - i -2
            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if (j+1)<len(B) else float("infinity")

            if Aleft<=Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Aright, Bright))/2
            elif Aleft>Bright:
                r = i - 1
            else:
                l = i + 1
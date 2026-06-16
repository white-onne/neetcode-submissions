class Solution:
    # 회전된 오름차순으로 정렬된 배열에서 target 찾기
    # 1. pivot(최솟값)을 구한다 ( left ~ pivot(0) ~ max )
    # 2. pivot을 기준으로 target의 탐색 범위를 지정한다
    # 3. 2번에 의해 지정된 탐색 범위 내에서 target을 찾는다
    def search(self, nums: list[int], target: int) -> int:
        # 1. pivot 찾기
        # pivot은 오름차순으로 정렬된 곳의 맨 왼쪽에 존재함
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[right]: # mid<right이면 mid ~ right 까지는 오름차순이라는 이야기 따라서 왼쪽으로 가서 최솟값을 찾는다. 이때 mid도 오름차순임으로 포함해야 함
                right = mid
            else:
                left = mid + 1
        pivot = left
        # 2. pivot을 기준으로 탐색 범위를 찾는다.
        left = 0
        right = len(nums)-1
        if target>=nums[pivot] and target<=nums[right]:
            left = pivot
        else:
            right = pivot - 1

        # 3. target을 찾는다
        while left<=right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

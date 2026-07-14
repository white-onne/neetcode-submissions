class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            if target == numbers[start] + numbers[end]:
                return [start+1, end+1]
            elif target > numbers[start] + numbers[end]:
                start += 1
            else:
                end -= 1
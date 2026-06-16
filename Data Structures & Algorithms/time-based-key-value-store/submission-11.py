from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.storing = defaultdict(list)  # key: [(timestamp, idx, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 저장
        cnt = 0
        if key in self.storing:
            cnt = len(self.storing[key])
        self.storing[key].append((timestamp, cnt + 1, value))
        # 정렬
        self.storing[key].sort(key=lambda x: (x[0], x[1]))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storing:
            return ""
        lst = list(self.storing[key])
        left = 0
        right = len(lst) - 1
        while left <= right:  # target이 없을 수도 있음
            mid = (left + right) // 2
            if lst[mid][0] <= timestamp:  # target이 같거나 더 크면 오른쪽 보기
                left = mid + 1
            else:
                right = mid - 1

        if lst[right][0] == timestamp:
            return lst[right][2]

        if lst[right][0] < timestamp:
            return lst[right][2]

        return ""
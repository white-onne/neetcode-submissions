class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1 # There will be no solution in this problem

        res = 0
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0: # If total is minus, we can go to the next step
                total = 0 # Should be reset as 0 because minus is same as 0(total, we can go to the next with minus value)
                res = i+1 # I don't understand why should be added, I guess it is okay to store i if total>0
        return res
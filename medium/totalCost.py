class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        sum = 0
        lowest = float("inf")

        while k > 0:
            for cost in costs:
                if cost < lowest:
                    lowest = cost
            sum += lowest
            costs.remove(lowest)
            lowest = float("inf")
            k -= 1

        return sum

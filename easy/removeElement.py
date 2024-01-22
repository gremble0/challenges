class Solution:
    def removeElement(self, nums: list[int], val: int) -> list[int]:
        return list(filter(lambda x: x != val, nums))

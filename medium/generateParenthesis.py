class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        combinations = []

        def dfs(left: int, right: int, combination: str):
            if len(combination) == n * 2:
                combinations.append(combination)
                return

            if left < n:
                dfs(left + 1, right, combination + "(")

            if right < left:
                dfs(left, right + 1, combination + ")")

            
        dfs(0, 0, "")
        return combinations

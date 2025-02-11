# Programação Dinâmica (Bottom-Up):
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Encontra o caminho com a menor soma em uma grade, utilizando Programação Dinâmica (Bottom-Up).
        """
        m, n = len(grid), len(grid[0])
        
        # Inicializa a tabela DP
        dp = [[0] * n for _ in range(m)]
        
        # Inicializa os casos base
        self.initialize_base_cases(dp, grid, m, n)
        
        # Preenchimento da tabela DP
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = self.compute_dp(dp, grid, i, j)
        
        return dp[m - 1][n - 1]
    
    def initialize_base_cases(self, dp, grid, m, n):
        """
        Inicializa os casos base para a tabela DP.
        """
        dp[0][0] = grid[0][0]
        
        # Preenche a primeira coluna
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        # Preenche a primeira linha
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    def compute_dp(self, dp, grid, i, j):
        """
        Computa o valor de dp[i][j] baseado nos valores mínimos possíveis.
        """
        return min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

def testCases():
    """
    Executa os casos de teste conforme os exemplos fornecidos.
    """
    solution = Solution()
    
    test_cases = [
        ([[1,3,1],[1,5,1],[4,2,1]], 7),
        ([[1,2,3],[4,5,6]], 12)
    ]
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = solution.minPathSum(grid)
        print(f"Test Case {i}: grid = {grid} -> Expected: {expected}, Got: {result}")
        assert result == expected, f"Test Case {i} Failed!"
    
    print("Todos os casos de teste passaram!")

# if __name__ == "__main__":
#     testCases()

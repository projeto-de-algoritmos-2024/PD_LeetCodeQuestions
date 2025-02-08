# Programação Dinâmica (Bottom-Up):

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Verifica se a string s corresponde ao padrão p utilizando Programação Dinâmica (Bottom-Up).
        """
        m, n = len(s), len(p)
        
        # Inicializa a tabela DP com False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Função para inicializar os casos base
        self.initialize_base_cases(dp, s, p)

        # Preenchimento da tabela DP
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = self.compute_dp(dp, s, p, i, j)
        
        return dp[m][n]
    
    def initialize_base_cases(self, dp, s, p):
        """
        Inicializa os casos base para a tabela DP.
        """
        dp[0][0] = True  # String vazia corresponde ao padrão vazio
        
        # Lidar com padrões contendo '*' que podem corresponder a uma string vazia
        for j in range(2, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

    def compute_dp(self, dp, s, p, i, j):
        """
        Computa o valor de dp[i][j] baseado nos caracteres de s e p.
        """
        if p[j - 1] == s[i - 1] or p[j - 1] == ".":
            return dp[i - 1][j - 1]
        
        if p[j - 1] == "*":
            # Caso onde ignoramos o caractere antes de '*'
            match_without_char = dp[i][j - 2]

            # Caso onde usamos o caractere antes de '*' se ele corresponder
            if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                return match_without_char or dp[i - 1][j]

            return match_without_char

        return False

def testCases():
    """
    Executa os casos de teste conforme os exemplos fornecidos.
    """
    solution = Solution()
    
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True)
    ]
    
    for i, (s, p, expected) in enumerate(test_cases, 1):
        result = solution.isMatch(s, p)
        print(f"Test Case {i}: s = \"{s}\", p = \"{p}\" -> Expected: {expected}, Got: {result}")
        assert result == expected, f"Test Case {i} Failed!"

    print("Todos os casos de teste passaram!")

# if __name__ == "__main__":
#     testCases()
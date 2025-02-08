# Knapsack (semelhante ao Longest Increasing Subsequence (LIS))

from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Resolve o problema das Russian Doll Envelopes usando Programação Dinâmica.
        Estratégia baseada no algoritmo de Knapsack (Longest Increasing Subsequence - LIS).
        """
        if not envelopes:
            return 0

        # Ordenar os envelopes por largura crescente e altura decrescente (para mesmo w)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Aplicar Longest Increasing Subsequence (LIS) nas alturas
        return self.longestIncreasingSubsequence([h for _, h in envelopes])

    def longestIncreasingSubsequence(self, heights: List[int]) -> int:
        """
        Encontra a Longest Increasing Subsequence (LIS) nas alturas usando DP + Binary Search.
        """
        lis = []  # Vetor que armazena a sequência mais longa encontrada

        for height in heights:
            index = bisect.bisect_left(lis, height)  # Busca binária para encontrar a posição correta
            if index == len(lis):
                lis.append(height)  # Adiciona novo elemento ao LIS
            else:
                lis[index] = height  # Substitui para manter LIS válida

        return len(lis)

def testCases():
    """
    Executa os casos de teste conforme os exemplos fornecidos.
    """
    solution = Solution()
    
    test_cases = [
        ([[5,4],[6,4],[6,7],[2,3]], 3),
        ([[1,1],[1,1],[1,1]], 1)
    ]
    
    for i, (envelopes, expected) in enumerate(test_cases, 1):
        result = solution.maxEnvelopes(envelopes)
        print(f"Test Case {i}: envelopes = {envelopes} -> Expected: {expected}, Got: {result}")
        assert result == expected, f"Test Case {i} Failed!"

    print("Todos os casos de teste passaram!")

# if __name__ == "__main__":
#     testCases()
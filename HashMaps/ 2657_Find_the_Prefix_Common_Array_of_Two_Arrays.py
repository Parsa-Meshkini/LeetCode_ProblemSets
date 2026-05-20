class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        seen = set()
        common = 0
        out = []

        for i in range(len(A)):

            if A[i] in seen:
                common += 1

            if B[i] in seen:
                common += 1

            if B[i] == A[i]:
                common += 1
            
            seen.add(A[i])
            seen.add(B[i])
            out.append(common)
        return out
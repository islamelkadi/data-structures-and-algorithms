class Solution:
    def numberOfSteps(self, num: int) -> int:
        def process_number(n: int) -> int:
            return n // 2 if n % 2 == 0 else n - 1
    
        operations = 0
        while num != 0:
            num = process_number(num)
            operations += 1
        return operations

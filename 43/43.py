class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        answer = [0] * (len(num1) + len(num2))
        
        first_number = num1[::-1]
        second_number = num2[::-1]
        
        for place2, digit2 in enumerate(second_number):
            for place1, digit1 in enumerate(first_number):
                num_zeros = place1 + place2
                carry = answer[num_zeros]
                multiplication = int(digit1) * int(digit2) + carry
                answer[num_zeros] = multiplication % 10
                answer[num_zeros + 1] += multiplication // 10
        
        if answer[-1] == 0:
            answer.pop()
            
        return ''.join(str(digit) for digit in reversed(answer))

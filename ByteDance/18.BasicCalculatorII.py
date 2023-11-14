class Solution:
    def evaluate(self, A, B, op):
        if op == '+':
            return int(A+B)
        if op == '-':
            return int(A-B)
        if op == '*':
            return int(A*B)
        if op == '/':
            return int(A/B)
    def calculate(self, s: str) -> int:
        digit_stack = []
        operator_stack = []
        curr_num = 0
        d = {
            '/': 2, '*': 2,
            '+': 1, '-': 1
        }
        for i in range(len(s)):
            if s[i] in d:
                digit_stack.append(curr_num)
                curr_num = 0
                while operator_stack and d[operator_stack[-1]] >= d[s[i]]:
                    B = digit_stack.pop()
                    A = digit_stack.pop()
                    op = operator_stack.pop()
                    digit_stack.append(self.evaluate(A,B, op))
                operator_stack.append(s[i])
            elif s[i].isdigit():
                curr_num = curr_num*10 + int(s[i])
        digit_stack.append(curr_num)

        while operator_stack:
            B = digit_stack.pop()
            A = digit_stack.pop()
            op = operator_stack.pop()
            temp = self.evaluate(A,B, op)
            print(temp)
            digit_stack.append(temp)

        return digit_stack.pop()
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ('+', '-', '*', '/')
        nums = []

        for t in tokens:
            if t in op:
                n1 = nums.pop()
                n2 = nums.pop()
                match (t):
                    case "+":
                        n = n2 + n1
                    case "-":
                        n = n2 - n1
                    case "*":
                        n = n2 * n1
                    case "/":
                        n = abs(n2) // abs(n1)
                        if (n2 * n1) < 0:
                            n = -n

                nums.append(n)
            else:
                nums.append(int(t))

        return nums.pop()

# 1 2 3 4
# + * -
# - * +
# tokens=["4","13","5","/","+"] -> 6
# 4 13 5
# / +
# 5 13 4
# + /

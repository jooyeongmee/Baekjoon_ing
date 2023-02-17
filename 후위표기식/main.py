import sys

N = int(input())
input_str = sys.stdin.readline().strip()
stack = []

for j in range(N):
  arg = sys.stdin.readline().strip()
  input_str = input_str.replace(chr(65 + j), arg)
print(input_str)
for i in range(len(input_str)):
  if input_str[i] == '*':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top1 * top2)
  elif input_str[i] == '+':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top1 + top2)
  elif input_str[i] == '-':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top2 - top1)
  elif input_str[i] == '/':
    top1 = stack.pop()
    top2 = stack.pop()
    stack.append(top2 / top1)
  else:
    stack.append(int(input_str[i]))

print("{:.2f}".format(stack[0]))


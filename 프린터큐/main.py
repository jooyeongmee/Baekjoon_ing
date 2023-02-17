import sys
import numpy as np

num = int(input())
for i in range(num):
  N, target_idx = map(int, sys.stdin.readline().split())
  queue = list(map(int, sys.stdin.readline().split()))
  data = np.array(queue)
  
  j = 0
  count = 0
  while True:
    if len(queue) == 1:
        count += 1;
        print(count)
        break
    if j == len(queue): j = 0
    most_import = data.max()
    print("j: " + str(j))
    if queue[j] != most_import:
      j += 1
    else:
      count += 1
      top = queue[j]
      del queue[j]
      data = np.array(queue)
      if j == target_idx:
        print(count)
        break
      
      
      
      
      
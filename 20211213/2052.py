# 지수연산

## 생각을 해보니까 10의 -4승보다 작은 분수의 경우에는 딱히 문제가 안되는데
## 그보다 작은 경우에는 1e-05처럼 되어 있어서 별도의 처리가 필요할 것 같았다...

n = int(input())
p = "%.300f" % 2 ** -n

q = len(p)

for i in range(q-1, 1, -1):
  if p[i] != '0':
    q = i
    break
print(p[:q+1])
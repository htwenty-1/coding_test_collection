# 타임 카드

for _ in range(3):
  h1, m1, s1, h2, m2, s2 = map(int, input().split())
  # 입력 받은 시간을 초단위로 바꿔줌
  t1 = (h1 * 60 * 60) + (m1 * 60) + s1
  t2 = (h2 * 60 * 60) + (m2 * 60) + s2
  # 근무 시간
  t = t2 - t1
  # 시간으로 다시 바꿔줌
  h = t//60//60 % 24
  # 분으로 다시 바꿔줌
  m = t//60 % 60
  # 초로 다시 바꿔줌
  s = t%60
  print(h, m, s)
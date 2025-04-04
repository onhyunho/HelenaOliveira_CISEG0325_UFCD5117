def bonatchi(n):
  bonbon = [0, 1] 
  for i in range(2, n):
    bon = bonbon[i - 1] + bonbon[i - 2]
    bonbon.append(bon)
  return bonbon

primeiros_60 = bonatchi(60)
print(primeiros_60)
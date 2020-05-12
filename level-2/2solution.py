def solution(s):
  p = 0
  l = list(s)
  for i in xrange(len(l)):
    if l[i] == '>':
      for j in xrange(i,len(l)):
        if l[j] == '<':
          p += 2
  return p
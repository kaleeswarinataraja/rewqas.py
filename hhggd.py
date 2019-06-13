d1,f1=input().split()
d1=int(d1)
f1=int(f1)
for i in range(d+1,f1):
  if(i>0):
    for p in range(2,i):
      if(i%p==0):
        break
    else:
      print(i,end=' ')
  else:
    break
© 2019 GitHub, Inc.

def linearsearch(a,el):
  for i in range(len(a)):
    if a[i]==el:
      print(f'element is found at index (i)')
      return
  print('element not found')
a=[12,11,44,32,23,1,8,5]
linearsearch(a,23)

def linearsearch(a,el):
  for i in range(len(a)):
    if a[i]==el:
      #print(f'element is found at index (i)')
      return i
  #print('element not found')
  return -1
a=[12,11,44,32,23,1,8,5]
print(linearsearch(a,23))

def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if  a[i]==el:
      ar.append(i)
      #print(f'element is found at index (i)')
      #return i
  #print('element not found')
  return ar
a=[12,11,44,32,23,1,8,5]
res=linearsearch(a,23)
for i in res:
  print(i,end=" ")
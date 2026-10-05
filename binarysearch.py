def binarysearch(a,el):
    l=0
    r=len(a)
    while l<r:
        m=(l+r)//2
        if l==m:
            return -1

        if a[m]==el:
            return m
        elif a[m]<el:
            l=m
        else:
            r=m
        return -1  
a=[2,4,5,6,12,16,22,34]
print(binarysearch(a,12))
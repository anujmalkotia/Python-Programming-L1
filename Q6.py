def lmax(lst,l):
    a=max(lst)
    l.append(a)
    lst.remove(a)
    b=max(lst)
    l.append(b)
    
def lmin(lst,n1):
    a=min(lst)
    n1.append(a)
    lst.remove(a)
    b=min(lst)
    n1.append(b)

def Average(lst):
    return (sum(lst)/len(lst))

list1=[1,3,5,13,88,12]
list2=[11,421,22,53,12,20]
list3=[40,89,90,11]

mx1=[]
mx2=[]
mx3=[]
mn1=[]
mn2=[]
mn3=[]

lmax(list1,mx1)
lmax(list2,mx2)
lmax(list3,mx3)

lmin(list1,mn1)
lmin(list2,mn2)
lmin(list3,mn3)

Maxlist = mx1+mx2+mx3
print("MAXLIST",Maxlist)
Minlist=mn1+mn2+mn3
print("MINLIST",Minlist)
print("AVERAGE MAXLIST",Average(Maxlist))
print("AVERAGE MINLIST",Average(Minlist))

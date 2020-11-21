#bruteforce approach
a=[]
def sub(s,n):      #generated substring an stored in a list
    for i in range(n):
        for len in range(i+1,n+1):
            a.append(set(s[i:len]))     #converted substring to set
s=input("")
sub(s,len(s))
max=1
for i in a:
     if len(i)>max:
         max=len(i)      #stored the the length of substring conatining maximun unique characters
print(max)
#directly using set and reducing the time complexibility
# s=input("")
# g=set(s)
# print(len(g))
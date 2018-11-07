import time
import math
final=[]
def nearest(s, d):
        dist=0
        # s=list(m)
        selected=[]
        selected.append(int(s[0]))
        next =0
        tnext=0
        for j in range (0 ,len(d[0])-1):
            min = 1000000
            for i in range (1 , len(d[0])):
                if str(i) in s:
                        if d[next][i] <min and d[next][i] > 0 :
                                min = d[next][i]
                                tnext = i
            next = tnext
            selected.append(next)
            dist += min
            if str(next) in s:
                s.remove(str(next))
        dist += d[0][next]
        print (selected , dist)

def exhaustive( m , k, n ,d,distance):
    min = 100000
    s=list(m)
    temp =0
    if k==n :
        e=[]
        for i in range(0 ,len(s)) :
                e.append(int(s[i]))
        for i in range(0 ,len(s)-1) :
                temp = temp + d[e[i]][e[i+1]]
        temp=temp + d[e[len(s)-1]][e[0]]
        if s[0] == "0" and temp < distance:
                distance = temp
                final.append( temp )
                final.append("".join(s))
    else:
        for i in range(k ,n+1) :
                c = s[i]
                s[i]=s[k]
                s[k]=c
                exhaustive("".join(s),k+1,n ,d,distance)
    if len(final) == 240 : ################################## 12 ro motanesban taghir bedam =2* n-1 !
        for z in range (0 , int(len(final)/2)):
                if final[2*z] <min :
                        min = final[2*z]
                        str = final[2*z+1]
        print(min , str)
s=[]
size = input("number of nodes?") 
node = []
inner=[]
for i in range(0 , int(size)) :
    inner.append(0)
    s.append(str(i))
# for i in range(0 ,int(size)) :
#     node[i]=input("cordination: i.j")

with open('check2.txt') as f:
     read_data = f.read()
node = read_data.split('\n')

p = [[0 for x in range(2)] for y in range(int(size))] 
start =time.time()

for j in range(0 ,int(size)) :
    for i in range(0 ,2) :
        p[j][i]=int(node[j].split(' ')[i])


d =[[0 for x in range(int(size))] for y in range(int(size))] 

for i in range(0 ,int(size)) :
    for j in range(0 ,int(size)) :
        d[i][j] =math.sqrt( (p[j][0] -p[i][0])*(p[j][0] -p[i][0]) + (p[j][1] - p[i][1])*(p[j][1] - p[i][1]))

exhaustive("012345",0,int(size) - 1,d,1000000000) #-----------------inja ro ham dorost konam
# nearest(s , d)
stop = time.time()
print("runtime" , stop - start)



import  random
import operator
import time

def xulie(a,b,cishu):
    #start=time.time()
    f=open("./text.txt","a")
    zidian={ii:0 for ii in range(1,a+1)}
    while cishu>0:                #次数
        shuzu=list(range(1,a+1))  #生成所有数列
        a1 = a
        b1 = b
        while b1>0:                #选号数
            c=random.randint(1,a1)
            if c in shuzu:
                shuzu=[x for x in shuzu if x!=c]
                zidian[c]+=1
                b1-=1
        cishu-=1
        time.sleep(random.randint(1,35)*random.randint(1,12)*0.0000007)
    ddd=sorted(zidian.items(), key=operator.itemgetter(1), reverse=True)[:b+1]
    ddd=sorted([ddd[s][0] for s in range(len(ddd)-1)])
    print(ddd)
    f.close()
    #end=time.time()
    #print(end-start)

cishu=100
xulie(35,5,cishu)
xulie(12,2,cishu)
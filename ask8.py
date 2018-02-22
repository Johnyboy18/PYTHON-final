import random

def Check(i,j,k,tr):
    if [i,j,k] in tr or [i,k,j] in tr or [k,i,j] in tr or [k,j,i] in tr or [j,i,k] in tr or [j,k,i] in tr:
        return False
    else:
        return True

while True:
    lst = random.sample(range(-30,30),30) #dimiourgia pinaka me mono thetikous kai arnitikous opos ziteitai
    if not (0 in lst):
        break

f=False 
triades=[] 
for i in lst: #kathe syndiasmos
    for j in lst:
        for k in lst:
            if i+j+k==0 and Check(i,j,k,triades):
                triades.append([i,j,k])
                f=True

if f==False:
    print "Den vrethike triada"
else:
    for tr in triades: 
        tr.sort()
        print tr
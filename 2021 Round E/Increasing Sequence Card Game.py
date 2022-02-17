#author:quikziii
#https://quikzihao.web.app/

import math

case = int(input())
temp = 0
count = 1 
AnsArray=[0]
max = 0
for i in range(case):
    n = int (input())
    if(n>max and n<10**6):
        while(count<=n):
            temp = temp + 1/count
            count = count +1
            AnsArray.append(temp) 
    if(n < (10 **6)):
        print(f"Case #{i+1}: {AnsArray[n]}")
    else:
        print(f"Case #{i+1}: {0.57721566490153286060651209008240243104215933593992 + math.log(n) + 0.5 / n}")


    
#author:quikziii
#https://quikzihao.web.app/

def checkmove(testchar,listcheck):
    minimun=27
    for i in listcheck:
        temp=ord(testchar)-ord(i)
        temp=abs(temp)
        if(temp>13):
            temp=26-temp
        if(temp<minimun):
            minimun = temp
    return minimun
    
def string2Char(word):
    return [char for char in word]
    
def solve(num):
    testString = input()
    checkString = input()
    testList = string2Char(testString)
    listcheck = string2Char(checkString)
    ans = 0
    for i in testList:
        ans = ans + checkmove(i,listcheck)
    print(f"Case #{num}: {ans}")
    
n=int(input())
for i in range(1,n+1):
    solve(i)

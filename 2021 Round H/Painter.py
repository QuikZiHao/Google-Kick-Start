#author:quikziii
#https://quikzihao.web.app/

def solve(num):
    size = int(input())
    result = [char for char in input()]
    needed = checkNeeded(result)
    needed = becomeNeeded(needed)
    move= 0 
    for i in range(0,3):
        move = move + addColor(needed,i)
    print(f"Case #{num}: {move}")

def checkNeeded(result):
    needed=[]
    temp = result[0]
    for i in result:
        if temp != i :
            needed.append(temp)
            temp = i
    needed.append(temp)
    return needed
    
def becomeNeeded(needed):
    new=[]
    mixList = {"R":['1', '0', '0'],"Y":['0', '1', '0'],"B":['0', '0', '1'],"O":['1', '1', '0'],"P":['1', '0', '1'],"G":['0', '1', '1'],"A":['1', '1', '1'],"U":['0', '0', '0']}
    for i in needed:
        new.append(mixList[i])
    return new
    
        
def addColor(needed,num):
    move=0
    gotColor=False
    for i in needed:
        if(i[num]=="1"):
            if(gotColor):
                move = move - 1
            gotColor=True
        else:
            gotColor=False
        if(gotColor):
            move = move + 1
    return move
                   
num = int(input())
for i in range (num):
    solve(i+1)

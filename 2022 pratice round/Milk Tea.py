#author:quikziii
#https://quikzihao.web.app/

def countComplaint(preferences,locate):
    complaint = 0
    for i in preferences:
        if(i[locate] == "1"):
            complaint = complaint + 1
    return complaint


def milkTeaSolve():
    num_friends, num_forbidden, num_options = map(int, input().split())
    preferences = [input() for _ in range(num_friends)]
    forbiddens =[input() for _ in range(num_forbidden)]
    choosenList = []
    disturbList = []
    for locate in range (0,num_options):
        complaint0 = countComplaint(preferences,locate) #which choose 0 complaint
        complaint1 = num_friends-complaint0
        if(locate == 0):
            thisLayer = []
            thisLayer.append(("0",complaint0))
            thisLayer.append(("1",complaint1))
        else:
            thisLayer.sort(key=lambda x:x[1])
            lastLayer = thisLayer[0:num_forbidden+2]
            thisLayer = []
            while(len(lastLayer)!=0):
                temp = lastLayer[-1][0]
                lastComplaint = lastLayer[-1][1]
                lastLayer.pop()
                thisLayer.append((temp+"0",lastComplaint+complaint0))
                thisLayer.append((temp+"1",lastComplaint+complaint1))
    thisLayer.sort(key=lambda x:x[1])
    for i in thisLayer:
        if(i[0] not in forbiddens):
            return i[1]

case = int(input())
for num in range(1,case+1):  
    print(f"Case #{num}: {milkTeaSolve()}")

        


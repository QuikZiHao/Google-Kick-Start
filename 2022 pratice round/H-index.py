#author:quikziii
#https://quikzihao.web.app/

def h_index(n, citations):
  ans = []
  hIndex = 1
  hashList = [0]*100001
  score = 0
  for i in citations:
      if(i>=hIndex):
        hashList[i] = hashList[i]+1
        score = score + 1
        score = score-hashList[hIndex-1]
        hashList[hIndex-1] = 0
        if(score >=hIndex):
            hIndex = hIndex + 1 
        ans.append(hIndex-1)
      else:
          ans.append(hIndex-1)  
  return ans


if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):
    n = int(input())                      # The number of papers
    citations = list(map(int,input().split(" ")))  # The number of citations for each paper
    h_index_scores = h_index(n, citations)
    print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))

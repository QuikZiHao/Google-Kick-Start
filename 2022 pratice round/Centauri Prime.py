#author:quikziii
#https://quikzihao.web.app/

# TODO: Complete the get_ruler function
def get_ruler(kingdom,vowels):
    ruler = ''
    check = kingdom [-1]
    if (check == "y" or check =="Y"):
        ruler = "nobody"
    elif (check in vowels):
        ruler = "Alice"
    else:
        ruler = "Bob"  
    return ruler

def main():
  # Get the number of test cases
  T = int(input())
  vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom,vowels)))

if __name__ == '__main__':
  main()

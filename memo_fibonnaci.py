
memo = {}

def memo_fibonnaci(n):

    if n in memo.keys():
        return memo[n]
    elif n<2:
        memo[n]=1
    else:
        memo[n] = memo_fibonnaci(n-1)+memo_fibonnaci(n-2)
    return memo[n]

def main():

    print('Give an integer: ')
    n = input()
    print"The "+str(n)+"th fibonnaci number is: ", memo_fibonnaci(n)

main()
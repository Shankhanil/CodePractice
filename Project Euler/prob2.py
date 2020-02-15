if __name__ == "__main__":
	
    x = 1
    y = 2
    n = 0
    sum = 2
    while n < 4000000 :
        n = x + y
        #L.append( n )
        x = y
        y = n
        #print(n, end = ' ')
        if n%2 == 0:
            sum = sum+n
    print(sum)
    #print(L)
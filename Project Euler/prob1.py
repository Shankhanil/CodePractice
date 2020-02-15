"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
if __name__ == "__main__":
	
    div= []
    div3 = list(range(3,1000,3))
    div5 = list(range(5,1000,5))
    
    #div = div.append(div3)
    div3.extend(div5)
    
    SUM = sum(list(dict.fromkeys(div3)))
    
    print(SUM)
if __name__ == "__main__":
	
    div= []
    div3 = list(range(3,1000,3))
    div5 = list(range(5,1000,5))
    
    #div = div.append(div3)
    div3.extend(div5)
    
    SUM = sum(list(dict.fromkeys(div3)))
    
    print(SUM)
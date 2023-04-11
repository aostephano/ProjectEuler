def fibboGenerator():
    fibboList = [0, 1]
    nextFibbo = 0
    
    while len(str(nextFibbo)) < 1000:
            predFibbo = fibboList[-1]
            predPredFibbo = fibboList[-2]
            nextFibbo = predFibbo + predPredFibbo
            fibboList.append(nextFibbo)
            # print(len(str(nextFibbo)), ":", nextFibbo)
    
    print("Index:", len(fibboList)-1, "Digits:", len(str(fibboList[-1])), "Value:", fibboList[-1])
    
fibboGenerator()
def SwapFileData():
    file1Name= input(" enter a file name : ")
     file2Name= input(" enter a file name : ")

    with open(file1Name ,"r")as a:
        data_a = a.read()

    with open(fil2eName,"r")as b:
        data_b = b.read()

    with open(file1Name,"w") as a:
        a.write(data_b)

    with open(file2Name,"w") as b:
        b.write(data_a)

SwapFileData()
    
    


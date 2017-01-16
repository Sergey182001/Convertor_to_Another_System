do = "n"
while  do == "n" :
    try:
        do = "yn";
        index=1
        kk= True
        finish=[]
        finish1=[]
        
        intiv =int(input("Input number that you want to convert:"))
        m =int(input("Input convert type number[e.g. Binary=2] : "))
        count=-1
               
        while kk :
            count+=1
            index+=1
            finish.append(intiv % m)
            intiv = int(intiv / m)
            if intiv ==0 :
                kk= False
            
        
        kk=True
        print("Number in  "+str(m)+" system:",end = "")
        print("|",end = "")
        while kk :
        
            if m==16 :
                if finish[count] == 10:
                    finish1.append('A')
                    print(finish1[count],end = "");  
                elif finish[count] == 11:
                    finish1.append('B')
                    print(finish1[count],end = "")
                elif finish[count] == 12:
                    finish1.append('C')
                    print(finish1[count],end = "")
                elif finish[count] == 13:
                    finish1.append('D')
                    print(finish1[count],end = "")
                elif finish[count] == 14:
                    finish1.append('E')
                    print(finish1[count],end = "")
                elif finish[count] == 15:
                    finish1.append('F')
                    print(finish1[count],end = "")
                else:
                    print(finish[count],end = "")
                    
            else:
                print(finish[count],end = "")
            print("|",end = "")
            count-=1
            if count < 0:
                kk=False
                print() 
        while not do=="y" and not do=="n" :
            do = input("Do you want to go out(y/n):")
        del index
        del kk
        del finish
        del finish1
        del intiv
        del count
        del m
    except:
        del index
        del kk
        del finish
        del finish1
        del intiv
        del count
        del m
        print("Error")
        do = "n"
        
 

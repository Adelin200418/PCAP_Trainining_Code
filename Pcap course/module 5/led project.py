def led(num):
    for i in num:
        if i=="1":
            print('''
            
                # 
                #    
                #
                # 
                #  ''', end="")
        elif i=="2":
            print(""" 
                # # # 
                    #   
                # # #  
                #      
                # # #   """, end="")
        elif i=="3":
            print("""  
                # # # 
                    # 
                # # # 
                    #      
                # # # """, end="")
        elif i=="4":
            print(""" 
             #   #
             #   #
             # # # 
                 #
                 #  """, end="")
        elif i=="5":
            print(""" 
             # # #
             # 
             # # #
                 #
             # # #  """, end="")
        elif i=="6":
            print(""" 
             # # #
             # 
             # # #
             #   #
             # # # """, end="")
        elif i=="7":
            print(""" 
             # # #
                 #
                 # 
                 # 
                 #  """, end="")
        elif i=="8":
            print(""" 
             # # #
             #   #
             # # #
             #   #
             # # # """, end="")
        elif i=="9":
            print(""" 
             # # #
             #   #
             # # #
                 #
             # # # """, end="")
        else:
            return("it's not a number boss!")



numbr=input("Give me some numbers: ")
led(numbr)




def Print_A():
    c = '*'
    for row in range(0,6):
        for column in range(0,6):
            if(row == 0 and column == 2):
                print(c, end='')
            elif(row == 1 and (column == 1 or column == 3)):
                print(c, end='')
            elif(row == 2 and (column == 1 or column == 4)):
                print(c, end='')
            elif(row == 3 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                print(c, end='')
            elif(row == 4 and (column == 0 or column == 5)):
                print(c, end='')
            elif(row == 5 and (column == 0 or column == 5)):
                print(c, end='')
            else:
                print(' ', end='')
        print('\n')
    
     

def Print_N():
    c = '*'
    for row in range(0,6):
        for column in range(0,6):
            if(column == 0):
                print(c, end='')
            if(column == 5):
                print(c, end='')
            elif(row == column and (column != 0 or column != 3)):
                print(c, end='')
            else:
                print(' ', end='')
        print('\n')

def Print_E():
    c = '*'
    for column in range(0,5):
        for row in range(0,6):
            if(column == 0 or column == 2 or column == 4):
                print(c,end='')
            elif(row == 0):
                print(c,end='')
            else:
                print(' ', end='')
        print('\n')
        
            

        
if __name__=="__main__":
    Print_A()
    Print_N()
    Print_E()
    Print_K()
    
 

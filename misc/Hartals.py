#!/usr/bin/env python

def hartalCount(p,d):
    hartal_days = []
    for j in p:
        for i in range(d):
            i += 1
            if(i % j == 0 ):
                hartal_days.append(i)
                if(i%7 == 6 or i%7 == 0): #REMOVING HARTALS ON SATURDAY AND SUNDAY
                    hartal_days.pop()

    #REMOVING DUPLICATES OF MULTIPLES [ex: 2,3 both have multiple 6]
    hartal_days = list(dict.fromkeys(hartal_days))
    return hartal_days

if __name__ == "__main__":
    hartal_parameters =[3,4,8]
    hartal_parameters = list(dict.fromkeys(hartal_parameters)) #REMOVING DUPLICATES
    Days = 14
    Lost_Days = hartalCount(hartal_parameters, Days)
    print(len(Lost_Days))

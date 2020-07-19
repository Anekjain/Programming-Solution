#!/usr/bin/env python
'''
PROBLEM : GIVEN A BUNCH PF POINTS IN THE GRAPH WHICH MAKES TWO RECTANGLE.
WRITE ALGORITH TO SHOW THE OVERLAPPED AREA OF THE RECTANGLE IF EXSISTS.
'''

def Area_Overlapping(XY1,XY2,xy1,xy2):
        width = min(XY2[0],xy2[0])-max(XY1[0],xy1[0])
        if(width <= 0):
            return "DO NOT OVERLAP"

        length = min(XY2[1],xy2[1])-max(XY1[1],xy1[1])
        if(length <= 0):
            return "DO NOT OVERLAP"

        return length*width


if __name__=="__main__":
    R1x = [2,1]
    R1y = [5,5]
    R2x = [6,2]
    R2y = [5,7]

    Area = Area_Overlapping(R1x,R1y,R2x,R2y)
    print(Area)


def mergeSort(nlist):
    if len(nlist)>1:
        #Dividing the Array in Two Halfs
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        #Recursive Calls on Left and Right Half
        mergeSort(lefthalf)
        mergeSort(righthalf)

        
        #Sorting Two Lists using Two Pointer Approach
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        #Merging
        #Left Half Adding To List.    
        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1
        #Right Half Adding to List.
        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    
nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)

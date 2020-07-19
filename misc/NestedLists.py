if __name__ == '__main__':
    records = []
    names = []
    n = int(input("Size of List ?"))
    #TAKING NESTED INPUT FROM USER
    for i in range(n):
        name = input()
        score = float(input().strip())
        records.append([name, score])
    #SORTING NESTED LIST USING KEY     
    records.sort(key = lambda x:x[1])
    print(sorted(records, key= lambda x:x[0]))
    print(records)

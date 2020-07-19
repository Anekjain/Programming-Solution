def search_engine(query, pages):
    s = []
    query = query.split(" ")
    for i in pages: 
        for j in query:
            if j in pages[i].read():
                s.append(i)
                print(j, "found in", pages.get(i))
            
    if(s == None): print("No Pages Found")  
    return set(s)

if __name__=="__main__":
    query = "blogs videos"
    page1 = open("page1.txt")
    page2 = open("page2.txt")
    pages = {101:page1, 111:page2}  
    result = search_engine(query, pages)
    print(result)

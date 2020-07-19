class Process():
    #INITIALIZATION OF PROCESS
    def __init__(self, pid, state, resource):
        self.pid = pid
        self.state = state
        self.resource = resource
        self.deadlock = None

    # PRINT ALL PROCESS
    def get_process(self):
        print("PID", "STATE", "  ", "RESOURCE", "DEADLOCK STATUS")
        for proc in self.Process:
            if(proc.state == "Active"):
                print(proc.pid, proc.state, "  " ,list(proc.resource.values()), "  ", proc.deadlock)
            else:
                print(proc.pid, proc.state,"",list(proc.resource.values()), "  ", proc.deadlock)    
    #COUNT 
    def Count_Process(self, c, li):
        self.c = False
        for self.c in range(len(self.li)):
            if self.li.count(self.c[i]) > 1:
                self.c = True
            else:
                self.c = False
        return self.c
    # CHECK DEADLOCK        
    def OS_check_Deadlock(self):
        resource_in_use = []
        #GETTING ALL THE ACTIVE RESOURCES INTO A SET [MAX LIMIT OF RESOURCE = 2/PROCESS] 
        for proc in self.Process:
            if(proc.state == "Active"):
            #print(proc.state)
                for r in proc.resource:
                     #print(proc.resource.get(r)[0])
                     #print(proc.resource.get(r)[1])
                     resource_in_use.append(proc.resource.get(r)[0])
                     resource_in_use.append(proc.resource.get(r)[1])
        print(resource_in_use)
        #ALLOCATING DEADLOCK VARIABLE AS PER CONDITIONS:
        for proc in self.Process:
            if(proc.state == "Active"):
                for r in proc.resource:
                    cond1 = self.Count_Process(proc.resource.get(r)[0],resource_in_use)
                    cond2 = self.Count_Process(proc.resource.get(r)[1],resource_in_use)
                    if(cond1 and cond2):
                        print(resource_in_use, proc.deadlock)
                        proc.deadlock = "NO-DEADLOCK"
                    else:
                        proc.deadlock = "DEADLOCK"

    # DRIVER FUNCTION:
if __name__=="__main__":
      
        process = []
        #total_resources = [1,2,3,4,5]
        for i in range(1,6):
            process.append(Process(i,"Active",{i:[i,i+1]}))          

        process.append(Process(7,"Active",{7:[1,8]}))
        process.append(Process(8,"Active",{8:[9,10]}))        

        Process.OS_check_Deadlock()                  
        Process.get_process(process)

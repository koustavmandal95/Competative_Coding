class Job:
    def __init__(self,start,finish,profit):
        self.start=start
        self.finish=finish
        self.profit=profit
def schedule(job):
    job = sorted(job, key = lambda j: j.finish)
    n=len(job)
    inprofit=[0]*n
    for i in range(0,n):
        inprofit[i]=job[i].profit
    for i in range(1,n):
        for j in range(0,i):
            print(job[i].start)
            if job[i].start<=job[j].finish:
                inprofit[i]=inprofit[i]+job[j].profit
    return inprofit
if __name__=="__main__":
    job=[]
    N=int(input())
    for i in range(N):
        s,f,p=list(map(int,input().rstrip().split()))
        job.append(Job(s,f,p))
    # job = [Job(1, 2, 50), Job(3, 5, 20),  
    #       Job(6, 19, 100), Job(2, 100, 200)] 
    print("------------<<<--The output-->>------------------")
    print(schedule(job))
'''
4
2 100 200
6 19 100
3 5 20
1 2 50
'''
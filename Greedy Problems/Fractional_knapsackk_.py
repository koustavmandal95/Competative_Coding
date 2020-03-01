class Job:
    def __init__(self,available,cost,work):
        self.available=available
        self.cost=cost
        self.work=work
def minimum(job,D):
    job_a = sorted(job,key=lambda l:l.available)
    for i in range(len(job)):
        print(job_a[i].available,job_a[i].cost,job_a[i].work)
    job_c = sorted(job,key=lambda l:l.work/l.cost,reverse=True)
    W=D-job_a[0].work
    for i in range(len(job)):
        print(job_c[i].available,job_c[i].cost,job_c[i].work)
    for i in range(len(job)):
        for j in range(1,len(job)):
            if job_c[j].available<=job_a[i].available:
                if job_c[j-1].work

if __name__=="__main__":
    job=[]
    N,D=input().split()
    for i in range(int(N)):
        a,c,p=list(map(int,input().rstrip().split()))
        job.append(Job(a,c,p))
    # job = [Job(1, 2, 50), Job(3, 5, 20),  
    #       Job(6, 19, 100), Job(2, 100, 200)] 
    print(minimum(job,int(D)))
'''
3 3
1 1 1
2 2 2
3 1 5
'''
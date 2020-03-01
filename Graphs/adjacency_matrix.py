def print_all(edges,n,sv,visited):
    print(sv)
    visited[sv]=1
    for i in range(n):
        if i==sv:
            continue
        if edges[sv][i]==1:
            if visited[i]:
                continue
            print_all(edges,n,i,visited)
def print_bfs(edges,n,sv,visited):
    queue=[]
    queue.append(sv)
    visited[sv]=1
    while queue:
        cv=queue.pop(0)
        print(cv)
        for i in range(n):
            if i==cv:
                continue
            if edges[cv][i]==1 and visited[i]==0:
                queue.append(i)
                visited[i]=1
if __name__=="__main__":
    n=int(input())  # No. of vertices
    e=int(input())  # No. of edges
    edges=[[0 for i in range(n)]for i in range(n)]
    for i in range(e):
        f,s=list(map(int,input().rstrip().split()))
        edges[f][s]=1
        edges[s][f]=1
    visited=[0]*n
    # print_all(edges,n,0,visited)
    print_bfs(edges,n,0,visited)
'''
8
9
0 4
0 5
4 3
3 2
2 1
1 3
5 6
3 6
6 7
'''
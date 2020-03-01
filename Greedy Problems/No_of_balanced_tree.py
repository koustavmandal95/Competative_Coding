prime=1000000007
def binary_tree(h):
    if h in (0,1):
        return 1
    x=binary_tree(h-1)
    y=binary_tree(h-2)
    ans=(x*x+2*x*y)%prime
    return ans
h=int(input())
print(binary_tree(h))
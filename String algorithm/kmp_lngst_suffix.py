def compute_kmp_fail(T):
    m=len(T)
    fail=[0]*m
    i=1
    j=0
    while i<m:
        if T[j]==T[i]:
            fail[i]=j+1
            j=j+1
            i=i+1
        elif j>0:
            j=fail[j-1]
        else:
            i=i+1
    return fail
def kmpsearch(text,pattern):
    l_pattern=len(pattern)
    l_text=len(text)
    i=0
    j=0
    fail=compute_kmp_fail(pattern)
    while i < l_text and j <l_pattern:
        if text[i]==pattern[j]:
            i=i+1
            j=j+1
        else:
            if j>0:
                j=fail[j-1]
            else:
                i=i+1
    if j==l_pattern:
        if pattern in text:
            c=text[]
    else:
        return False
if __name__=="__main__":
    text=input()
    pattern=input()
    print(kmpsearch(text,pattern))
    
# adadabadadadabadadad

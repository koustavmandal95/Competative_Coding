#include<iostream>
using namespace std;
int* lis(int n, int* arr){
    int* out1 = new int[n];
    out1[0]=1;
    for(int i=1;i<n;i++){
        out1[i]=1;
        for(int j=i-1;j>=0;j--){
            if(arr[j]>=arr[i])
                continue;
            int temp=out1[j]+1;
            if(temp>out1[i])
                out1[i]=temp;
        }
    }
 //    for(int i=0;i<n;i++)
	// 	cout<<out1[i]<<' ';
	// cout<<endl;
    return out1;
}

int* lis_b(int n, int* arr){
	int* out = new int[n];
	out[n-1]=1;
	for(int i=n-2;i>=0;i--){
		out[i]=1;
		for(int j=i+1;j<n;j++){
			if(arr[j]>=arr[i])
				continue;
			int temp=out[j]+1;
			if(temp>out[i])
				out[i]=temp;
		}
	}
	// for(int i=0;i<n;i++)
	// 	cout<<out[i]<<' ';
	// cout<<endl;
	return out;
} 	
	
int longestBitonicSubarray(int *input, int n) {
		
	
     	int* lis_ = lis(n, input);
    int* dis_ = lis_b(n, input);
    int res=0;
    for(int i=0;i<n;i++){
    	int temp = lis_[i]+dis_[i]-1;
    	if(temp>res)
    		res=temp;

    }
    return res;
     	
 	}
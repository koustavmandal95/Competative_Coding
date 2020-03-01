#define mod 1000000007
int balancedBTs(int h) {
  /* Don't write main().
     Don't read input, it is passed as function argument.
     Return the output and don’t print it.
  */
    if(h == 0 || h==1){
		return (1);
	}
	long long int ans1 = (balancedBTs(h-1))% mod;
	long long int ans  = (balancedBTs(h-2))% mod;
	return (int)((ans1 * ans1)% mod + (2*(ans * ans1))%mod) % mod;

}

21-10-19 20:17

kishan kunal

try to 
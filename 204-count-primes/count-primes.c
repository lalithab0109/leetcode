#include <math.h>
int countPrimes(int n) {
    if(n<=1)return 0;
    int *prime;
    prime=(int*)malloc(sizeof(int)*n);
    for(int i=0;i<n;i++){
        if(i<=1)prime[i]=0;
        else prime[i]=1;
    }
    int cp;
    int sqrtn=(int)(sqrt(n)+1);
    for(int i=2;i<sqrtn;i++){
        if(prime[i]==0)continue;
        cp=i;
        for(int j=2*cp;j<n;j=j+cp){
            prime[j]=0;
        }
    }
    int count=0;
    for(int i=0;i<n;i++){
        if(prime[i]==1)count++;
    }
    return count;
}
#include <math.h>
int smallestNumber(int n) {
    int totdigits=0;
    while(n>0){
        n=n/2;
        totdigits++;
    }
    int num=0;
    for(int i=1;i<pow(2,totdigits);i*=2){
        num+=i;
    }
    return num;

    
}
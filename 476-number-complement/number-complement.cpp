class Solution {
public:
    int findComplement(int num) {
        int n=0;
        int num_org=num;
        while(num>0){
            n++;
            num=num/2;
        }
        long long x=1;
        for(int i=1;i<=n;i++){
            x*=2;
        }
        x=x-1;
        num=num_org;
        return num^x;
    }
};
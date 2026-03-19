class Solution {
public:
    int bitwiseComplement(int n) {
        int total_digits=0;
        int num_org=n;
        if(n==0) return(1);
        while(n>0){
            total_digits+=1;
            n=n/2;
        }
        int num=0;
        for(int i=0;i<total_digits;i++){
            num+=pow(2,i);
        }
        int comp=num^num_org;
        return comp;
    }
};
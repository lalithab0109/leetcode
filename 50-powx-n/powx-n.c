double myPow(double x, int n) {
    if(n>0){
        double prod=1;
        double prodseq=x;
        while(n>0){
            if(n&1){
                prod*=prodseq;
            }
            n=n/2;
            prodseq*=prodseq;
        }
        return prod;
    }
    else if(n<0){
        long int m=(long int)n;
        m=labs(m);
        double prod=1;
        double prodseq=1/x;
        while(m>0){
            if(m&1){
                prod*=prodseq;
            }
            m=m/2;
            prodseq*=prodseq;
        }
        return prod;
    }
    else{
        return 1;
    }
}
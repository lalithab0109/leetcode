int mySqrt(int x) {
    double r1,r2;
    r1=x/2.0;
    r2=r1;
    double e=0.005;
    if(x==0){
        return 0;
    }
    else{
        do{
            r1=r2;
            r2=(r1+x/r1)/2;
        }while(fabs(r1-r2)>e);
    }
    return (int)r2;
}
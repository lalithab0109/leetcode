int fib(int n){
    int n1,n2,n3;
    n1=0;
    n2=1;
    if(n==0){
        return n1;
    }
    else if(n==1){
        return n2;
    }
    else{
    for (int i=2;i<=n;i++){
        n3=n1+n2;
        n1=n2;
        n2=n3;
       
    }
    return n3;
    }


}
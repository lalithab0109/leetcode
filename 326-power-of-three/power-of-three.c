bool isPowerOfThree(int n) {
    double num=(double)n;
    while(num>1){
        num=num/3;
    }
    if(num==1){
        return true; 
    }
    else{
        return false;
    }
    
}
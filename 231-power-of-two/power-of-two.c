bool isPowerOfTwo(int n) {
    double num=(double)n;
    while(num>1){
        num=num/2;
    }
    if(num==1){
        return true; 
    }
    else{
        return false;
    }
  
}
bool isPerfectSquare(int num) {
    float r1=((float)num)/2;
    float r2=((float)num)/2;
    float e=0.001;
    
    do{
        r1=r2;
        r2=((r1 + num/r1)/2);
    }while(fabs(r1-r2)>e);
    if(round(r2)*round(r2)==num) return true;
    else return false;
    
}
int addDigits(int num) {
    int sum;
    
    while(num>9){
        sum=0;
        while(num>0){
            int digit=num%10;
            sum+=digit;
            num=num/10;
        }
        num=sum;

    }
    return num;
    
}
class Solution {
public:
    int sum_of_sq_of_digits(int n){
        int digit;
        int sum=0;
         while(n>0){
            digit=n%10;
            sum+=digit*digit;
            n=n/10;
        }
        return sum;
    }
    bool isHappy(int n) {
        int count=0;
        while(n>1){
            n=sum_of_sq_of_digits(n);
            count++;
            if(count>100) return false;
        }
        return true;
    }
};
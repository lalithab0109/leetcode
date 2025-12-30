class Solution {
public:
    bool hasAlternatingBits(int n) {
        int bit;
        int prev_bit=n%2;
        n=n/2;
        while(n>0){
            bit=n%2;
            if(prev_bit==bit) return false;
            prev_bit=bit;
            n=n/2;
        }
        return true;
    }
};
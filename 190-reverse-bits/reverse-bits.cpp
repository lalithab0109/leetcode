class Solution {
public:
    int reverseBits(int n) {
        int rev_num=0;
        int digit=0;
        int count_bits=0;
        while(count_bits<32){
            digit=n%2;
            count_bits++;
            rev_num=rev_num*2+digit;
            n=n/2;
        }
        return rev_num;
    }
};
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int n=nums.size();
        int x=0;
       for(int i=0;i<n;i++){
        x=x^nums[i];
       }
       unsigned int k = (unsigned int)x & (-(unsigned int)x);
       int a=0;
       int b=0;
       for(int i=0;i<n;i++){
        if((nums[i]&k)!=0){
            a=a^nums[i];
        }
        else{
             b=b^nums[i];
        }
       }
       return {a,b};
    }
};
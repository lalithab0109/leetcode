class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int len=1;
        int l=0;
        int r;
        for(int i=1;i<nums.size();i++){
            if(nums[i]<=nums[i-1]){
                r=i-1;
                len=max(len,r-l+1);
                l=i;
            }
        }
        r=nums.size()-1;
        len=max(len,r-l+1);
        return len;
        
    }
};
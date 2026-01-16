class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n=nums.size();
        int max=nums[0];
        for(int i=0;i<n;i++){
            if(nums[i]>max) max=nums[i];
        }
        vector<int> count(max+1);
        for(int i=0;i<n;i++){
            count[nums[i]]+=1;
        }
        int rep=0;
        for(int i=0;i<max+1;i++){
            if(count[i]>count[rep]) rep=i;
        }
        return rep;
    }
};
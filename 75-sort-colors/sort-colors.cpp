class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n=nums.size();
        vector<int> count(3);
        for(int i=0;i<n;i++){
            if(nums[i]==0) count[0]++;
            else if(nums[i]==1) count[1]++;
            else count[2]++;
        }
        int index=0;
        for(int i=0;i<3;i++){
            for(int j=0;j<count[i];j++){
                nums[index]=i;
                index++;
            }
        }
    }
};
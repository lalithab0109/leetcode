class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n=nums.size();
        int psize=(1<<n);
        vector<vector<int>> output;
        for(int i=0;i<psize;i++){
            vector<int> temp;
            for(int j=0;j<n;j++){
                if((i&(1<<j))!=0) temp.push_back(nums[j]);
            }
            output.push_back(temp);
        }
        return output;
        
    }
};
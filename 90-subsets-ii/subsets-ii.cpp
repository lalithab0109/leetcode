class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int psize=(1<<n);
        vector<vector<int>> output;
        vector<vector<int>> output_final;
        for(int i=0;i<psize;i++){
            vector<int> temp;
            for(int j=0;j<n;j++){
                if((i&(1<<j))!=0) temp.push_back(nums[j]);
            }
            output.push_back(temp);
        }
        sort(output.begin(),output.end());
        output_final.push_back(output[0]);
        for(int i=1;i<output.size();i++){
            if(output[i]!=output[i-1])output_final.push_back(output[i]);
        }
        return output_final;
    }
};
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n=nums.size();
        vector<int> missing_nums;
        vector<int> count(n);
        for(int i=0;i<n;i++){
            count[i]=0;
        }
        for(int i=0;i<n;i++){
            count[nums[i]-1]+=1;
        }
        for(int i=0;i<n;i++){
            if(count[i]==0){
                missing_nums.push_back(i+1);
            }
        }
        return missing_nums;
        
    }
};
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n=nums.size();
       vector<int> a(n);
       for(int i=0;i<n;i++){
        a[nums[i]-1]+=1;
       }
       vector<int> ans;
       for(int i=0;i<n;i++){
        if(a[i]==2){
            ans.push_back(i+1);
        }
       }
       for(int i=0;i<n;i++){
        if(a[i]==0){
            ans.push_back(i+1);
        }
       }
       return ans; 
    }
};
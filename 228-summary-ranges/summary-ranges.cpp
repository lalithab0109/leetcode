class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> output;
        if(nums.size()==0){
            return output;
        }
        int start=nums[0];
        int end;
        for(int i=1;i<nums.size();i++){
            if(nums[i]!=nums[i-1]+1){
                end=nums[i-1];
                if(start!=end){
                    output.push_back(to_string(start)+"->"+to_string(end));
                }
                else{
                    output.push_back(to_string(start));
                }
                start=nums[i];
                
            }                             
        }
        end=nums[nums.size()-1];
        if(start!=end){
            output.push_back(to_string(start)+"->"+to_string(end));
        }
        else{
            output.push_back(to_string(start));
        }
        return output;
    }
};
class Solution {
public:
    string addBinary(string a, string b) {
        int carry=0;
        string ans="";
        int len=max(a.length(),b.length());
        if(a.length()<len){
            a=string(len-a.length(),'0')+a;
        }
        if(b.length()<len){
            b=string(len-b.length(),'0')+b;
        }
        cout<<a<<endl;
        cout<<b;
        for(int i=len-1;i>=0;i--){
            if((a[i]-'0')+(b[i]-'0')+carry==3){
                carry=1;
                ans.insert(ans.begin(),'1');
            }
            else if((a[i]-'0')+(b[i]-'0')+carry==2){
                carry=1;
                ans.insert(ans.begin(),'0');
            }
            else if((a[i]-'0')+(b[i]-'0')+carry==1){
                carry=0;
                ans.insert(ans.begin(),'1');
            }
            else if((a[i]-'0')+(b[i]-'0')+carry==0){
                carry=0;
                ans.insert(ans.begin(),'0');
            }
        }
        if(carry!=0) ans.insert(ans.begin(),'1');
        return ans;
    }
};
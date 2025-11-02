bool checkIfExist(int* arr, int arrSize) {
    int ele=0;
    for(int i=0;i<arrSize;i++){
        ele=arr[i];
        for(int j=0;j<arrSize;j++){
            if(arr[j]==2*arr[i] && i!=j){
                return true;
            }

        }
    }
    return false;
    
}
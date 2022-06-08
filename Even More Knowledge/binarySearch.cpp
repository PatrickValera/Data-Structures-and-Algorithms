#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binary_search(nums,0,nums.size()-1,target);
    }
    int binary_search(vector<int>& nums, int start, int end, int target){
        if(end>=start){
            int mid=start+(end-start)/2;
            if(nums[mid]==target)return mid;
            if(nums[mid]>target) return binary_search(nums,start,mid-1,target);
            else return binary_search(nums,mid+1,end,target);
        }
        return -1;
    }
};

int main(){
    Solution s;
    vector<int> vec = {1,2,3,4,5,6,7};
    cout<<s.search(vec,7);

}
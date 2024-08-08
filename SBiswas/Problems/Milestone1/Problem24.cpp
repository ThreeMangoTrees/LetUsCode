#include<iostream>
#include<vector>

using namespace std;


//  Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 
class Solution {
public:
    TreeNode* treeBuilder(int left, int right, vector<int>& nums)
    {
        if(left>right)
        {
            return nullptr;
        }

        int mid = (left+right)/2;

        TreeNode* temp = new TreeNode(nums[mid]);
        temp->left = treeBuilder(left, mid-1, nums);
        temp->right = treeBuilder(mid+1, right, nums);

        return temp;
    }
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int left=0, right = nums.size()-1;
        TreeNode* root = treeBuilder(left, right, nums);

        return root;
    }   
};
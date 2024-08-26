#include<iostream>
#include<vector>
#include<unordered_map>

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

    TreeNode* treeBuilder(vector<int>& nums, int left, int right)
    {
        if(left > right)
        {
            return nullptr;
        }

        int mid = (left + right)/2;

        TreeNode* root = new TreeNode(nums[mid]);
        root->right = treeBuilder(nums, mid+1, right);
        root->left = treeBuilder(nums, left, mid-1);

        return root;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int size = nums.size();

        int left = 0;
        int right = size-1;

        TreeNode* root = treeBuilder(nums, left, right);

        return root;

    }
};
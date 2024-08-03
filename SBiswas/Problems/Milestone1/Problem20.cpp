/* 
    Problem 20: Range Sum of BST
*/

#include<iostream>
#include<vector>
#include<limits.h>

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

    void helper(TreeNode* root, int& low, int& high, int& sum)
    {
        if(!root)
        {
            return;
        }
        
        helper(root->left, low, high, sum);
        if(root->val<=high && root->val>=low)
        {
            sum += root->val;
        }
        helper(root->right, low, high, sum);

    }

    int rangeSumBST(TreeNode* root, int low, int high) {
        int ans =0;

        helper(root, low, high, ans);

        return ans;
    }
};
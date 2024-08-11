/* 
    Problem 19: Diameter of a binary tree
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
    int max_depth(TreeNode* root, int& diameter)
    {
        if(!root)
        {
            return 0;
        }
        int l_depth = max_depth(root->left, diameter);
        int r_depth = max_depth(root->right, diameter);

        diameter = max(diameter, l_depth+r_depth);

        return 1 + max(l_depth, r_depth);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter=0;
        max_depth(root, diameter);

        return diameter;
    }
};
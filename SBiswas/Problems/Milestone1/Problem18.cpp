/* 
    Problem 18: Minimum Absolute Difference in BST
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
    void inorder(TreeNode* root, vector<int>& nodes)
    {
        if(!root)
        {
            return;
        }

        inorder(root->left,nodes);
        nodes.push_back(root->val);
        inorder(root->right, nodes);

    }
    int getMinimumDifference(TreeNode* root) {

        vector<int> nodes;
        inorder(root, nodes);

        int len = nodes.size();

        if(len == 2)
        {
            return abs(nodes[1]-nodes[0]);
        }

        int min_val = INT_MAX;
        
        for(int i=1; i<len; i++)
        {
            min_val = min(min_val, nodes[i]-nodes[i-1]);
        }

        return min_val;
    }
};
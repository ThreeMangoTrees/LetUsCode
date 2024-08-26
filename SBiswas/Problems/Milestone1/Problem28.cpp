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

    TreeNode* temp = new TreeNode;
    TreeNode* ans = temp;
    TreeNode* last_val_node = nullptr;
public:

    void inorder(TreeNode* root)
    {
        if(!root)
        {
            return;
        }

        inorder(root->left);
        last_val_node = temp;
        temp->val = root->val;
        temp->right = new TreeNode;
        temp = temp->right;
        inorder(root->right);
    }

    TreeNode* increasingBST(TreeNode* root) {
        
        inorder(root);
        last_val_node->right = nullptr;
        return ans;
    }
};
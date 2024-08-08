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
    TreeNode* ans = nullptr;
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        bool done = false;

        inorder(original, cloned, target, done);

        return ans;
    }

    void inorder(TreeNode* root, TreeNode* clone_root, TreeNode* target, bool& done)
    {   
        if(done)
        {
            return;
        }

        if(!root)
        {
            return;
        }

        inorder(root->left, clone_root->left, target, done);
        if(root == target)
        {
            // clone_root is the answer
            done = true;
            ans = clone_root;
        }
        inorder(root->right, clone_root->right, target, done);
    }
};
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
    unordered_map<int, pair<TreeNode*,int>> node_info;
public:
    void find_depth(TreeNode* root, TreeNode* parent, int depth)
    {
        if(!root)
        {
            return;
        }

        find_depth(root->left, root, depth+1);
        
        auto a = make_pair(parent,depth);
        node_info[root->val] = a;
        // node_info[root->val].first = 

        find_depth(root->right, root, depth+1);
    }
    bool isCousins(TreeNode* root, int x, int y) {
        
        TreeNode* dummy_parent = nullptr;

        find_depth(root, dummy_parent, 0);

        return ((node_info[x].first != node_info[y].first) && (node_info[x].second == node_info[y].second));
    }
};
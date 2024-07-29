/* Mode of BST tree*/

#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;

class TreeNode {
    
    public:
    int data;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int val)
    {
        data = val;
        left = nullptr;
        right = nullptr;
    }
    
};

class Solution {
public:
    void inorder(TreeNode* root, unordered_map<int,int>& node_count)
    {
        if(!root)
        {
            return;
        }

        inorder(root->left, node_count);

        if(node_count.find(root->data) == node_count.end())
        {
            node_count[root->data] = 0;
        }
        node_count[root->data] += 1;

        inorder(root->right, node_count);

    }
    vector<int> findMode(TreeNode* root) {
        
        unordered_map<int,int> node_count;
        inorder(root, node_count);

        vector<int> ans;
        int max_freq=0;
        for(auto i : node_count)
        {
            max_freq = max(max_freq, i.second);
        }

        for(auto i : node_count)
        {
            if(i.second == max_freq)
            {
                ans.push_back(i.first);
            }
        }

        return ans;
    }
};
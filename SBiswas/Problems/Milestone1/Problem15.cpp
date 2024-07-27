/* 110. Balanced Binary Tree*/

class TreeNode {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
public:
    bool isBalanced(TreeNode* root) {
        
        if(getHeight(root)==-1)
        {
            return false;
        }

        return true;
    }

    int getHeight(TreeNode* root)
    {   
        if(!root)
        {
            return 0;
        }

        int left_subtree_height = getHeight(root->left); // get left subtree height
        int right_subtree_height = getHeight(root->right); // get right subtree height
        
        if(left_subtree_height == -1 || right_subtree_height == -1) // if either of the heights are -1 then return -1
        {
            return -1;
        }

        if(abs(left_subtree_height-right_subtree_height)>1) // check if the height diff between left and right is greater than 1.
        {
            return -1;
        }

        return max(left_subtree_height,right_subtree_height)+1; // return the height of the current subtree with root as root_node.
        
    }
};
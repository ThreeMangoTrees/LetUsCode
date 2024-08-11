/* Average of levels of a binary tree*/

#include <iostream>
#include <vector>
#include <queue>


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
    vector<double> averageOfLevels(TreeNode* root) {

        queue<TreeNode*> curr_level;
        queue<TreeNode*> next_level;

        vector<double> ans;

        next_level.push(root);
        ans.push_back((double)root->data);


        while(!next_level.empty())
        {
            curr_level = next_level;
            queue<TreeNode*> temp;
            next_level = temp;

            while(!curr_level.empty())
            {
                TreeNode* top = curr_level.front();
                curr_level.pop();

                if(top->left!=nullptr)
                {
                    next_level.push(top->left);
                }

                if(top->right!=nullptr)
                {
                    next_level.push(top->right);
                }
            }

            double sum = 0;
            double count=0;

            if(!next_level.empty())
            {
                temp = next_level;
                while(!temp.empty())
                {
                    sum+= (double)temp.front()->data;
                    count++;
                    temp.pop();
                }
                ans.push_back(sum/count);
            }

        }

        return ans;
        
    }
};
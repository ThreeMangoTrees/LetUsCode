#include<iostream>
#include<vector>
#include <algorithm>
#include<stack>
using namespace std;

class Node {
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
    vector<int> ans;
    stack<Node*> my_stack;
public:
    /* pre order helper for recursive solution*/
    void helper_prorder(Node* root)
    {
        if(!root)
        {
            return;
        }
        
        int num_child = root->children.size();
        cout<<root->val<<" ";
        ans.push_back(root->val);
        for(int i=0; i<num_child; i++)
        {
            
            helper_prorder(root->children[i]);
        }
    }

    /* Pre order Iterative*/
    void helper_preorder_iterative(Node* root)
    {
        if(!root)
        {
            return;
        }

        my_stack.push(root);

        while(!my_stack.empty())
        {
            Node* curr_top = my_stack.top();
            ans.push_back(curr_top->val);
            my_stack.pop();

            for (auto it = curr_top->children.rbegin(); it != curr_top->children.rend(); ++it) { 
                my_stack.push(*it);
            } 
        }

    }


    /* post order helper for recursive solution*/
    void helper_postorder(Node* root)
    {  
        if(!root)
        {
            return;
        }
        
        int num_child = root->children.size();
        for(int i=0; i<num_child; i++)
        {
            
            helper_postorder(root->children[i]);
        }
        cout<<root->val<<" ";
        ans.push_back(root->val);
    }

    void helper_postorder_iterative(Node* root)
    {
        if(!root)
        {
            return;
        }

        my_stack.push(root);

        while(!my_stack.empty())
        {
            Node* curr_top = my_stack.top();
            my_stack.pop();
            ans.push_back(curr_top->val);

            for (auto it = curr_top->children.begin(); it != curr_top->children.end(); ++it) { 
                my_stack.push(*it);
            } 
        }
        reverse(ans.begin(), ans.end());

    }

    // Postorder Recursive solution
    vector<int> postorder(Node* root) {
        helper_postorder(root);
        // helper_postorder_iterative(root);
        return ans; 
    }

    // Preorder Recursive solution
    vector<int> preorder(Node* root) {
        helper_prorder(root);
        // helper_preorder_iterative(root);
        return ans;       
    }
};

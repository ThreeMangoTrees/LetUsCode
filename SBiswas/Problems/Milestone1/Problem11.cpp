#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
/*
    TODO: Modularize the code. For example build a different header file 
    with class Node and Class BST for binary search tree.

    Inorder traversal on binary tree, Iterative way
*/
using namespace std;

class Node {
    
    public:
    int data;
    Node* left;
    Node* right;
    
    Node(int val)
    {
        data = val;
        left = nullptr;
        right = nullptr;
    }
    
};

stack<Node*> my_stack;

Node* insert_in_BST(Node* root, int val)
{   
    /*
    Insert Function for Binary Search Tree
    */

   if(root == nullptr)
   {
        Node* temp = new Node(val);
        return temp;
   }

    if(val > root->data)
    {
        // Go to right of the root
        root->right = insert_in_BST(root->right,val);
    }
    else if (val < root->data)
    {
        // Go to left of the root
        root->left = insert_in_BST(root->left,val);
    }    
    
    return root;
}

void left_most(Node* root)
{
    while(root)
    {   
        my_stack.push(root);
        root=root->left;
    }
}

void inorderTraversal(Node* root)
{   
    /*
        Iterative Inorder tree traversal
    */
    left_most(root);

    while (!my_stack.empty())
    {
        Node* curr_root = my_stack.top();
        my_stack.pop();

        if(curr_root->right)
        {
            left_most(curr_root->right);
        }
        cout<<curr_root->data<<" ";

    }
    
}

void left_most_preorder(Node* root)
{
    while(root)
    {   
        cout<<root->data<<" ";
        my_stack.push(root);
        root=root->left;
    }
}

void preorderTraversal(Node* root)
{   
    /*
        Iterative Preorder tree traversal
    */
    left_most_preorder(root);

    while (!my_stack.empty())
    {
        Node* curr_root = my_stack.top();
        my_stack.pop();

        if(curr_root->right)
        {
            left_most_preorder(curr_root->right);
        }
        // cout<<curr_root->data<<" ";

    }
    
}

void postorderTraversal(Node* root)
{   
    if(!root)
    {
        cout<<"Tree is empty";
    }
    vector<int> ans;

    stack<Node*> postorder_stack;
    postorder_stack.push(root);

    while(!postorder_stack.empty())
    {
        Node* curr_top = postorder_stack.top();
        postorder_stack.pop();
        ans.push_back(curr_top->data);

        if(curr_top->right)
        {
            postorder_stack.push(curr_top->right);
        }

        if(curr_top->left)
        {
            postorder_stack.push(curr_top->left);
        }
    }

    reverse(ans.begin(), ans.end());
    for(int& i : ans)
    {
        cout<<i<<" ";
    }
}

int main()
{
    // Node values for BST
    std::vector<int> nodes = {20, 10, 30, 5, 15, 25, 35, 40, 50, 100};

    Node* tree = nullptr;
    
    // Create Trees 1 and 2 (they have same nodes)
    for(int & val : nodes)
    {
        tree = insert_in_BST(tree,val);
    }

    cout<<"Inorder Traversal: ";
    preorderTraversal(tree);
    cout<<"\n";
    postorderTraversal(tree);
    cout<<"\n";

    
    return 0;
}
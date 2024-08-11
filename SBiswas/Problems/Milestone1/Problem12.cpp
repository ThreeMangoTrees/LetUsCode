#include <iostream>
#include <vector>
#include <stack>
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


Node* recursion(Node* root, int val)
{
    if(!root)
    {
        return nullptr;
    }

    if(val == root->data)
    {
        return root;
    }
    else if(val > root->data)
    {
        return recursion(root->right, val);
    }
    else
    {
        return recursion(root->left, val);
    }
}

Node* searchBST(Node* root, int val) {
    Node* ans = nullptr;
    ans = recursion(root, val);
    return ans;
}

void inorder(Node* root)
{
    if(!root)
    {
        return;
    }

    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
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

    Node* sub_tree = searchBST(tree, 30);
    cout<<"Inorder subtree Traversal: ";
    inorder(sub_tree);
    cout<<"\n";

    sub_tree = searchBST(tree, 2);
    cout<<"Inorder subtree Traversal: ";
    inorder(sub_tree);
    cout<<"\n";
    
    return 0;
}
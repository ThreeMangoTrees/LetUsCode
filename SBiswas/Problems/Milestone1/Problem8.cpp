#include <iostream>
#include <vector>
/*
    TODO: Modularize the code. For example build a different header file 
    with class Node and Class BST for binary search tree.
*/

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


void sum_left_leaves(Node* root, int& sum)
    {
        if(!root)
        {
            return ;
        }

        if(root->left && !root->left->left && !root->left->right)
        {
            sum+=root->left->data;
        }

        sum_left_leaves(root->left,sum);
        sum_left_leaves(root->right,sum);
        
    }

int main()
{
    // Node values for BST
    std::vector<int> nodes = {20, 10, 30, 70};

    Node* tree = nullptr;
    
    // Create Trees 1 and 2 (they have same nodes)
    for(int & val : nodes)
    {
        tree = insert_in_BST(tree,val);
    }

    int sum = 0;
    sum_left_leaves(tree,sum);

    std::cout<<"Sum of Left Leaves= "<<sum<<'\n';

    
    return 0;
}
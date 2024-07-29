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

bool hasPathSum(Node* root, int targetSum) {

        if(!root)
        {
            return false;
        }

        if(root->left == nullptr && root->right == nullptr)
        { // leaf node
            if(targetSum-root->data == 0){
                return true;
            }
            else
            {
                return false;
            }
        }
        return hasPathSum(root->left, targetSum-root->data) || hasPathSum(root->right, targetSum-root->data);
 
    }

int main()
{
    // Node values for BST
    std::vector<int> nodes = {20, 10, 30, 5, 15, 25};

    Node* tree = nullptr;
    
    // Create Trees 1 and 2 (they have same nodes)
    for(int & val : nodes)
    {
        tree = insert_in_BST(tree,val);
    }

    std::cout<<"Tree has sum path = 35: "<<hasPathSum(tree,35)<<'\n';
    std::cout<<"Tree has sum path = 30: "<<hasPathSum(tree,30)<<'\n';
    
    return 0;
}
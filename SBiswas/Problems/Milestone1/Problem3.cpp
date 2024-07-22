#include <iostream>

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

void preorder(Node* root)
{
    if(root == nullptr)
    {
        return;
    }
    
    std::cout<<root->data<<" - ";
    preorder(root->left);
    preorder(root->right);
}

void postorder(Node* root)
{
    if(root == nullptr)
    {
        return;
    }
    
    postorder(root->left);
    postorder(root->right);
    std::cout<<root->data<<" - ";
}

void inorder(Node* root)
{
    if(root == nullptr)
    {
        return;
    }
    
    inorder(root->left);
    std::cout<<root->data<<" - ";
    inorder(root->right);
}


int main()
{
    Node* my_tree = nullptr; 
    
    // insert(my_tree,1);
    my_tree = insert_in_BST(my_tree,5);
    my_tree = insert_in_BST(my_tree,6);
    my_tree = insert_in_BST(my_tree,7);
    
    my_tree = insert_in_BST(my_tree,1);
    my_tree = insert_in_BST(my_tree,9);

    my_tree = insert_in_BST(my_tree,4);
    my_tree = insert_in_BST(my_tree,0);
    my_tree = insert_in_BST(my_tree,8);
    
    std::cout<<"Inorder Traversal: \n";
    inorder(my_tree);
    std::cout<<'\n';
    std::cout<<"Preorder Traversal: \n";
    preorder(my_tree);
    std::cout<<'\n';
    std::cout<<"Postorder Traversal: \n";
    postorder(my_tree);
    std::cout<<'\n';
    std::cout<<"Inorder Traversal outputs the nodes in ascending order.\n";
    
    return 0;
}


#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

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

bool isSameTree(Node* p, Node* q) {

    if(p== nullptr && q==nullptr )
    {
        return true;
    }

    if(p== nullptr || q==nullptr )
    {
        return false;
    }

    if(p->data != q->data)
    {
        return false;
    }

    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    
}

int main()
{
    // Both trees have Same Nodes
    std::vector<int> nodes_11 = {20, 10, 30, 5, 15, 25, 35};
    std::vector<int> nodes_12 = {20, 10, 30, 5, 15, 25, 35};
    
    // Both Trees have different Nodes
    std::vector<int> nodes_21 = {20, 10, 30, 5, 15, 25, 35};
    std::vector<int> nodes_22 = {20, 10, 30, 5, 15, 25, 100};

    

    Node* tree_1 = nullptr;
    Node* tree_2 = nullptr;
    Node* tree_3 = nullptr;
    
    // Create Trees 1 and 2 (they have same nodes)
    for(int & val : nodes_11)
    {
        tree_1 = insert_in_BST(tree_1,val);
        tree_2 = insert_in_BST(tree_2,val);
    }

    // Create Tree 3 
    for(int & val : nodes_22)
    {
        tree_3 = insert_in_BST(tree_3,val);
    }

    std::string ans = isSameTree(tree_1,tree_2) ? "YES":"NO";
    std::cout<<"tree_1 and tree_2: "<<ans<<'\n';

    ans = isSameTree(tree_1,tree_3) ? "YES":"NO";
    std::cout<<"tree_1 and tree_3: "<<ans<<'\n';

    
    return 0;
}


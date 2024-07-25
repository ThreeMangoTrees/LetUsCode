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

Node* insert(int val)
{
    Node* temp = new Node(val);
    return temp;
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

bool isSymmetricTree(Node* p, Node* q) {

    if(p== nullptr && q==nullptr )
    {
        return true;
    }

    if(p == nullptr || q ==nullptr )
    {
        return false;
    }

    if(p->data != q->data)
    {
        return false;
    }

    // Check if current Node's data in p and q are equal, also check symmetry, p->left and q->right followed by p->right and q->left
    return p->data == q->data && isSymmetricTree(p->left, q->right) && isSymmetricTree(p->right, q->left);
    
}

int main()
{

    Node* tree_1 = new Node(1); 
    Node* tree_2 = new Node(1);

    // Symmetric tree
    tree_1->left = insert(2);
    tree_1->right = insert(2);
    tree_1->left->left = insert(3);
    tree_1->left->right = insert(4);
    tree_1->right->left = insert(4);
    tree_1->right->right = insert(3);

    // Non Symmetric Tree
    tree_2->left = insert(2);
    tree_2->right = insert(2);
    tree_2->left->right = insert(3);
    tree_2->right->right = insert(3);


    std::string ans = isSymmetricTree(tree_1,tree_1) ? "SYMMETRIC":"NOT SYMMETRIC";
    std::cout<<"tree_1 is: "<<ans<<'\n';

    ans = isSymmetricTree(tree_2,tree_2) ? "SYMMETRIC":"NOT SYMMETRIC";
    std::cout<<"tree_2 is: "<<ans<<'\n';

    
    return 0;
}


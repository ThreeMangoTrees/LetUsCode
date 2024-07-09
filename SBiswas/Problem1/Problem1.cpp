#include <iostream>

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
    std::cout<<"insert: "<<val<<'\n';
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

int main()
{
    std::cout<<"Hello World\n";
    Node* my_tree = new Node(1);
    
    // insert(my_tree,1);
    my_tree->left = insert(2);
    my_tree->right = insert(3);
    
    my_tree->left->left = insert(4);
    my_tree->left->right = insert(5);
    
    my_tree->right->left = insert(6);
    my_tree->right->right = insert(7);
    
    
    inorder(my_tree);

    return 0;
}
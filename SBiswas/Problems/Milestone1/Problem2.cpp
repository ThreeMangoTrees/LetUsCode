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
    Node* temp = new Node(val);
    return temp;
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

int main()
{
    Node* my_tree = new Node(1);
    
    // insert(my_tree,1);
    my_tree->left = insert(2);
    my_tree->right = insert(3);
    
    my_tree->left->left = insert(4);
    my_tree->left->right = insert(5);
    
    my_tree->right->left = insert(6);
    my_tree->right->right = insert(7);
    
    std::cout<<"Preorder Traversal: \n";
    preorder(my_tree);
    std::cout<<'\n';
    std::cout<<"Postorder Traversal: \n";
    postorder(my_tree);
    std::cout<<'\n';
    
    return 0;
}


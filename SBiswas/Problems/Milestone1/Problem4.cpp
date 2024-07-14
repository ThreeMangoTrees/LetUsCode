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

void inorder(Node* root, std::set<int>& node_set)
{   
    /*
        Traverse and collect tree node values in nodes list;
    */
    if(root == nullptr)
    {
        return;
    }
    
    inorder(root->left,node_set);
    node_set.insert(root->data);
    inorder(root->right,node_set);
}

void compare_trees(Node* tree_A, Node* tree_B)
{
    std::set<int> set_tree_A;
    std::set<int> set_tree_B;
    std::set<int> intersection;

    inorder(tree_A,set_tree_A);
    inorder(tree_B,set_tree_B);
    
    if(set_tree_A.empty() || set_tree_B.empty())
    {
        std::cout<<"One of the tree has no data";
    }

    std::set_intersection(set_tree_A.begin(), set_tree_A.end(), 
                          set_tree_B.begin(), set_tree_B.end(), 
                          std::inserter(intersection, intersection.begin()));
    
    if(set_tree_A == set_tree_B)
    {
        std::cout<<"Both Trees have equal nodes\n\n";
    }
    else if(intersection.empty())
    {
        std::cout<<"Both Trees have different nodes\n\n";
    }
    else
    {
        std::cout<<"Both Trees have common nodes\n\n";
    }

}

int main()
{
    // Both trees have Same Nodes
    std::vector<int> nodes_11 = {20, 10, 30, 5, 15, 25, 35};
    std::vector<int> nodes_12 = {20, 10, 30, 5, 15, 25, 35};
    
    // Both Trees have different Nodes
    std::vector<int> nodes_21 = {20, 10, 30, 5, 15, 25, 35};
    std::vector<int> nodes_22 = {40, 50, 60, 70, 80, 90, 100};

    // Both Trees have Common nodes
    std::vector<int> nodes_31 = {20, 10, 30, 5, 15, 25, 35};
    std::vector<int> nodes_32 = {15, 25, 35, 45, 55};

    Node* tree_1 = nullptr;
    Node* tree_2 = nullptr;
    Node* tree_3 = nullptr;
    Node* tree_4 = nullptr; 
    
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

    // Create Tree 4 
    for(int & val : nodes_32)
    {
        tree_4 = insert_in_BST(tree_4,val);
    }

    std::cout<< "Comparing Trees 1 and 2 \n";
    std::cout<< "Tree 1:  ";
    inorder(tree_1);
    std::cout<<'\n';
    std::cout<< "Tree 2:  ";
    inorder(tree_2);
    std::cout<<'\n';
    compare_trees(tree_1, tree_2);
    
    std::cout<< "Comparing Trees 1 and 3 \n";
    std::cout<< "Tree 1:  ";
    inorder(tree_1);
    std::cout<<'\n';
    std::cout<< "Tree 3:  ";
    inorder(tree_3);
    std::cout<<'\n';
    compare_trees(tree_1, tree_3);

    std::cout<< "Comparing Trees 1 and 4 \n";
    std::cout<< "Tree 1:  ";
    inorder(tree_1);
    std::cout<<'\n';
    std::cout<< "Tree 4:  ";
    inorder(tree_4);
    std::cout<<'\n';
    compare_trees(tree_1, tree_4);
    
    return 0;
}


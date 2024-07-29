#include <iostream>
#include <vector>
#include <stack>
#include <queue>
/*
    TODO: Modularize the code. For example build a different header file 
    with class Node and Class BST for binary search tree.

    Find 2nd minimum value of a special tree
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

void inorder(Node* root, priority_queue<int, vector<int>, greater<int>>& pq)
{       
    if(!root)
    {
        return;
    }
    inorder(root->left, pq);
    pq.push(root->data);
    inorder(root->right, pq);
}

int findSecondMinimumValue(Node* root) {
    priority_queue<int, vector<int>, greater<int>> pq;
    
    inorder(root,pq);
    int first_min = pq.top();
    pq.pop();

    while(pq.top()==first_min && !pq.empty())
    {
        pq.pop();
    }

    if(pq.empty())
    {
        return -1;
    }

    return pq.top();

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

    cout<<"Second minimum value of the tree is: "<<findSecondMinimumValue(tree)<<'\n';

    return 0;
}
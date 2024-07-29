#include <iostream>
#include <vector>
/*
    TODO: Modularize the code. For example build a different header file 
    with class Node and Class BST for binary search tree.
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

void recursion(Node* root, int targetSum, vector<int> curr_ans, vector<vector<int>>& ans)
{
    if(!root)
    {
        return;
    }

    curr_ans.push_back(root->data);
    if(!root->left && !root->right)
    {
        if(targetSum-root->data == 0)
        {
            ans.push_back(curr_ans);
            return;
        }
    }
    else
    {
        recursion(root->right, targetSum-root->data, curr_ans, ans);
        recursion(root->left, targetSum-root->data, curr_ans, ans);
    }

    curr_ans.pop_back();
}

vector<vector<int>> pathSum(Node* root, int targetSum) {
    vector<vector<int>> ans;
    vector<int> curr_ans;
    recursion(root, targetSum, curr_ans, ans);
    return ans;
}

void printAns(vector<vector<int>>& ans)
{
    cout<<"[";
    for(auto vec : ans)
    {   
        cout<<"[";
        for(auto num : vec)
        {
            cout<<num<<" ";
        }
        cout<<"] ";
    }
    cout<<"]";
}

int main()
{
    // Node values for BST
    std::vector<int> nodes = {20, 18, 21, 3, 19};

    Node* tree = nullptr;
    
    // Create Trees 1 and 2 (they have same nodes)
    for(int & val : nodes)
    {
        tree = insert_in_BST(tree,val);
    }

    vector<vector<int>> ans = pathSum(tree, 41);
    printAns(ans);    
    cout<<"\n";
    return 0;
}
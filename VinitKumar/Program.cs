// Problem 1

using VinitKumar.Problems;
using VinitKumar.Utilities;

Problem1 problem1Instance = new();
TreeNode? BinaryTreeRoot = problem1Instance.CreateABinaryTree();
problem1Instance.InOrderTraversalRecursive(BinaryTreeRoot);

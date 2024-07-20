using System;
using VinitKumar.Utilities;

/*
 * Tasks - 
		1. Iterative solution only - [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
		1. Iterative solution only - [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
		1. Iterative solution only - [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)
 * */

namespace VinitKumar.Problems
{
	public class Problem11
	{
		public static void InOrderTraversal(TreeNode? root)
		{
			Stack<TreeNode> st = new();
			while(root != null || st.Count > 0)
			{
				while(root != null)
				{
					st.Push(root);
					root = root.left;
				}
				root = st.Pop();
				Console.WriteLine(root.val);
				root = root?.right;
			}
		}

        public static void PreOrderTraversal(TreeNode? root)
        {
			Stack<TreeNode> st = new();
			while(root != null || st.Count > 0)
			{
				while(root != null)
				{
                    Console.WriteLine(root.val);
                    st.Push(root);
					root = root.left;
				}
				root = st.Pop();
				root = root?.right;
			}

        }

        public static IList<int> PostorderTraversal(TreeNode? root)
        {
            Stack<TreeNode> st = new();
            IList<int> ans = [];
            if (root == null) return ans;
            TreeNode? lastVisited = null;

            while (root != null || st.Count > 0)
            {
                if (root != null)
                {
                    st.Push(root);
                    root = root.left;
                }
                else
                {
                    TreeNode? top = st.Peek();
                    if (top?.right != null && lastVisited != top?.right)
                    {
                        root = top?.right;
                    }
                    else
                    {
                        ans.Add((top?.val).GetValueOrDefault());
                        lastVisited = st.Pop();
                    }
                }
            }
            return ans;
        }
    }
}

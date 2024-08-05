using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem14
    {
        public IList<int> IterativePreorder(Node root)
        {
            IList<int> ansI = new List<int>();
            if (root == null)
            {
                return ansI;
            }
            Stack<Node> st = new Stack<Node>();
            st.Push(root);

            while (st.Count > 0)
            {
                Node crnt = st.Pop();
                ansI.Add(crnt.val);
                if (crnt.children is null) continue;
                for (int i = crnt.children.Count - 1; i >= 0; i--)
                {
                    st.Push(crnt.children[i]);
                }
            }
            return ansI;
        }

        IList<int> ans;
        public void RecursivePreOrder(Node root)
        {
            if (root == null)
            {
                return;
            }

            ans.Add(root.val);

            for (int i = 0; i < root.children.Count; i++)
            {
                RecursivePreOrder(root.children[i]);
            }
        }

        public IList<int> Preorder(Node root)
        {
            //return IterativePreorder(root);
            ans = new List<int>();
            RecursivePreOrder(root);
            return ans;
        }
    }
}
using VinitKumar.Utilities;

namespace VinitKumar.Problems.Milestone1
{
    public class Problem14
    {
        private IList<int> IterativePreorder(Node root)
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

        private IList<int> ansRPreOrder;
        private void RecursivePreOrder(Node root)
        {
            if (root == null)
            {
                return;
            }

            ansRPreOrder.Add(root.val);

            for (int i = 0; i < root.children.Count; i++)
            {
                RecursivePreOrder(root.children[i]);
            }
        }

        public IList<int> Preorder(Node root)
        {
            //return IterativePreorder(root);
            ansRPreOrder = new List<int>();
            RecursivePreOrder(root);
            return ansRPreOrder;
        }


        // Part - 2

        private IList<int> ansRPostOrder;
        private IList<int> IterativePostOrder(Node root)
        {
            IList<int> ans = new List<int>();
            if (root == null)
            {
                return ans;
            }

            Stack<Node> st = new Stack<Node>();
            st.Push(root);
            while (st.Count > 0)
            {
                Node crnt = st.Pop();
                if (crnt.children is null) continue;
                for (int i = 0; i < crnt.children.Count; i++)
                {
                    st.Push(crnt.children[i]);
                }
                ans.Insert(0, crnt.val);
            }
            return ans;
        }

        
        private void RecursivePostOrder(Node root)
        {
            if (root == null || root.children is null)
            {
                return;
            }

            for (int i = 0; i < root.children.Count; i++)
            {
                RecursivePostOrder(root.children[i]);
            }

            ansRPostOrder.Add(root.val);
        }

        public IList<int> Postorder(Node root)
        {
            //return Iterative(root);
            ansRPostOrder = new List<int>();

            RecursivePostOrder(root);
            return ansRPostOrder;
        }
    }
}
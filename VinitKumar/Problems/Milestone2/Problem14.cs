namespace VinitKumar.Problems.Milestone2
{
    
    
    public class TreeNode {
       public int val;
       public TreeNode? left;
       public TreeNode? right;
       public TreeNode(int val=0, TreeNode? left=null, TreeNode? right=null) {
             this.val = val;
           this.left = left;
         this.right = right;
         }
    }
    public class Problem14 {
        List<string> ans = new List<string>();
        private void Helper(TreeNode? root, string crnt) {
            if(root == null) {
                return;
            }
            crnt = crnt == "" ? (root.val).ToString() : crnt + ("->" + (root.val).ToString());
            if(root.left == null && root.right == null) {
                ans.Add(crnt);
            } 

            Helper(root?.left, crnt);
            Helper(root?.right, crnt);
        }
        public IList<string> BinaryTreePaths(TreeNode root) {
            Helper(root, "");
            return ans;
        }
    }
}
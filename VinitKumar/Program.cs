

using VinitKumar.Problems.Milestone1;
using VinitKumar.Utilities;


Console.WriteLine("Problem 13");

TreeNode root = new(4)
{
    left = new(2)
    {
        left = new(1),
        right = new(3)
    },
    right = new(7)
};

TreeNode? ans = Problem13.SearchBST(root, 3);
Console.WriteLine(ans?.val);

ans = Problem13.SearchBST(root, 2);
Console.WriteLine(ans?.val);

ans = Problem13.SearchBST(root, 14);
Console.WriteLine(ans?.val);




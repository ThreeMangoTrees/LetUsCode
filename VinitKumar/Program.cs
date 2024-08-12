

using VinitKumar.Problems.Milestone1;
using VinitKumar.Utilities;


Console.WriteLine("Problem 13");

TreeNode root = new(2)
{
    left = new(2)
    {
        left = new(1),
        right = new(2)
    },
    right = new(2)
};
Console.WriteLine($"ans = {Problem13.FindSecondMinimumValue(root)}");

root = new(2)
{
    left = new(2)
    {
        left = new(2),
        right = new(2)
    },
    right = new(5)
    {
        left = new(5),
        right = new(7)
    }
};
Console.WriteLine($"ans = {Problem13.FindSecondMinimumValue(root)}");





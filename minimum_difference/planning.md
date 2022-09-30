Given a binary search tree, return the minimum difference between any two nodes in the tree.

Ex: Given the following tree...
        2
       / \
      3   1
return 1.
Ex: Given the following tree...
        29
       /  \
     17   50
    /     / \
   1    42  59
return 8.
Ex: Given the following tree...
        2
         \
         100
return 98.


First thought is that this is a binary search tree so we are going to have to do a loop of some sort... Probably a while loop or I guess recursion would also be viable and maybe even better.

Then within the recursion or loop we would need to compare each node and then check it against past comparisons.


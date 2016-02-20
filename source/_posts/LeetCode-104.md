---
layout: post
title: LeetCode - Maximum Depth of Binary Tree
date: 2015-2-28
description: "LeetCode"
tags: [LeetCode,code]
---

# Maximum Depth of Binary Tree

>Given a binary tree, find its maximum depth.
>
>The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```c++

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode *root) {
        if(root == NULL)
            return 0;
        return max(maxDepth(root->left),maxDepth(root->right))+1;
    }
};

```
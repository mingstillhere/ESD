# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:01:33 2020

@author: bjdn
"""

from collections import deque
class Node(object):
    def __init__(self,item,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
def add(root, item):
    if root is None:
        return False
    node = Node(item)
    q = [root]
    while True:
        pop_node = q.pop(0)
        if pop_node.left is None:
            pop_node.left = node
            return root
        elif pop_node.right is None:
            pop_node.right = node
            return root
        else:
            q.append(pop_node.left)
            q.append(pop_node.right)

def get_parent(root, item):
    '''
    Find the parent node of Item
    '''
    if root.item == item:
        return None
    tmp = [root]
    while tmp:
        pop_node = tmp.pop(0)
        if pop_node.left and pop_node.left.item == item:
            return pop_node
        if pop_node.right and pop_node.right.item == item:
            return pop_node
        if pop_node.left is not None:
            tmp.append(pop_node.left)
        if pop_node.right is not None:
            tmp.append(pop_node.right)
    return None

def delete(root,item):
        '''
        Remove an element from the binary tree
        First get the parent node of the node item to be deleted
        If the parent node is not empty,
            Determine the left and right subtrees of item
            If the left subtree is empty, then determine whether item is the left child or the right child of the parent node. 
            If it is a left child, point the left pointer of the parent node to the right subtree of the item, otherwise point the right pointer of the parent node to the right of item Subtree    
            
            If the right subtree is empty, then determine whether item is the left child or right child of the parent node. 
            If it is a left child, point the left pointer of the parent node to the left child tree of item, otherwise, point the right pointer of the parent node to the left of item Subtree
            
            If the left and right subtrees are not empty, find the leftmost leaf node x in the right subtree and replace x with the node to be deleted.
        '''
        if root is None:
            return False
 
        parent = get_parent(root,item)
        if parent:
            if parent.left and parent.left.item == item:
                del_node = parent.left
            elif parent.right and parent.right.item == item:
                del_node = parent.right
            
            if parent.left and del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return root
            elif del_node.right is None:
                if parent.left and parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return root
            else:  
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
 
                else:
                    while tmp_next.left:  
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left and parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return root
        else:
            if root.item==item:
                if root.left is None and root.right is None:
                    
                    root.item = None
                    del root
                    return None
                if root.left is None:
                    root.item=root.right.item
                    root.left=root.right.left
                    root.right=root.right.right
                    
                    return root
                if root.right is None:
                    root.item=root.left.item
                    root.right=root.left.right
                    root.left=root.left.left
                    
                    
                    return root
                if root.right.left is None:
                    del_node=root.right
                    root.item=del_node.item
                    root.right=del_node.right
                    del del_node
                    return root
                tmp_pre = root.right
                tmp_next= tmp_pre.left
                while tmp_next.left:
                    tmp_pre = tmp_next
                    tmp_next = tmp_next.left
                root.item=tmp_next.item
                tmp_pre.left=tmp_next.right
                del tmp_next
                return root
                    
                            
                

def to_list(root):  # Level traversal
    if root is None or isinstance(root,Node) is False:
        return []
    q = [root]
    res = [root.item]
    while q != []:
        pop_node = q.pop(0)
        if pop_node.left is not None:
            q.append(pop_node.left)
            res.append(pop_node.left.item)
        if pop_node.right is not None:
            q.append(pop_node.right)
            res.append(pop_node.right.item)
    return res   
    
def traverse(root):  # Level traversal
    if root is None or isinstance(root,Node) is False:
        return []
    q = [root]
    res = [root.item]
    while q != []:
        pop_node = q.pop(0)
        if pop_node.left is not None:
            q.append(pop_node.left)
            res.append(pop_node.left.item)
        if pop_node.right is not None:
            q.append(pop_node.right)
            res.append(pop_node.right.item)
    return res   
    
def getlength(root):
    return len(traverse(root))

def find_special(root,func):
    res=[]
    src=traverse(root)
    
    for i in src:
        if(func(i)):
            res.append(i)
        
    return res

def filter_special(root,func):
    src=find_special(root,func)
    for i in src:
        delete(root,i)
    if(root.item == None):
        return None
    return root

def map(root,func):
    if root is None:
        return None
    q = [root]
    res = [root.item]
    root.item=func(root.item)
    while q != []:
        pop_node = q.pop(0)
        if pop_node.left is not None:
            q.append(pop_node.left)
            res.append(pop_node.left.item)
            pop_node.left.item=func(pop_node.left.item)
        if pop_node.right is not None:
            q.append(pop_node.right)
            res.append(pop_node.right.item)
            pop_node.right.item=func(pop_node.right.item)
    return root

def reduce(root,func):
    if(root == None):
        return 0
    src=traverse(root)
    length=len(src)-1
    res=src[0]
    for i in range(length):
        res=func(res,src[i+1])
    return res

def mempty(root):
    if root is not None:
        src=traverse(root)
        for i in src:
            root=delete(root,i)
        return root
    else:
        return None

def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """

    if (t1 is None and t2 is None):
        return None

    if (t1 is None):
        return t2
    if (t2 is None):
        return t1
    
    if ((type(t1)!= 'bool') and (type(t1)!= 'bool')):
        if (t1.item!='root' and t2.item!='root'):
            t1.item += t2.item

        t1.right = mergeTrees(t1.right, t2.right)
        t1.left = mergeTrees(t1.left, t2.left)
        return t1
    
def construct_tree(item=None):
     if item is None or len(item)==0:
         return None
     root = Node(item[0])
     queue = deque([root])
     leng = len(item)
     nums = 1     
     while nums < leng:
         node = queue.popleft()
         if node:
            node.left = Node(item[nums]) if item[nums]!=None else None
            queue.append(node.left)
            if nums + 1 < leng:
                 node.right = Node(item[nums+1]) if item[nums+1]!=None else None
                 queue.append(node.right)
                 nums += 1
            nums += 1
     return root
 
def in_traversal(root):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.item)
            traversal(head.right)

        traversal(root)
        return ret   
    
def iter(root):
        src=traverse(root)
        for c in src:
            yield c
            

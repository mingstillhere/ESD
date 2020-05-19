# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import deque

class Node(object):
    def __init__(self,item,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class Tree(object):
    def __init__(self):
        self.root = None
 
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
 
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
 
    def get_parent(self, item):
        if self.root.item == item:
            return None
        tmp = [self.root]
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
 
    def delete(self, item):
        if self.root is None:
            return False
 
        parent = self.get_parent(item)
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
                return True
            elif del_node.right is None:
                if parent.left and parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
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
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            if self.root.item == item:
                if self.root.left is None and self.root.right is None:
                    self.root = None
                    return self.root 
                if self.root.left is None:
                    del_node=self.root
                    tmp_root=self.root.right
                    return tmp_root
                if self.root.right is None:
                    del_node=self.root
                    tmp_root=self.root.left
                    self.root=tmp_root
                    return self.root
                if self.root.right.left is None:
                    del_node=self.root.right
                    self.root.item=del_node.item
                    self.root.right=del_node.right
                    del del_node
                    return self.root
                tmp_pre = self.root.right
                tmp_next= tmp_pre.left
                while tmp_next.left:
                    tmp_pre = tmp_next
                    tmp_next = tmp_next.left
                self.root.item=tmp_next.item
                tmp_pre.left=tmp_next.right
                del tmp_next
                return self.root
    
    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)
 
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res
 
    def getlength(self):
        if self.root is None:
            return 0
        return len(self.traverse())
    
    def find_special(self,func):
        res=[]
        src=self.traverse()
        
        for i in src:
            if(func(i)):
                res.append(i)
        return res
    
    def filter_special(self,func):
        src=self.find_special(func)
        for i in src:
            self.delete(i)
              
    def map(self,func):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            pop_node.item=func(pop_node.item)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)
                pop_node.left.item=func(pop_node.left.item)
 
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
                pop_node.right.item=func(pop_node.right.item)
    
    def reduce(self,func):
        src=self.traverse()
        length=len(src)-1
        res=src[0]
        for i in range(length):
            res=func(res,src[i+1])
        return res
    
    def mempty(self):
        if self.root is not None:
            src=self.traverse()
            for i in src:
                self.delete(i)
            self.root=None
        return self.root
        
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (t1 is None and t2 is None):
            return
        if (t1 is None):
            return t2
        if (t2 is None):
            return t1
        if (t1.item!='root' and t2.item!='root'):
            t1.item += t2.item
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        
        return t1
    
#tree to list

    def to_list(self):
        if self.root is None:
            return []
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)
 
            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res

    
    def construct_tree(self, item=None):
        if item is None or len(item)==0:
            return None
        self.root = Node(item[0])
        queue = deque([self.root])
        leng = len(item)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = Node(item[nums]) if item[nums] != None else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = Node(item[nums+1]) if item[nums+1] != None else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    

    def iter(self):
        src=self.traverse()
        for c in src:
            yield c



    
        
        
        
        
        
                

        
            
            

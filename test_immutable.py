# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:38:20 2020

@author: bjdn
"""

import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *

#For add function need two parameters:the tree node and the data that is added.
#When the parameter tree node is none,we add a root node "root"
#Also ,when we construct a tree from list ,we add a root node 'root'
#

class TestMutableList(unittest.TestCase):
    
    def test_construct_tree(self):
        '''
        root=construct_tree([5,8,6,3,1])
        self.assertEqual(traverse(root), [ 5, 8, 6, 3, 1])
        self.assertEqual(in_traversal(root), [3, 8, 1, 5, 6])
        '''
        self.assertEqual(traverse(construct_tree([5,8])), traverse(add(construct_tree([5]),8)))
    
    def test_add(self):
        '''
        root=construct_tree([5,8,6,3,1])
        add(root,10)
        self.assertEqual(traverse(root), [5, 8, 6, 3, 1,10])
        self.assertEqual(in_traversal(root), [3, 8, 1, 5, 10, 6])
        add(root,4)
        self.assertEqual(traverse(root), [ 5, 8, 6, 3, 1,10,4])
        self.assertEqual(in_traversal(root), [3, 8, 1, 5, 10, 6, 4])
        '''
        root1 = construct_tree()
        self.assertEqual(traverse(construct_tree([5, 8])), traverse(add(construct_tree([5]), 8)))


    
    def test_del(self):
        '''
        root=construct_tree([5,8,6,3,1])
        delete(root,6)
        self.assertEqual(traverse(root), [5, 8, 3, 1])
        self.assertEqual(in_traversal(root), [3, 8, 1, 5])
        delete(root,1)
        self.assertEqual(traverse(root), [ 5, 8, 3])
        self.assertEqual(in_traversal(root), [3, 8, 5])
        '''
        self.assertEqual(traverse(delete(construct_tree([5, 8]),8)), traverse(construct_tree([5])))
        
    def test_getlength(self):
        '''
        root=construct_tree([5,8,6,3,1])
        self.assertEqual(getlength(root), 5)
        delete(root,6)
        self.assertEqual(getlength(root), 4)
        '''
        self.assertEqual(getlength(add(construct_tree([5]),8)), 2)

    
    def test_tolist(self):
        '''
        root=construct_tree([5,8,6,3,1])
        self.assertEqual(to_list(root),[5,8,6,3,1])
        '''
        self.assertEqual(to_list(construct_tree([5, 8])), to_list(add(construct_tree([5]), 8)))

    def test_find(self):
        def is_even(i):
            if (i%2==0):
                return True
            return False
        def is_odd(i):
            if (i%2==1):
                return True
            return False
        '''
        root=construct_tree([5,8,6,3,1])
        res = find_special(root,"is_even_")
        self.assertEqual(res, [8,6])
        res = find_special(root,'is_odd_')
        self.assertEqual(res, [5,3,1])
        '''
        self.assertEqual(find_special(construct_tree([5,8,6,3,1]),is_even), [8, 6])
        
    def test_filter(self):
        def is_even(i):
            if (i%2==0):
                return True
            return False
        def is_odd(i):
            if (i%2==1):
                return True
            return False
        '''
        root=construct_tree([5,8,6,3,1])
        filter_special(root,"is_odd_")
        self.assertEqual(traverse(root), [6, 8])
        '''
        self.assertEqual(traverse(filter_special(construct_tree([5,8,6,3,1]),is_odd)), [6, 8])
    
    def test_mempty(self):
        '''
        root=construct_tree([5,8,6,3,1])
        
        self.assertEqual(getlength(mempty(root)), 0)
        '''
        self.assertEqual(getlength(mempty(construct_tree([5, 8]))), 0)

    def test_mergeTrees(self):
        '''
        root1=construct_tree([5,8,6,3,1])
        root2=construct_tree([5,8,6,3,1])
        root1= mergeTrees(root1,root2)
        self.assertEqual(traverse(root1), [10, 16, 12, 6, 2])
        '''
        self.assertEqual(traverse(mergeTrees(construct_tree([5, 8]),construct_tree([5, 8]))), traverse(construct_tree([10, 16])))
        
    def test_map(self):
        def increment(i):
            return i+1

        '''
        root=construct_tree([5,8,6,3,1])
        map(root,increment)
        self.assertEqual(traverse(root), [6, 9, 7, 4, 2])
        '''
        self.assertEqual(traverse(map(construct_tree([5, 8]),increment)), traverse(construct_tree([6, 9])))
        
    def test_reduce(self):
        def Sum(x,y):
            return x+y

        '''
        root=construct_tree([5,8,6,3,1])
        self.assertEqual(reduce(root,Sum), 23)
        '''
        self.assertEqual(reduce(construct_tree([5, 8]), Sum), 13)

    def test_iter(self):
        root=construct_tree([4,8,6,3,4])
        res=[4,8,6,3,4]
        i=0
        for x in iter(construct_tree([4,8,6,3,4])):
            self.assertEqual(x, res[i])
            i=i+1



    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        '''
        root=construct_tree(a)
        b=to_list(root)
        self.assertEqual(b, a)
        '''
        self.assertEqual(to_list(construct_tree(a)), a)
    
    @given(st.lists(st.integers()))
    def test_python_len_and_tree_size_equality(self,a):
        '''
        root=construct_tree(a)
        l=getlength(root)
        self.assertEqual(l, len(a))
        '''
        self.assertEqual(getlength(construct_tree(a)),len(a))
        
    @given(st.lists(st.integers()))
    def test_identity_element(self,a):

        self.assertEqual(traverse(mergeTrees(construct_tree(a),mempty(None))), traverse(construct_tree(a)))
        self.assertEqual(traverse(mergeTrees(mempty(None),construct_tree(a))), traverse(construct_tree(a)))
        
    @given(st.lists(st.integers()),st.lists(st.integers()),st.lists(st.integers()))
    def test_associativity(self,a,b,c):
        self.assertEqual(traverse(mergeTrees(mergeTrees(construct_tree(a),construct_tree(b)),construct_tree(a))), traverse(mergeTrees(mergeTrees(construct_tree(a),construct_tree(b)),construct_tree(a))))
        
        

if __name__=='__main__':
    unittest.main()
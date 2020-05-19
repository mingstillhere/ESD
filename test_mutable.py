# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:25:27 2020

@author: bjdn
"""

import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *

class TestMutableList(unittest.TestCase):
    def test_add(self):
        tree = Tree()
        tree.add('a')
        self.assertEqual(tree.to_list(), ['a'])

    def test_del(self):
        tree = Tree()
        tree.add('a')
        tree.add('b')
        self.assertEqual(tree.to_list(), ['a','b'])
        tree.delete('b')
        self.assertEqual(tree.to_list(), ['a'])

    def test_getlength(self):
        tree = Tree()
        self.assertEqual(tree.getlength(), 0)
        tree.add('a')
        self.assertEqual(tree.getlength(), 1)

    def test_tolist(self):
        tree = Tree()
        tree.add('a')
        self.assertEqual(tree.to_list(), ['a'])
        tree.add('b')
        self.assertEqual(tree.to_list(), ['a','b'])

    def test_find(self):
        def is_even(i):
            if (i%2==0):
                return True
            return False
        def is_odd(i):
            if (i%2==1):
                return True
            return False
        tree = Tree()
        tree.add(2)
        tree.add(3)
        res = tree.find_special(is_even)
        self.assertEqual(res, [2])
        res = tree.find_special(is_odd)
        self.assertEqual(res, [3])

    def test_filter(self):
        def is_even(i):
            if (i%2==0):
                return True
            return False
        def is_odd(i):
            if (i%2==1):
                return True
            return False
        tree = Tree()
        tree.add(2)
        tree.add(3)
        tree.filter_special(is_even)
        self.assertEqual(tree.to_list(), [3])
        tree.filter_special(is_odd)
        self.assertEqual(tree.to_list(), [])

    def test_mempty(self):
        tree = Tree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.mempty()
        self.assertEqual(tree.getlength(), 0)

    def test_mergeTrees(self):
        tree1 = Tree()
        tree1.add(1)
        tree1.add(2)
        tree2 = Tree()
        tree2.add(1)
        tree2.add(2)
        tree1.root = tree1.mergeTrees(tree1.root,tree2.root)
        self.assertEqual(tree1.to_list(), [2,4])
        
    def test_map(self):
        def increment(i):
            return i+1
        tree1 = Tree()
        tree1.add(1)
        tree1.add(2)
        tree1.map(increment)
        self.assertEqual(tree1.to_list(), [2,4])
        
    def test_reduce(self):
        def Sum(x,y):
            return x+y
        tree1 = Tree()
        tree1.add(1)
        tree1.add(2)
        self.assertEqual(tree1.reduce(Sum), 3)
        
    def test_construct_tree(self):
        t=Tree()
        t.construct_tree([4,8,6,3,4])
        self.assertEqual(t.traverse(), [4, 8, 6, 3, 4])
        
    def test_iter(self):
        t=Tree()
        t.construct_tree([4,8,6,3,4])
        res=[4,8,6,3,4]
        i=0
        for x in t.iter():
            self.assertEqual(x, res[i])
            i=i+1
            
    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        t=Tree()
        t.construct_tree(a)
        b=t.to_list()
        self.assertEqual(b, a)
        
    @given(st.lists(st.integers()))
    def test_python_len_and_tree_size_equality(self,a):
        t=Tree()
        t.construct_tree(a)
        l=t.getlength()
        self.assertEqual(l, len(a))
        
    @given(st.lists(st.integers()))
    def test_identity_element(self,a):
        t1=Tree()
        t1.construct_tree(a)
        t2=Tree()
        t2.mempty()
        t3=Tree()
        t3.root = t1.mergeTrees(t1.root,t2.root)
        self.assertEqual(t3.to_list(), t1.to_list())
        
        t1=Tree()
        t1.construct_tree(a)
        t2=Tree()
        t2.mempty()
        t3=Tree()
        t3.root = t2.mergeTrees(t1.root,t2.root)
        self.assertEqual(t3.to_list(), t1.to_list())
        
    @given(st.lists(st.integers()),st.lists(st.integers()),st.lists(st.integers()))
    def test_associativity(self,a,b,c):
        t1=Tree()
        t11=Tree()
        t1.construct_tree(a)
        t11.construct_tree(a)
        t2=Tree()
        t22=Tree()
        t2.construct_tree(b)
        t22.construct_tree(b)
        t3=Tree()
        t33=Tree()
        t3.construct_tree(c)
        t33.construct_tree(c)
        
        t4=Tree()
        t4.root = t33.mergeTrees(t1.mergeTrees(t1.root,t2.root),t3.root)
        t5=Tree()
        t5.root = t11.mergeTrees(t22.mergeTrees(t22.root,t33.root),t11.root)
        self.assertEqual(t4.to_list(), t5.to_list())
      
        
        
if __name__=='__main__':
    unittest.main()
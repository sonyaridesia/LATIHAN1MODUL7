#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:23:17 2022

@author: sonyaridesia
"""
def is_prima ():
    x=int(input("Masukan angkanya: "))
    for i in range(2, x):
        if x % i == 0:
            return ("bukan bilangan prima")
    return ("bilangan prima")
        
p=is_prima()
print(p)

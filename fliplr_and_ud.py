# -*- coding: utf-8 -*-
"""FlipLR and UD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MQMGBDTxVqeNnnRq4Nf50acAV0UGRpQS
"""

vec = []

def flipLR(vec, i):
  if (i < len(vec)/2):
    aux = vec[i]
    vec[i] = vec[len(vec)-i-1]
    vec[len(vec)-i-1] = aux
    flipLR(vec, i+1)

vec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vec2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
flipLR(vec, 0)
flipLR(vec2, 0)
print(vec)
print(vec2)
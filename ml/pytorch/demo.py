import torch
import numpy as np 

a = torch.LongTensor([[2,3],[4,8],[7,9]])
print('a is : {}'.format(a))
print('a size is {}'.format(a.size()))

c = torch.zeros((3,2))
print('c is : {}'.format(c))

d = torch.randn((2,3))
print('d is : {}'.format(d))

a[0,1] = 10
print('a change to {} '.format(a))

numpy_b = a.numpy()

print('a convert to numpy {}'.format(numpy_b))

print (' support GPU {}'.format(torch.cuda.is_available()) )




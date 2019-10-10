import torch
a=torch.Tensor([[2,3],[1,1]])
print(a)
b=a[0].clone().detach()
b[0]=8
print(a)
print(b)
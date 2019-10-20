import torch

x = torch.ones([3, 4])
s = torch.cuda.is_available()

print(s)


import torch
print(torch.version)  # 应显示 2.0.1+cu118
print(torch.cuda.is_available())  # 应返回 True
print(torch.version.cuda)  # 应显示 11.8
print(torch.cuda.get_device_name(0))  # 应显示你的 GPU 名称

import torchvision
print(torchvision.version)  # 应显示 0.15.2
import torch.nn as nn
import torch.functional as F

class Inception(nn.modules):
    def __init__(self):
        super().__init__()

    
class Sleep_CNN(nn.modules):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1,1,7)
        self.bn1 = nn.BatchNorm2d(256)
        self.mp1 = nn.MaxPool2d(3,2)
        
        self.conv2 = nn.Conv2d(1,1,3)
        self.bn2 = nn.BatchNorm2d(128)
        self.mp2 = nn.MaxPool2d(3,2)



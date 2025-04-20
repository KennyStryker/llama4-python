import torch
from torch import nn


class Llama4(nn.Module):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def forward(self, inp: torch.Tensor):
        return inp

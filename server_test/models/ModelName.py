from enum import Enum


class ModelName(str, Enum):
    ALEXNET = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

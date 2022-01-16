import torch.nn as nn

############ This part of the code is from an old model ##################


def old_conv_block(in_planes, out_planes, kernel_size):
    return nn.Sequential(
        nn.Conv2d(in_planes, out_planes, kernel_size=kernel_size, bias=False),
        nn.BatchNorm2d(out_planes),
        nn.ReLU(inplace=True)
    )


def old_pokemon_model():
    return nn.Sequential(
        old_conv_block(3, 16, 7),
        nn.MaxPool2d(kernel_size=2),
        old_conv_block(16, 32, 3),
        nn.MaxPool2d(kernel_size=2),
        old_conv_block(32, 64, 3),
        nn.MaxPool2d(kernel_size=2),
        old_conv_block(64, 128, 3),
        nn.MaxPool2d(kernel_size=2),
        old_conv_block(128, 256, 3),
        nn.MaxPool2d(kernel_size=2),
        old_conv_block(256, 512, 3),
        nn.MaxPool2d(kernel_size=2),
        nn.Flatten(),
        nn.Linear(512, 150)
    )
#############################################################################


def simple_conv_block(in_planes, out_planes, kernel_size, stride=1, padding=0):
    return nn.Sequential(
        nn.Conv2d(in_planes, out_planes, kernel_size=kernel_size,
                  stride=stride, padding=padding, bias=False),
        nn.BatchNorm2d(out_planes),
        nn.ReLU(inplace=True),
        nn.MaxPool2d(kernel_size=2)
    )


def pokemon_model(num_classes=149):
    return nn.Sequential(
        simple_conv_block(3, 32, 3),
        simple_conv_block(32, 32, 3),
        simple_conv_block(32, 64, 3),
        simple_conv_block(64, 64, 3),
        simple_conv_block(64, 128, 3),
        nn.Flatten(),
        nn.Linear(128, num_classes)
    )

from torchvision import datasets, transforms
import os

root = "data/cifar10"
os.makedirs(root, exist_ok=True)

transform = transforms.ToTensor()

print("Downloading CIFAR-10...")
datasets.CIFAR10(root=root, train=True, download=True, transform=transform)
datasets.CIFAR10(root=root, train=False, download=True, transform=transform)

print("Done! Files saved in data/cifar10")
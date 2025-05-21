import torch

print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("Device:", torch.cuda.get_device_name(0))
    print("Memory Allocated:", torch.cuda.memory_allocated(0) / 1e6, "MB")
    print("Memory Reserved:", torch.cuda.memory_reserved(0) / 1e6, "MB")
else:
    print("Running on CPU.")

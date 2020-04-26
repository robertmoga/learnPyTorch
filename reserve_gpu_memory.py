def check_mem():
    # replace with the path of current's sistem gpu management interface 
    mem = os.popen('"C:\\Program Files\\NVIDIA Corporation\\NVSMI\\nvidia-smi" --query-gpu=memory.total,memory.used --format=csv,nounits,noheader').read().split(",")
    
    return mem

def reserve_gpu_memory(allocated_percent):
    
    total, used = check_mem()
    
    total = int(total)
    used = int(used)
    
    print(total)
    print(used)
    
    max_mem = int(total * allocated_percent)
    block_mem = max_mem - used
        
    x = torch.rand((256,1024,block_mem)).cuda()
    x = torch.rand((2,2)).cuda()

if __name__ == "__main__":
    reserve_gpu_memory(0.8) # allocates 80% of available memory for CUDA
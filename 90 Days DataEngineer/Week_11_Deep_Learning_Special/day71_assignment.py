import torch

def create_and_sum_tensors(a_list: list, b_list: list):
    """
    Convert lists a_list and b_list to PyTorch Tensors,
    and return their sum as a PyTorch Tensor.
    """
    t_a = torch.tensor(a_list)
    t_b = torch.tensor(b_list)
    return t_a + t_b

from fvcore.nn import FlopCountAnalysis
from transformers import AutoModelForCausalLM
import argparse
import torch
import pprint as pp
pp = pp.PrettyPrinter(indent=4)
    

def get_input_shapes(batch_size=1, sequence_length=512):
    # Create a dummy input tensor with the desired shape
    input_tensor = torch.ones(batch_size, sequence_length, dtype = torch.long)
    return input_tensor
    

def parse_args():
    parser = argparse.ArgumentParser(description="Count FLOPs of a causal language model.")
    parser.add_argument("--model_stub", default="HuggingFaceH4/tiny-random-LlamaForCausalLM",  type=str, help="The model stub to count FLOPs for.") 
    parser.add_argument("--batch_size", default=1, type=int, help="The batch size to use for the input tensor.")
    parser.add_argument("--sequence_length", default=512, type=int, help="The sequence length to use for the input tensor.")
    parser.add_argument("--by_module", default=False, action="store_true", help="Count FLOPs by module.")
    parser.add_argument("--by_operator", default=False, action="store_true", help="Count FLOPs by operator.")
    
           
    return parser.parse_args()

def main():
    args = parse_args() 
    model = AutoModelForCausalLM.from_pretrained(args.model_stub)
    input_shape = get_input_shapes(args.batch_size, args.sequence_length)
    flops = FlopCountAnalysis(model, input_shape)
    print(f"FLOP/s:")
    
    if args.by_module:
        pp.pprint(flops.by_module())
    elif args.by_operator:
        pp.pprint(flops.by_operator())
    else:
        pp.pprint(flops.by_module_and_operator())
        


if __name__ == "__main__":
    main()
    
    




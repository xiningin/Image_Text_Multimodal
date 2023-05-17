import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--gpu" , type=str , default="0" , help="choose the index of the gpu used to run")
parser.add_argument("--lr" , type=float , default=0.0002 , help="learning rate for train")
parser.add_argument("--log_dir", type=str , default="./tensorboard_logger/" , help="directory path for generate logging information")
parser.add_argument("--vocab_path", type=str , default="../vocab/" , help="directory path for generate logging information")
parser.add_argument("--batch_size", type=int , default=128 , help="batch size for train")
parser.add_argument("--workers", type=int , default=5 , help="number of workers for dataloader")
parser.add_argument("--embed_size", type=int , default=1024 , help="image and text align embedding size")
parser.add_argument("--finetune" , action='store_true' , default=False , help="whether finetune VGG19 embedding")
parser.add_argument("--word_dim" , type=int , default=300 , help="word embedding size")
parser.add_argument("--num_layers" , type=int , default=2 , help="number of layers for GRU")
parser.add_argument("--bidirection_rnn" , action='store_true' , default=False , help="whether use bidirection for GRU")
parser.add_argument("--rnn_mean_pool" , action='store_true' , default=False , help='whether to use mean pool for the end of GRU net')
parser.add_argument("--margin" , type=float , default=0.2 , help="margin for triplet loss")
parser.add_argument("--max_violation" , action='store_true' , default=False , help="whether to use max_violation for triplet loss")
parser.add_argument("--grad_clip" , type=float , default=2.0 , help="clip gradient")
parser.add_argument("--num_epochs" , type=int , default=30 , help="number of epochs for train")
parser.add_argument("--log_step" , type=int , default=10 , help="number of steps for logging")
parser.add_argument("--val_step" , type=int , default=500 , help="number of steps for validation")
parser.add_argument("--lr_decay_step", type=int , default=15 , help='Number of epochs to decay the learning rate.')
parser.add_argument("--use_InfoNCE_loss" , action='store_true' , default=False , help='Select whether to use InfoNCE as the loss function')
parser.add_argument("--temperature" , type=float , default=0.1 , help='float 0-1, One of the parameters of the loss function——InfoNCE')
parser.add_argument("--reduction" , type=str , default='mean' , help='str, One of the parameters of the loss function——InfoNCE')
parser.add_argument("--negative_mode" , type=str , default='unpaired' , help='str, One of the parameters of the loss function——InfoNCE')
parser.add_argument("--cnn_type" , type=str , default='VGG19' , help='choose the cnn backbone for VSE ( VGG19 , ResNet101 , ResNet152 )')
parser.add_argument("--use_attention_for_text" , action='store_true' , default=False , help='choose to use GRU or self-attention for textEncoding') 
parser.add_argument("--num_heads" , type=int , default=3 , help='heads num of multihead-attention') 

args = parser.parse_args()

from __future__ import print_function
import argparse
import os
import random
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.autograd import Variable
from models import Generator
from models import Discriminator
import gen_config

'''
parser = argparse.ArgumentParser()
parser.add_argument('--batchSize', type=int, default=64, help='input batch size')
parser.add_argument('--imageSize', type=int, default=128, help='the height / width of the input image to network')
parser.add_argument('--nz', type=int, default=128, help='size of the latent z vector')
parser.add_argument('--cuda', action='store_true', help='enables cuda')
parser.add_argument('--netG', default='', help="path to netG (to continue training)")
parser.add_argument('--outf', default='dcgan/', help='folder to output images and model checkpoints')
parser.add_argument('--manualSeed', type=int, help='manual seed')
parser.add_argument('--ngf', type=int, default=128)
'''

#opt = parser.parse_args()
opt = gen_config.Config()
#print(opt)

try:
    os.makedirs(opt.outf)
except OSError:
    pass

if opt.manualSeed is None:
    opt.manualSeed = random.randint(1, 10000)
print("Random Seed: ", opt.manualSeed)
random.seed(opt.manualSeed)
torch.manual_seed(opt.manualSeed)
if opt.cuda:
    torch.cuda.manual_seed_all(opt.manualSeed)

cudnn.benchmark = True

###########   Load netG   ###########
#assert opt.netG != '', "netG must be provided!"
nc = 3
netG = Generator(nc, opt.ngf, opt.nz, opt.imageSize)
netG.load_state_dict(torch.load(opt.netG))



###########   Generate   ###########
noise = torch.FloatTensor(opt.batchSize, opt.nz)
noise = Variable(noise)

if(opt.cuda):
    netG.cuda()
    noise = noise.cuda()


'''
vutils.save_image(fake.data,
            '%s/samples.png' % (opt.outf),
            normalize=True, nrow = 3)
'''
for i in range(1):
    noise = torch.FloatTensor(512, opt.nz)
    noise = Variable(noise)

    if (opt.cuda):
        netG.cuda()
        noise = noise.cuda()

    noise.data.uniform_(-1, 1)
    # 生成圖片，併計算圖片在判別器的分數
    fake_img = netG(noise)

    result = []
    for ii in range(9):
        result.append(fake_img.data[ii])
    # 保存圖片
    vutils.save_image(torch.stack(result), opt.outf+'/'+str(i).zfill(3)+'_image'+'.png', normalize=True, range=(-1, 1), nrow=3)

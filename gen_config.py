class Config(object):
    dataPath = 'Img/128_crop/'  # data path
    batchSize = 64
    loadSize = 128
    fineSize = 128
    flip = 1
    nz = 64
    ngf = 64
    ndf = 64
    niter = 300000
    lr = 0.0001
    beta1 = 0.5
    cuda = True
    outf = 'output/'
    manualSeed = None

    lambda_k = 0.001
    gamma = 0.5
    save_step = 1000
    hidden_size = 64
    lr_decay_every = 500
    imageSize = 128
    netG = 'output5/model_dict/netG_46000.pth'
    netD = 'output5/model_dict/netD_46000.pth'
    outf = 'img'
    gen_num = 9
    gen_search_num = 512


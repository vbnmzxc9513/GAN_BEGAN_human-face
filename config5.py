class Config(object):
    dataPath = 'Img/128_crop/'  # data path
    batchSize = 32
    loadSize = 128
    fineSize = 128
    flip = 1
    nz = 64
    ngf = 64
    ndf = 64
    niter = 300000
    lr = 0.0003
    beta1 = 0.5
    cuda = True
    outf = 'output5/model_dict/'
    outp = 'output5/pic/'
    manualSeed = None

    lambda_k = 0.001
    gamma = 0.5
    save_step = 2000
    hidden_size = 64
    lr_decay_every = 500


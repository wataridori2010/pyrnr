
import numpy as np
import cv2



def reduce_color_pyr_wb2(img3, d_sigma=0.01, x_sigma=100):

    filter_size = 5
    shape = img3.shape

    # half scale
    img4 = img3.copy()
    #img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2YCrCb) 

    # generate pyramid
    img16 = cv2.resize(img3, (int(shape[1]/2), int(shape[0]/2)), interpolation=cv2.INTER_LINEAR).astype('float32')
    img64 = cv2.resize(img16, (int(shape[1]/4), int(shape[0]/4)), interpolation=cv2.INTER_LINEAR).astype('float32')
    img256 = cv2.resize(img64, (int(shape[1]/8), int(shape[0]/8)), interpolation=cv2.INTER_LINEAR).astype('float32')

    # denoise / de-colorization
    img256_dst = cv2.bilateralFilter(img256, filter_size, d_sigma*0.13, x_sigma)
    img256_noise = img256 - img256_dst
    img64_noise  = cv2.resize(img256_noise, (int(shape[1]/4), int(shape[0]/4)), interpolation=cv2.INTER_LINEAR).astype('float32')

    img64 = img64 - img64_noise
    img64_dst = cv2.bilateralFilter(img64, filter_size, d_sigma*0.25, x_sigma)
    img64_noise = img64_noise + (img64 - img64_dst)
    img16_noise  = cv2.resize(img64_noise, (int(shape[1]/2), int(shape[0]/2)), interpolation=cv2.INTER_LINEAR).astype('float32')

    img16 = img16 - img16_noise
    img16_dst = cv2.bilateralFilter(img16, filter_size, d_sigma*0.5, x_sigma)
    img16_noise = img16_noise + (img16 - img16_dst)
    noise_map = cv2.resize(img16_noise, (int(shape[1]), int(shape[0])), interpolation=cv2.INTER_LINEAR)

    #img3_ = img3.copy()
    img3 = img3 - noise_map
    img3_dst = cv2.bilateralFilter(img3 - noise_map, filter_size, d_sigma, x_sigma)
    #img3_dst[:,:,0] = img3[:,:,0]

    return img3_dst
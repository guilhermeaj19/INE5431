''' 
INE5431 Sistemas Multimidia
Prof. Roberto Willrich

Aula Pratica IV: Compressao de Entropia

'''

from PIL import Image
from Cuif import Cuif
import math
import os

def PSNR(original,decodificada,b):
    try:
        mse = MSE(original,decodificada) 
        psnr = 10*math.log10(((2**b-1)**2)/mse)
        return psnr
    except ZeroDivisionError:
        return "Infinito"

def MSE(ori, dec):
    nsymbols = ori.width * ori.height * 3
    sum = 0
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))
            sum +=  (ori_r-dec_r)*(ori_r-dec_r) \
                  + (ori_g-dec_g)*(ori_g-dec_g) \
                  + (ori_b-dec_b)*(ori_b-dec_b)
    return sum/nsymbols

def conversor(version, img, img_name):
    cuif1 = Cuif(img,version,matriculas)
    cuif1.printHeader()
    # cuif1.show()
    cuif1.save(f'imgs_{img_name}/{img_name}{version}.cuif')
    cuif1.saveBMP(f'imgs_{img_name}/{img_name}{version}.bmp')
    img1 = Image.open(f'imgs_{img_name}/{img_name}{version}.bmp')
    print(f"PSNR do {img_name} CUIF.{version}",PSNR(img,img1,8)) 


if __name__ == "__main__":
    
    # Cria as pastas de saída
    try:
        os.mkdir('imgs_teste')
    except FileExistsError:
        pass

    try:
        os.mkdir('imgs_mandril')
    except FileExistsError:
        pass

    img = Image.open('mandril.bmp')
    img_teste = Image.open('teste.bmp')
    
    # Indique a matricula dos alunos do grupo na lista abaixo
    matriculas = [22102191, 22100619, 22100620]
    
    # Geracao do arquivo Cuif.1, converte o arquivo Cuif.1 em BMP, e calcula o PSNR
    conversor(1, img, 'mandril')
    conversor(1, img_teste, 'teste')
    print()

    # Geracao do arquivo Cuif.2, converte o arquivo Cuif.2 em BMP, e calcula o PSNR
    conversor(2, img, 'mandril')
    conversor(2, img_teste, 'teste')
    print()

    # Geracao do arquivo Cuif.3, converte o arquivo Cuif.3 em BMP, e calcula o PSNR
    conversor(3, img, 'mandril')
    conversor(3, img_teste, 'teste')
    print()

    # Geracao do arquivo Cuif.4, converte o arquivo Cuif.4 em BMP, e calcula o PSNR
    conversor(4, img, 'mandril')
    conversor(4, img_teste, 'teste')
    print()

    size_mandril = os.path.getsize("mandril.bmp")  
    print("Mandril")
    for i in range(1,5):      
        size_mandril_dec = os.path.getsize(f"imgs_mandril/mandril{i}.cuif")
        print(f"Comp {i} = {size_mandril/size_mandril_dec:.5f}")

    size_teste = os.path.getsize("teste.bmp")  
    print("\nTeste")
    for i in range(1,5):      
        size_teste_dec = os.path.getsize(f"imgs_teste/teste{i}.cuif")
        print(f"Comp {i} = {size_teste/size_teste_dec:.5f}")


    print("THE END")

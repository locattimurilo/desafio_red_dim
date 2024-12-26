from PIL import Image


def escala_cinza(colorida):
    larg, alt = colorida.size
    img_cinza = Image.new("L", (larg, alt))  # Modo 'L' para escala de cinza

    for x in range(larg):
        for y in range(alt):
            pxl = colorida.getpixel((x, y))
            # Coordenadas RGB
            val_rgb = int(0.299 * pxl[0] + 0.587 * pxl[1] + 0.114 * pxl[2])
            img_cinza.putpixel((x, y), val_rgb)
    
    return img_cinza

if __name__ == "__main__":
    robo = Image.open("robo.jpg")
    robo_pb = escala_cinza(robo)
    robo_pb.save("pb_robo.jpg")
    robo_pb.show() 


def img_bin(imagem_cinza, limiar=127):
   
    larg, alt = imagem_cinza.size
    imagem_binaria = Image.new("1", (larg, alt))  

    for y in range(alt):
        for x in range(larg):
            valor_cinza = imagem_cinza.getpixel((x, y))  
            valor_binario = 1 if valor_cinza > limiar else 0  
            imagem_binaria.putpixel((x, y), valor_binario)  

    return imagem_binaria

if __name__ == "__main__":
    
    imagem_cinza = Image.open("robo.jpg").convert("L")    
    imagem_binaria = img_bin(imagem_cinza, limiar=127)    
    imagem_binaria.save("robo_bin.jpg")
    imagem_binaria.show()
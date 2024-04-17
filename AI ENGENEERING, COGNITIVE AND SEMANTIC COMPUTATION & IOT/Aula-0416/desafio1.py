import cv2
import numpy as np
 
# Carrega uma imagem
# Neste caso estamos criando uma imagem RGB preta de tamanho 480x640
img = np.zeros((480, 640, 3), dtype="uint8")
  
# Exibe a imagem
cv2.imshow('image', img)

count = 0

# Função de callback, quando ocorre um evento do mouse, essa função é chamada
def mouse_click(event, x, y, flags, param):
    global img
    global count
    # Se foi o botão esquerdo do mouse 

    if event == cv2.EVENT_MBUTTONDOWN:
          
         # ---------- implemente a solução...  
            print(f"Variável contadora: {count}")
            if count == 0:
                img[:,:] = [0,0,255]
                cv2.imshow('image', img)
                count += 1 
            elif count == 1:
                img[:,:] = [0,255,0]
                cv2.imshow('image', img)
                count += 1 
            else:
                img[:,:] = [255,0,0]
                cv2.imshow('image', img)
                count += 1
                count = 0            
        
# Seta a função de callback que será chamada 
# Evento 'image', função callback mouse_click  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)
  
# fecha a janela.
cv2.destroyAllWindows()
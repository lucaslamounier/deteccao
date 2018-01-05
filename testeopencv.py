import cv2

print(cv2.__version__)

imagem = cv2.imread('opencv-python.jpg') # carrega a imagem
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Converte a imagem para escala de cinza.
cv2.imshow("Original", imagem) # apresenta a imagem carregada
cv2.imshow("Cinza", imagemCinza) # apresenta a imagem carregada em escala de cinza
cv2.waitKey() # fecha a janela quando apertado alguma tecla.

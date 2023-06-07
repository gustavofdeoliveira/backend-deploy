# ----------------------------------
# Esse arquivo tem como objetivo apenas demonstrar um exemplo de como utilizar o modelo treinado para analisar um vídeo ao vivo.
# ----------------------------------
# Importando as bibliotecas necessárias
from ultralytics import YOLO
import cv2 as cv

# Carrengado o modelo treinado
model = YOLO('./model.pt')

# Capturando o video com o OpenCV
cap = cv.VideoCapture(0)

# Loop para ficar analisando o video ao vivo
while True:
   _, frame = cap.read()
   # Fazendo a predição com uma confiança mínima de 60%
   result = model.predict(frame, conf=0.6)
   # Mostrando o resultado na tela
   cv.imshow('frame', result[0].plot())
   # Se apertar a tecla 'q' o programa para
   if cv.waitKey(1) == ord('q'):
      break

cap.release()
cv.destroyAllWindows()
from math import dist
import time
import numpy as np
import dlib
import cv2



# definir constantes
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 40
COUNTER = 0

def eye_aspect_ratio(eye):
    # calcula a distancia euclidiana vertical os olhos
    # vertical eye landmarks (x, y)-coordinates
    A = dist(eye[1], eye[5])
    B = dist(eye[2], eye[4])

    # # calcula a distancia euclidiana horizontal os olhos
    # eye landmark (x, y)-coordinates
    C = dist(eye[0], eye[3])

    # calcula uma taxa de abertura dos olhos
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear


# inicializa o detector e preditor do dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# pega os índices do previsor, para olhos esquerdo e direito
(lStart, lEnd) = (42, 48)
(rStart, rEnd) = (36, 42)

# inicializar vídeo
vs = cv2.VideoCapture(0)


# loop sobre os frames do vídeo
while True:
    ret, frame = vs.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detectar faces (grayscale)
    rects = detector(gray, 0)

    # loop nas detecções de faces
    for rect in rects:
        
        shape = predictor(gray, rect)
        #devolve shape em uma lista coords
        coords = np.zeros((shape.num_parts, 2), dtype=int)
        for i in range(0,68): #São 68 landmark em cada face
            coords[i] = (shape.part(i).x, shape.part(i).y)

        # extrair coordenadas dos olhos e calcular a proporção de abertura
        leftEye = coords[lStart:lEnd]
        rightEye = coords[rStart:rEnd]
        
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # ratio média para os dois olhos
        ear = (leftEAR + rightEAR) / 2.0

        # convex hull cria um contorno com base nos pontos 
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # checar ratio x threshold
        if ear < EYE_AR_THRESH:
            COUNTER += 1

            # dentro dos critérios
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame, "[ALERTA] FADIGA!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # caso acima do threshold, resetar o contador e desligar o alarme
        else:
            COUNTER = 0
            # desenhar a proporção de abertura dos olhos
        cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Exibe resultado
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    # tecla para sair do script "q"
    if key == ord("q"):
        break

# clean
cv2.destroyAllWindows()
vs.release()    
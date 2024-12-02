import cv2
from distance_utils import calculate_distance, find_object

# Constante de largura
REAL_WIDTH = 6.0

# Distância de referência
KNOWN_DISTANCE = 50.0

focal_length = None 

# Iniciando câmera:
cap = cv2.VideoCapture(0)

print("Posicione o objeto na distância conhecida:")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Referência", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        roi = find_object(frame)
        if roi:
            _, _, object_width, _ = roi
            focal_length = (object_width * KNOWN_DISTANCE) / REAL_WIDTH
            print(f"Focal Length Calculada: {focal_length:.2f}")
            break

# Validação de `focal_length`
if focal_length is None:
    print("Erro: Não foi possível calcular a distância focal. Verifique se o objeto foi detectado corretamente.")
    cap.release()
    cv2.destroyAllWindows()
    exit()  # Saída de emergência

# Front da Distância:
print("Distância em Tempo Real:")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    roi = find_object(frame)
    if roi:
        x, y, object_width, h = roi
        if focal_length:
            distance = calculate_distance(REAL_WIDTH, focal_length, object_width)
            cv2.rectangle(frame, (x, y), (x + object_width, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"Distance: {distance:.2f} cm", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)


    cv2.imshow("Distância em Tempo Real", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''

2025 05. 06.

'''

import cv2
from ultralytics import YOLO

model = YOLO('yolo12n.pt') # yolo 12 n modell használata -> jobb lassabb gépekhez

# kamera megnyitása
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # olvassa be
    ret, frame = cap.read()
    if not ret:
        break

    # a modell csinálja a nehezét
    results = model(frame)
    r = results[0]

    for box in r.boxes:
        # minden dologhoz tegyen egy téglalapot és egy címkét
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        conf = float(box.conf[0])
        cls  = int(box.cls[0])
        label = model.names[cls]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(
            frame,
            f"{label} {conf:.2f}", # + biztosság
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0,255,0), 2
        )
    # és a végén megjelenítjük
    cv2.imshow('YOLOv12n Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# a végén engedje el a memóriát, és zárjon be minden ablakot
cap.release()
cv2.destroyAllWindows()

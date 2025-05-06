## YOLOv12n Real-Time Object Detection

This project uses the YOLOv12n model for real-time object detection via webcam, optimized for slower machines.

📦 Requirements

Install the dependencies using pip:

    pip install ultralytics opencv-python

Ensure you have a compatible YOLOv12n model file : yolo12n.pt.

🚀 How to Run

    python main.py

Replace detect.py with your script filename if different.
The program will:

  - Open your webcam.

  - Use YOLOv12n to detect objects.

  - Draw bounding boxes and labels with confidence scores.

  - Display the result in a window.

  - Press Q to exit the window.

🧠 Model Info

    yolo12n.pt is a lightweight YOLOv12 model ideal for devices with low computational power.

    Adjust or change the model path if you have a different version.

🛠 Notes

    This example uses cv2.VideoCapture(0), which captures from the default webcam. Change the index if needed.

    Ensure your webcam is connected and accessible.

    Tested with Ultralytics ultralytics library version >=8.0.

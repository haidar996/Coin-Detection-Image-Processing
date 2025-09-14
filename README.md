# Coin-Detection-Image-Processing
A Python-based coin detection system using OpenCV for image processing. Applies thresholding, morphological operations, edge detection, and Hough Circle Transform to identify and count coins in images. Demonstrates computer vision techniques for object detection.
## 🎯 Features

- 📷 Image preprocessing and grayscale conversion
- 🌓 Otsu's thresholding for automatic binarization
- ⚙️ Morphological operations: erosion, dilation, and opening
- 🪞 Edge detection using the Canny algorithm
- 🔵 Circle detection via Hough Circle Transform
- 🖼️ Visualization of results with detected coins highlighted

---

## 📦 Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

---

## 💻 Installation

Install the required libraries using `pip`:

```bash
pip install opencv-python numpy
🕹️ Usage
Place your coin image in the appropriate directory.

Update the image path in the script.

Run the script:

bash
Copy code
python coins_task.py
🔄 Process Flow
Load and convert the image to grayscale

Apply Otsu's thresholding for binarization

Perform morphological operations (e.g., opening)

Detect edges using the Canny edge detector

Apply Hough Circle Transform to detect circular shapes

Draw the detected circles on the original image

Display and save the results

📈 Results
The program outputs:

Intermediate processed images (optional)

Final image with detected coins circled

Radius values of the detected coins

🖼️ Example Output


🚀 Applications
🧮 Coin counting systems

🧪 Object detection tutorials

🎓 Educational purposes in image processing

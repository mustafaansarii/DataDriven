from flask import Flask, request, jsonify, render_template
from torchvision import models, transforms
from PIL import Image
import torch
import io

app = Flask(__name__)

# Load the pre-trained PyTorch model
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(512) # Adjust output layer to match your dataset
model.eval()

# Define image transformations
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to preprocess image and get predictions
def predict_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
    _, predicted = torch.max(outputs, 1)
    return predicted.item()

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling image upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        try:
            image_bytes = file.read()
            prediction = predict_image(image_bytes)
            # You can have a dictionary mapping class indices to class names
            class_names = {0: 'Healthy', 1: 'Disease 1', 2: 'Disease 2'}  # Update with your actual class names
            predicted_class = class_names[prediction]
            return jsonify({'prediction': predicted_class})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

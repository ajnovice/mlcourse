from flask import Flask
from keras.models import load_model
from keras.application.resnet50 import ResNet50
app = Flask(__name__)

model = ResNet50(weights='imagenet')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def upload():
	if request.method == 'POST':
		f = request.files('file')
		f.save(file_path)
		preds = model_predict(file_path,model)
		pred_class  = decode_predictions(preds,top=1)
		return pred_class
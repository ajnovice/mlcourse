from keras.models import load_model
from keras.application.resnet50 import ResNet50

model = ResNet50(weights='imagenet')

def model_predict(img_path,model):
	img = load_img(img_path)
	img_array = img_to_array(img)
	preds = model.predict(img_array)
	return preds

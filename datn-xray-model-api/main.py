from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import torch
import imageio
from PIL import Image
from torchvision import transforms
import base64
import numpy as np
from waitress import serve
from heatmap import HeatmapGenerator
from densenet121 import DenseNet121

app = Flask(__name__)
api = Api(app)

img_post_args = reqparse.RequestParser()
img_post_args.add_argument("imgb64", type=str, help="B64 of the image is required")

# Load model
device = torch.device("cpu")
model = torch.load('densenet121_Chest14.pth', map_location=torch.device("cpu"))

mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])

data_transforms = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean, std)
])

classname = ['Emphysema', 'Hernia', 'Nodule', 'Effusion', 'Pleural_Thickening',
             'Pneumonia', 'Cardiomegaly', 'Infiltration', 'Consolidation',
             'Atelectasis', 'Pneumothorax', 'Mass', 'Edema', 'Fibrosis']

class PostImg(Resource):
    def post(self):
        pred_classname = []
        args = img_post_args.parse_args()
        imgb64 = args['imgb64']
        img_pd = base64.b64decode(imgb64)
        img_pd2 = imageio.v3.imread(img_pd)
        img_pil = Image.fromarray(img_pd2).convert('RGB')

        # Preprocess the image
        img = data_transforms(img_pil)
        img = img.unsqueeze(0)

        # Make a prediction
        with torch.no_grad():
            img = img.to(device)
            output = model(img)
            pred = output > 0.4
            pred = pred.to(torch.float32)
            pred = pred.cpu().squeeze().detach().numpy().tolist()
            for i, e in enumerate(pred):
                if e == 1.0:
                    pred_classname.append(classname[i])
        predictresult = pred_classname if pred_classname else ["No Finding"]

        # Generate heatmaps
        h = HeatmapGenerator('densenet121_Chest14.pth', 224)
        combined_hmImg, hmImgs = h.generate(img_pil, img_pd, 224, predictresult)

        # Format the result
        if "No Finding" in predictresult:
            individual_heatmap_images = [{"disease": "No Finding", "heatmap": combined_hmImg}]
        else:
            individual_heatmap_images = [{"disease": disease, "heatmap": hmImgs[disease]} for disease in predictresult if disease in hmImgs]

        # When there's only one disease, make sure the combined and individual heatmaps match
        if len(individual_heatmap_images) == 1:
            combined_hmImg = individual_heatmap_images[0]["heatmap"]

        result = {
            'combined_heatmap_image': combined_hmImg,
            'individual_heatmap_images': individual_heatmap_images,
            'predict_result': ", ".join(predictresult)
        }
        return jsonify(result)

api.add_resource(PostImg, "/predict")

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=9000, threads=3)

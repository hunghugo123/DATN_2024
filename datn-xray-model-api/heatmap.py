import numpy as np
from torch.nn import functional as F
from torch.autograd import Variable
import cv2
import base64
import torch
import torchvision.transforms as transforms
from densenet121 import DenseNet121


class HeatmapGenerator():
    def __init__(self, pathModel, transCrop, num_classes=14):
        # ---- Initialize the network
        model = torch.load(pathModel, map_location=torch.device("cpu"))
        model = torch.nn.DataParallel(model).to("cpu")
        self.model = model.module.densenet121.features
        # ---- Initialize the weights
        self.weights = list(self.model.parameters())[-2]
        # ---- Initialize the image transform - resize + normalize
        normalize = transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        transformList = [transforms.Resize(transCrop), transforms.ToTensor(), normalize]
        self.transformSequence = transforms.Compose(transformList)
        # Number of classes
        self.num_classes = num_classes

    def generate(self, imagePil, imageOri, transCrop, predictresult):
        # ---- Load image, transform, convert
        imageData = self.transformSequence(imagePil)
        imageData = imageData.unsqueeze_(0)
        input = torch.autograd.Variable(imageData)

        self.model.to("cpu")
        output = self.model(input.to("cpu"))

        # ---- Generate individual heatmaps
        heatmaps = []
        combined_heatmap = None
        for i in range(self.num_classes):
            map = output[0, i, :, :]
            heatmap = self.weights[i] * map
            heatmap = F.relu(Variable(heatmap))
            npHeatmap = heatmap.cpu().data.numpy()
            npHeatmap -= npHeatmap.min()
            if npHeatmap.max() != 0:
                npHeatmap /= npHeatmap.max()
            cam = cv2.resize(npHeatmap, (transCrop, transCrop))
            heatmaps.append(cam)
            if combined_heatmap is None:
                combined_heatmap = cam
            else:
                combined_heatmap += cam

        # Normalize combined heatmap
        if combined_heatmap.max() != 0:
            combined_heatmap = combined_heatmap / np.max(combined_heatmap)
        combined_heatmap = cv2.resize(combined_heatmap, (transCrop, transCrop))

        # Decode the original image
        nparr = np.frombuffer(imageOri, np.uint8)
        imgOriginal = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        imgOriginal = cv2.resize(imgOriginal, (transCrop, transCrop))

        # Encode individual heatmaps
        imgstrs = {}
        for i, cam in enumerate(heatmaps):
            if "No Finding" in predictresult:
                combined_heatmap = cv2.resize(combined_heatmap,
                                              (transCrop, transCrop))  # Uniform blue color for No Finding
                combined_heatmap = combined_heatmap * 0 + 0.12345223
                heatmap = cv2.applyColorMap(np.uint8(255.0 * cam), cv2.COLORMAP_JET)

            else:
                heatmap = cv2.applyColorMap(np.uint8(255.0 * cam), cv2.COLORMAP_JET)

            img = heatmap.astype(np.float64) + imgOriginal.astype(np.float64)
            img = img / img.max() * 255.0
            retval, buffer = cv2.imencode('.jpg', img)
            img_base64 = base64.b64encode(buffer).decode("utf-8")
            if i < len(predictresult) and predictresult[i] != "No Finding":
                imgstrs[predictresult[i]] = img_base64

        # Encode combined heatmap
        combined_heatmap_colormap = cv2.applyColorMap(np.uint8(255.0 * combined_heatmap), cv2.COLORMAP_JET)
        combined_img = combined_heatmap_colormap.astype(np.float64) + imgOriginal.astype(np.float64)
        combined_img = combined_img / combined_img.max() * 255.0
        retval, buffer = cv2.imencode('.jpg', combined_img)
        combined_img_base64 = base64.b64encode(buffer).decode("utf-8")

        # Return combined heatmap and individual heatmaps
        return combined_img_base64, imgstrs

from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
from utils import *
#from featureExtractor import *

def feature_extractor_unittest(imgPath):
  """
  This is a unit test function for feature extractor
  """
  imgFiles = [f for f in listdir(imgPath) if isfile(join(imgPath, f))]

  for f in imgFiles:
    img = cv2.imread(imgPath+f)
    grayImg = convert_to_gray(img)
    (_,features1) = sift_features(grayImg)
    (_,features2) = orb_features(grayImg)
    has_nan = np.isnan(features1).any()
    has_nan = np.isnan(features2).any()
    if has_nan:
      raise ValueError("Featues1 has nan!")
    if has_nan:
      raise ValueError("Features2 has nan!")
      
      
 imgPath = ""
 feature_extractor_unittest(imgPath)

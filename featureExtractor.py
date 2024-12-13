import cv2
import numpy as np
#import matplotlib.pyplot as plt

def sift_features(img):
  """
  This function extractor SIFT features and its locations
  """
  sift = cv2.SIFT_create()
  keyPoints, descriptors = sift.detectAndCompute(img, None)
  return keyPoints, descriptors

def orb_features(img):
  """
  This function extractor orb features and its locations
  """
  orb = cv2.ORB_create()
  keyPoints, descriptors = orb.detectAndCompute(img, None)
  return keyPoints, descriptors

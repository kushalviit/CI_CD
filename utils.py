import cv2
import numpy as np
import matplotlib.pyplot as plt

def convert_to_gray(img):
  """
  This function converts image to gray scale
  """
  gray_image= cv2.Canny(img, cv2.COLOR_BGR2GRAY)
  return gray_image

def gray_to_cannydge(img, uprThr, lwrThr):
  """
  This function extractor image to canny edge
  """
  edges = cv2.Canny(img, uprThr, lwrThr)
  return edges

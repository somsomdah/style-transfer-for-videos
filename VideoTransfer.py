import tensorflow as tf
import numpy as np
import cv2

from style_transfer import StyleTransfer
from image_segmentation import ImageSegmentation

cap=cv2.VideoCapture("./samples/video001_edit.mp4")

frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size=(frame_width,frame_height)

width=frame_width//2
height=frame_height//2

fourcc=cv2.VideoWriter_fourcc(*'DIVX')
out=cv2.VideoWriter("./results/veido001_result_5.mp4",fourcc,24,frame_size)
#out=cv2.VideoWriter("./results/veido001_result.mp4",fourcc,24,(width,height))

#style_transfer=StyleTransfer(width,height)
style_transfer=StyleTransfer(frame_width,frame_height)
style_transfer.load()
style_transfer.change_style(0)
#image_segmentation=ImageSegmentation(width,height)
image_segmentation=ImageSegmentation(frame_width,frame_height)

while True:
     retval,frame=cap.read()
     
     if not retval:
          break

     #resized_image=cv2.resize(frame,(width,height))
     
     #style_image=style_transfer.predict(resized_image)
     #seg_mask=image_segmentation.predict(resized_image)
     style_image=style_transfer.predict(frame)
     seg_mask=image_segmentation.predict(frame)
     
     seg_mask = cv2.cvtColor(seg_mask, cv2.COLOR_GRAY2RGB)

     #result_image = np.where(seg_mask, style_image, resized_image)
     result_image = np.where(seg_mask, style_image, frame)

     cv2.imshow("result",result_image)
     out.write(result_image)

     key=cv2.waitKey(30)
     if key==32:
          break
     

cap.release()
out.release()
cv2.destroyAllWindows()

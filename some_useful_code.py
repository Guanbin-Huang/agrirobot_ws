import cv2
bb = self.primaryRGBImg
for xy_coord in plantsInCropRow:
    _x, _y = xy_coord
    cv2.circle(bb, (_x, _y), radius = 5, color=(255,0,0), thickness = 5)

cv2.line(bb, (t_i, 0), (b_i, 475), color=(0,0,255), thickness = 2)
cv2.rectangle(bb, (51, 0), (210, 480), color, thickness = 2)
cv2.imwrite("bb.jpg",bb)


xx, yy = poly.exterior.coords.xy

from shapely.geometry import Polygon
poly1 = Polygon( [[0, 0], [1,0], [1,1], [0,1] ] )
poly2 = Polygon( [(0, 0), (1,0), (1,1), (0,1) ] )

print(poly1.wkt)
print(poly2.wkt)


import cv2
import numpy as np
# black = np.zeros((480, 640, 3))
current_img = self.primaryRGBImg
for pair in [[(boxBR_x, boxB_y), (boxBL_x, boxB_y)],
             [(boxBL_x, boxB_y), (boxTL_x, boxT_y)],
             [(boxTL_x, boxT_y), (boxTR_x, boxT_y)],
             [(boxTR_x, boxT_y), (boxBR_x, boxB_y)]]:

    cv2.line(current_img, (int(pair[0][0]), int(pair[0][1])), (int(pair[1][0]), int(pair[1][1])), color=(0,0,255), thickness = 2)
cv2.imwrite("current_img.jpg",current_img)





# import cv2
# current_img = self.primaryRGBImg
# for xy in [     (boxBR_x, boxB_y),
#                 (boxBL_x, boxB_y),
#                 (boxTL_x, boxT_y),
#                 (boxTR_x, boxT_y)]:
#     x, y = xy
#     cv2.circle(current_img, (int(x),int(y)), radius = 5, color=(255,255,255), thickness = 5)

# cv2.imwrite("current_img.jpg",current_img)
            


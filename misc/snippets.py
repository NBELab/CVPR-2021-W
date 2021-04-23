import numpy as np
import cv2

# Save event data as point cloud in XYZ format for visualization
# can be visualized using MeshLab (XYZRGB)
def SaveEvents(data):
    pts = np.zeros((data.x.shape[0],6), np.float32)
    pts[:,0] = data.x
    pts[:,1] = data.y
    pts[:,2] = data.ts*1e-3 # in msec
    pts[:,5] = (data.p).astype(float)*255
    pts[:,3] = (data.p==False).astype(float)*255
    np.savetxt('events.txt',pts, fmt='%d;%d;%f;%d;%d;%d')

# Save image of events
# Note: OpenCV inverts B and R channels, therefore we assign
# td_img is the events summed for a single frame
# frame_idx stores frame index: [0,num_frames)
tmp = np.zeros((145, 233, 3), np.uint8) # hardcoded, but can easily be generalized
tmp[..., 0] = (td_img > 0)*255
tmp[..., 2] = (td_img < 0)*255
cv2.imwrite(f'frame_{frame_idx}.png', tmp)


# save OBJ file with textured coordinates to visualize image in 3D
# additionaly, MTL file should be
'''
newmtl Mat
   Kd 1.000 1.000 1.000
   map_Kd frame_5.png
'''
with open(f'frame3d_{frame_idx}.obj', 'w') as f:
    f.write(f'mtllib netmat5.mtl\n')
    f.write(f'usemtl  Mat\n')
    f.write(f'v {frame_xmin} {frame_ymin} {frame_end*1e-3}\n')
    f.write(f'v {frame_xmin} {frame_ymax} {frame_end*1e-3}\n')
    f.write(f'v {frame_xmax} {frame_ymax} {frame_end*1e-3}\n')
    f.write(f'v {frame_xmax} {frame_ymin} {frame_end*1e-3}\n')
    f.write('vt 0 1\n')
    f.write('vt 0 0\n')
    f.write('vt 1 0\n')
    f.write('vt 1 1\n')
    f.write('f 1/1 2/2 3/3 \n')
    f.write('f 3/3 4/4 1/1 \n')

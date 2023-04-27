import numpy as np
from tqdm import tqdm
import math
from PIL import Image
import os
def imread(path):
    label = np.array(Image.open(path))
    return label

def get_palette():
    unlabelled = [0, 0, 0]
    car = [64, 0, 128]
    person = [64, 64, 0]
    bike = [0, 128, 192]
    curve = [0, 0, 192]
    car_stop = [128, 128, 0]
    guardrail = [64, 64, 128]
    color_cone = [192, 128, 128]
    bump = [192, 64, 0]
    palette = np.array(
        [
            unlabelled,
            car,
            person,
            bike,
            curve,
            car_stop,
            guardrail,
            color_cone,
            bump,
        ]
    )
    return palette

def visualize(save_name, label):
    palette = get_palette()
    pred = label
    img = np.zeros((pred.shape[0], pred.shape[1], 3), dtype=np.uint8)
    for cid in range(1, int(label.max())):
        img[pred == cid] = palette[cid]
    img = Image.fromarray(np.uint8(img))
    img.save(save_name)

if __name__ == '__main__':
    label_dir = r'./test/Segmentation_labels' #label所在文件夹
    save_dir = r'./test/Segmentation_visualize' ## 可视化结果保存的文件夹
    os.makedirs(save_dir, exist_ok=True)
    file_list = os.listdir(label_dir)
    for item in file_list:
        file_path = os.path.join(label_dir, item)
        save_path = os.path.join(save_dir, item)
        label = imread(file_path)
        visualize(save_path, label)
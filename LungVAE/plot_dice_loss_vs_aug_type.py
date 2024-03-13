from pathlib import Path
from os import listdir
from PIL import Image
from numpy import asarray, multiply, sum, mean
import matplotlib.pyplot as plt


def dice_coef(y_true, y_pred):
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = multiply(y_true_f, y_pred_f)
    intersection = sum(intersection)
    return (2. * intersection + 1) / (sum(y_true_f) + sum(y_pred_f) + 1)

predicted_path_raw = '../../results/pred_20220614_16_57/'
truth_path_raw = '../../data/masks/'

predicted_path = Path(predicted_path_raw)
truth_path = Path(truth_path_raw)
size = (128, 128)

augtype_to_file_prefix = [
    'Contrast',
    'RandomAffine',
    'RandomBiasField',
    'RandomFlip',
    'RandomGhosting',
    'Original'
]
augtype_to_description = [
    'augmentation 0',
    'augmentation 1',
    'augmentation 2',
    'augmentation 3',
    'augmentation 4',
    'original'
]
augtype_to_color = [
    'red',
    'blue',
    'green',
    'yellow',
    'brown',
    'orange'
]

if __name__ == '__main__':

    predicted_list = [p for p in listdir(predicted_path) if 'post' in p]
    truth_list = listdir(truth_path)
    
    input = []
    target = []
    augtypes = []

    for path in predicted_list:
        path = str(path)
        name = path.split('\\')[-1][:-14] + '_mask.png'
        if name not in truth_list:
            name = path.split('\\')[-1][:-14] + '.png'            
        if name in truth_list:
            inp = asarray(Image.open(f'{predicted_path_raw}{path}').resize(size).convert('L'))
            tar = asarray(Image.open(str(Path(truth_path_raw + name))).resize(size).convert('L'))

            augtype = None
            for a, prefix in enumerate(augtype_to_file_prefix):
                if name.startswith(prefix):
                    augtype = a
                    break

            augtypes.append(augtype)
            input.append(inp / 255)
            target.append(tar / 255)

    augtype_to_results = [[] for _ in range(6)]

    mean_coeff = 0
    for i, t, a in zip(input, target, augtypes):
        if a == None:
            continue
        res = dice_coef(i, t)
        mean_coeff += res
        augtype_to_results[a].append(res)

    mean_coeff /= len(input)
    print(f"Mean dice coeff: {mean_coeff} (on {len(input)} samples)")
    fig, axs = plt.subplots(2, 3, figsize=(10,10))

    for i in [0,1]:
        for j in [0,1,2]:
            a = i*3+j
            axs[i,j].hist(augtype_to_results[a], bins=30, color=augtype_to_color[a])
            axs[i,j].set_title(augtype_to_description[a])

    max_top_ylim = max([axs[i,j].get_ylim()[1] for i in [0,1] for j in [0,1,2]])

    for i in [0,1]:
        for j in [0,1,2]:
            a = i*3+j
            axs[i,j].set_ylim((0, max_top_ylim))
            axs[i,j].set_xlim((0.0, 1.0))
            axs[i,j].vlines(mean(augtype_to_results[a]), 0.0, max_top_ylim, colors='k', linestyles='dashed')

    fig.text(0.5, 0.04, 'dice coefficient', ha='center')
    fig.text(0.04, 0.5, 'number of samples', va='center', rotation='vertical')
    plt.savefig('plot.pdf')
    plt.show()

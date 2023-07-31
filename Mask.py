import cv2
import numpy as np
import pyautogui as ag
import pandas as pd


# считываем картинки в виде numpy array
large_image = cv2.imread('Путь/большая_картинка.png')
small_image = cv2.imread('Путь/малая картинка.png')

# преобразуем 3-мерный numpy array в 2-мерный
all_rgb_codes = small_image.reshape(-1, small_image.shape[-1])
all_rgb_codes_big = large_image.reshape(-1, large_image.shape[-1])

# выделяем уникальные пиксели, подсчитываем количество повторений
Unique, count = np.unique(all_rgb_codes, axis=0, return_counts=True)
UniqueBig, countBig = np.unique(all_rgb_codes_big, axis=0, return_counts=True)

# объединяем массивы уникальных точек и количества повторений в один массив
UniqueS = np.hstack((Unique, count.reshape(Unique.shape[0], 1)))
UniqueB = np.hstack((UniqueBig, countBig.reshape(UniqueBig.shape[0], 1)))

# преобразуем массивы numpy array в pandas df
dfS = pd.DataFrame(UniqueS, columns=['B', 'R', 'G', 'frequency'])
dfB = pd.DataFrame(UniqueB, columns=['B', 'R', 'G', 'frequency'])

# анализируем пиксели малой картинки, находим частоту таких пикселей на большой картинке
mergedDF = pd.merge(dfS, dfB, on=['B', 'R', 'G'], how='left', suffixes=('_1', '_2'))

# находим пиксели, частота которых на большой и малой картинках совпадают
common_pixels = mergedDF.loc[mergedDF['frequency_1'] == mergedDF['frequency_2']]

# если пикселей с совпадающей частотой на двух картинках больше одной, и расстояние между ними на большой
# и на малой картинке совпадают, то малая картинка является частью большой
if len(common_pixels) > 1:
    pixel0 = common_pixels.iloc[0, :3].tolist()
    pixel1 = common_pixels.iloc[1, :3].tolist()
    Y0, X0 = np.min(np.where(np.all(large_image == pixel0, axis=2)), axis=1)
    y0, x0 = np.min(np.where(np.all(small_image == pixel0, axis=2)), axis=1)
    Y1, X1 = np.min(np.where(np.all(large_image == pixel1, axis=2)), axis=1)
    y1, x1 = np.min(np.where(np.all(small_image == pixel1, axis=2)), axis=1)
    if (Y0 - y0) == (Y1 - y1) and (X0 - x0) == (X1 - x1):
        centerX, centerY = (X0 - x0 + int(small_image.shape[1] / 2), Y0 - y0 + int(small_image.shape[0] / 2))
        cv2.circle(large_image, (centerX, centerY), int(small_image.shape[1] / 1.5), (0, 0, 255), 3)
        cv2.imshow("Image", large_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('Искомого кадра нет на экране')
else:
    print('Искомого кадра нет на экране')

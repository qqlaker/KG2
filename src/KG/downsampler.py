from KG.image import Image


def downsample_neighbour(new_width, new_height, 
                         img: Image) -> Image:
    width, height = img.img_size
    result_matrix = [0] * (new_width * new_height)

    scale_x = width / new_width
    scale_y = height / new_height

    for y in range(new_height):
        for x in range(new_width):
            index = y * new_width + x

            src_x = int(x * scale_x)
            src_y = int(y * scale_y)

            result_matrix[index] = img.img_matrix[src_y * width + src_x]

    img.img_matrix = result_matrix
    img.img_size = (new_width, new_height)
    return img
    
def bicubic_interpolation(x, y, width, img_matrix) -> int:
    # вычисляем координаты центрального пикселя
    cx, cy = width / 2, len(img_matrix) / (2 * width)

    # вычисляем коэффициенты для интерполяции
    a = -0.5
    f = [0] * 16
    for i in range(4):
        for j in range(4):
            x_diff = abs(i - 1.5)
            y_diff = abs(j - 1.5)
            if x_diff < 1 and y_diff < 1:
                f[i * 4 + j] = ((a + 2) * abs(x_diff) ** 3 - (a + 3) * abs(x_diff) ** 2 + 1) * ((a + 2) * abs(y_diff) ** 3 - (a + 3) * abs(y_diff) ** 2 + 1)
            else:
                f[i * 4 + j] = 0

    # соседние пиксели
    x1, x2 = int(x), int(x) + 1
    y1, y2 = int(y), int(y) + 1

    # вычисление значений пикселей в окрестности целевой точки
    values = [0] * 16
    for i in range(4):
        for j in range(4):
            px = x1 + i - 1
            py = y1 + j - 1
            if px >= 0 and px < width and py >= 0 and py * width < len(img_matrix):
                values[i * 4 + j] = img_matrix[py * width + px]
            else:
                values[i * 4 + j] = 0

    # вычисление значения в целевой точке с помощью бикубической интерполяции
    dx = x - x1
    dy = y - y1
    interpolated_value = sum([f[i] * values[i] for i in range(16)]) / sum([f[i] for i in range(16)])

    return interpolated_value

def downsample_interpoll(new_width, new_height, 
                         img: Image) -> Image:
    width, height = img.img_size
    new_image_list = [0] * (new_width * new_height)

    scale_x = float(width) / float(new_width)
    scale_y = float(height) / float(new_height)

    for i in range(new_height):
        for j in range(new_width):
            # коорды пикселя в исходном изображении
            x = j * scale_x
            y = i * scale_y
            
            # бикубическая интерполяция
            new_image_list[i * new_width + j] = \
                bicubic_interpolation(x, y, img.img_size[0], img.img_matrix)

    img.img_matrix = new_image_list
    img.img_size = (new_width, new_height)
    return img

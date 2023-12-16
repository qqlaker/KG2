# Лабораторная работа №3: "Уменьшение изображений"

Реализовать уменьшение изображений первым способом: распределить пиксели исходног изображения по новому, а затем интерполировать полученные значения
1) методом ближайшего соседа;
2) методом бикубической интерполяции
---

[Класс Image](https://github.com/qqlaker/KG2/blob/main/src/KG/image.py)

[Реализация преобразователей](https://github.com/qqlaker/KG2/blob/main/src/KG/downsampler.py)

[Входные данные](https://github.com/qqlaker/KG2/tree/main/src/KG/input)

[Результат](https://github.com/qqlaker/KG2/tree/main/src/KG/output_2)

## Tests

Изначальная картинка
![](https://github.com/qqlaker/KG2/blob/main/src/KG/input/test_logo.png)

После уменьшения методом ближайшего соседа (200x200)

![](https://github.com/qqlaker/KG2/blob/main/src/KG/output_2/neighbour.png)

После уменьшения методом бикубической интерполяции (100x100)

![](https://github.com/qqlaker/KG2/blob/main/src/KG/output_2/interpoll.png)

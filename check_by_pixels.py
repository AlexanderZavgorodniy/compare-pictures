from PIL import Image

def pixels_by_img(name):
    img = Image.open( name, 'r' ) # создаст картинку из файла
    img.load()                                # форсировать чтение файла
    print( img.format, img.size, img.mode )   # данные по файлу

    if img.mode != 'RGB':          # bmp может по разному кодировать цвета
                                   # если используется режим
                                   # отличный от RGB, то в данных будут
                                   # либо индекс палитры (mode=p)
                                   # либо оттенок серого (один байт на пиксель mode=L)
                                   # либо ещё что то (mode=1 у меня нет такой картинки)

        img = img.convert( 'RGB' ) # сконвертирует эти форматы в 'RGB'

    pixels = img.getdata()                    # получить пиксели (возвращает класс `ImagingCore`)
    pix3 = list( pixels )
    return pix3

def is_equal(l1,l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

l1 = pixels_by_img("1.png")
l2 = pixels_by_img("2.png")
print(is_equal(l1,l2))

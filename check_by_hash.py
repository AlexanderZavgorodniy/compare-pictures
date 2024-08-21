import hashlib

from PIL import Image

import io


def hash_by_img(name):
    img = Image.open(name)

    m = hashlib.md5()

    with io.BytesIO() as memf:

        img.save(memf, 'PNG')

        data = memf.getvalue()

        m.update(data)

    return m.hexdigest()


l1 = hash_by_img("1.png")
l2 = hash_by_img("2.png")
print(l1==l2)


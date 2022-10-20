from PIL import Image, ImageChops;
import os;


def uses_transparency(filename):
    img = Image.open(filename);
    trans = img.info.get("transparency", None);
    if trans is not None:
        trans *= 3; # convert color number to palette table index
        palette = img.getpalette();
        imgs = [];
        for bg in [0, 255]:   # map transparent color first to black, then white
            palette[trans:trans+3] = [bg] * 3;
            img.putpalette(palette);
            imgs.append(img.convert("L"));
        return bool(ImageChops.difference(*imgs).getbbox());
    return False;

def img_transparency(filename):
    img = Image.open(filename1);
    if img.mode == "RGBA" or "transparency" in img.info:
        return True;
    else:
        return False;

for name in os.listdir('./all-image'):
    file, file_extension = os.path.splitext(name);
    filename1 = f'./all-image/{name}';

    if(file_extension == '.gif'):
        result = uses_transparency(filename1);
        if file.split('_')[0].capitalize() == f'{result}':
            print('Passed');
        else:
            print(f'Failed => {name}')

    if(file_extension == '.png'):
        result = img_transparency(filename1);
        if file.split('_')[0].capitalize() == f'{result}':
            print('Passed');
        else:
            print(f'Failed => {name}')






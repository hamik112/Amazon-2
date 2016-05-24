import shlex
from pytesser import *
image = Image.open('./img/Captcha_ermhqnhhrc.jpg')
print image_to_string(image)

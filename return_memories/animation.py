import os

import numpy as np
import cv2
from manim import *

IMAGE_DIR  = "./assets/"
IMAGE_SIZE = 890

def image_center_crop(img):
    """
    Makes a square center crop of an img, which is a [h, w, 3] numpy array.
    Returns [min(h, w), min(h, w), 3] output with same width and height.
    For cropping use numpy slicing.
    """
    img = np.asarray(img)

    shape = img.shape
    dim = len(shape)

    if dim == 3:
        h, w, c = shape
    else:
        h, w = shape

    h_crop = min(h, w)

    if dim == 3:
        cropped_img = img[
            # ...,
            (h // 2 - h_crop // 2) : (h // 2 + h_crop // 2),
            (w // 2 - h_crop // 2) : (w // 2 + h_crop // 2),
            :,
        ]
    else:
        # For our case, this is wrong
        raise ValueError("YOu have done a mistake in reading the image. Read it as RGB!!!")
        # cropped_img = img[
        #     ...,
        #     (h // 2 - h_crop // 2) : (h // 2 + h_crop // 2),
        #     (w // 2 - h_crop // 2) : (w // 2 + h_crop // 2),
        # ]

    return cropped_img

def get_all_images():
    imgfiles = os.listdir(IMAGE_DIR)
    imgfiles.sort()
    imgs = Group()
    for imgfile in imgfiles:
        img = cv2.imread(os.path.join(IMAGE_DIR, imgfile))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = image_center_crop(img)
        img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
        imgs.add(ImageMobject(img))
    return imgs

class Memories(Scene):
    def construct(self):
        background_frame = Rectangle(height=config.frame_height, width=config.frame_width)
        imgs  = get_all_images()
        texts = [
            "Floor Gang Hu!",
            "WTF!",
            "Shreyanshi He He...",
            "Fisrt pizza party!!!",
            "Ghodo in his habitat",
            "3 Idiots!",
            "3 Idiots Again!",
            "Holi beta, masti nahi!",
            "WTF Part 2",
            "WTF Part 3",
            "High ho riya!",
            "Cool Dudes!",
            "Urvashi, urvashi, take it easy, urvashi",
            "haha",
            "haha haha",
            "Go Mad, Go Stupid",
            "Guy on the left has a project to do HIMSELF!!",
            "Aaaa karo!!",
            "Mad boi!",
            "Mad Boi Part 2",
            "Shrey Didi",
            "Colgate. Dentists ka sujhaya gaya no. 1",
            "Kuchu Kuchu Kuch... hehehe...",
            "Lipstick under my chanla!",
            "4-1 Idiots",
            "5-2 Idiots",
            "BROS",
            "BROS (Extended)",
            "Drink Water!",
            "Titli ban ke tirth uda",
            "uda uda hai kahi doooooooor!"
        ]
        texts = [Text(t) for t in texts]
        texts = VGroup(*texts)
        texts.move_to(3*UP).scale(0.8)
        imgs.scale(0.8).move_to(0.7*DOWN)
        self.play(FadeIn(imgs[0]), Write(texts[0]))
        for i in range(1, len(imgs)):
            self.play(ReplacementTransform(imgs[i-1], imgs[i]),
                      ReplacementTransform(texts[i-1], texts[i]))
            self.wait()
        self.play(FadeOut(imgs[-1]), FadeOut(texts[-1]))
        gratitude = VGroup(Tex("I owe you all an ", "astronomical", " amount"),
                           Tex("of ", "gratitude", " that I will"),
                           Tex("always be in ", "debt", " of."))
        gratitude[0][1].set_color(YELLOW)
        gratitude[1][1].set_color(GREEN)
        gratitude[2][1].set_color(BLUE)
        self.play(Write(gratitude[0].move_to(UP)))
        for i in range(1, len(gratitude)):
            self.play(Write(gratitude[i].next_to(gratitude[i-1], DOWN)))
        self.wait()

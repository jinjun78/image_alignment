from PIL import ImageEnhance

def contrast_and_brightness(img):
    # Improve contrast and brighness of the image to make it easier to be detected
    enhancer1 = ImageEnhance.Contrast(img)
    factor = 1.5
    img_con = enhancer1.enhance(factor)

    enhancer2 = ImageEnhance.Brightness(img_con)
    factor = 1.5
    img_output = enhancer2.enhance(factor)

    return img_output
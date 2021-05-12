from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/kitten.jpg')
    bordered_img = add_border(image, 15)
    bordered_img.show()

def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """

    # new height and width with surrounding border
    # add twice the border size since there is a border on both sides
    new_height = original_img.height + border_size * 2
    new_width = original_img.width + border_size * 2

    # create a new blank image object with larger size (including border)
    new_image = SimpleImage.blank(new_width, new_height)

    for x in range(new_width):
        for y in range(new_height):
            if is_border_pixel(x, y, border_size, new_image):
                # if in border, set to black
                # create a new pixel object at location before setting RGB colors
                pixel = new_image.get_pixel(x, y)
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0
            else:
                # otherwise translate offset location and copy from original
                # remember x, y is in larger, new_image
                original_x = x - border_size
                original_y = y - border_size

                # get the pixel from original image
                original_pixel = original_img.get_pixel(original_x, original_y)

                # set the pixel of new_image to the matching pixel from original_image
                new_image.set_pixel(x, y, original_pixel)

    # return our new image with surrounding border and copy of original image inside
    return new_image

def is_border_pixel(x, y, border_size, bordered_image):
    '''
    Inputs:
        - x,y: Coordinates to check whether pixel is in border
        - border_size: The thickness of the border to add around the image
        - bordered_image: Overall image

    Returns:
        True if pixel at x,y is in border
    '''

    # if top or bottom border
    if y < border_size or y >= bordered_image.height - border_size:
        return True

    # if left or right border
    if x < border_size or x >= bordered_image.width - border_size:
        return True

    # anything else is not border
    return False


if __name__ == '__main__':
    main()

def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all([-1 < rgb[0] < 256, -1 < rgb[1] < 256, -1 < rgb[2] < 256]):
        raise ValueError
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'.upper()


if __name__ == "__main__":
    #print(rgb_to_hex((128, 0, 10)))
    print(rgb_to_hex((128, 303, -10)))

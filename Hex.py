def tohex(dec):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    rest = int(dec/16)
    x = (dec%16)
    if (rest == 0):
        return digits[x]
    return tohex(rest) + digits[x]

def hex_color(red, green, blue):
    red = tohex(red)
    if len(red) < 2:
        x = "0"
        red = x + red
    green = tohex(green)
    if len(green) < 2:
        x = "0"
        green = x + green
    blue = tohex(blue)
    if len(blue) < 2:
        x = "0"
        blue = x + blue
    hex_code = "#"+str(red)+str(green)+str(blue)
    print(hex_code)

hex_color(10,32,255)
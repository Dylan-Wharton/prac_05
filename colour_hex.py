
COLOUR_LIST = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "BlanchedAlmond": "#ffebcd",
               "blue1": "#0000ff", "BlueViolet": "#8a2be2"}
# print(STATE_NAMES)

colour = input("Enter colour: ")
while colour != "":
    if colour in COLOUR_LIST:
        print(colour, "is", COLOUR_LIST[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
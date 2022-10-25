from posixpath import splitext
from PIL import Image, ImageOps
import sys
def main():
    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    #fitting the input image to shirt image size
    photo = ImageOps.fit(imagefile, size)
    # And you can overlay that image on top of another
    photo.paste(shirt, shirt)
    #save the image
    photo.save(sys.argv[2])

        




def check_command_line_arg():
    if(len(sys.argv)) < 3:
        sys.exit("Too few command-line arguments")
    if(len(sys.argv)) > 3:
        sys.exit("Too many command-line arguments")
    input_file = splitext(sys.argv[1])
    output_file = splitext(sys.argv[2])
    # print(input_file)
    # print(output_file)
    if chk_extension(input_file[1]) == False:
        print("Invalid Input")
    if chk_extension(output_file[1]) == False:
        print("Invalid Output")
    if input_file[1].lower() != output_file[1].lower():
        print("Input and output have different extensions")
    
    



def chk_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False
    


if __name__ == "__main__":
    main()
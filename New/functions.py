# import libraries / modules

from tkinter import filedialog as fd        # this is a module to can open dialogues.
from PIL import Image                   # this is a module for image manipulation.
import math

# declare variables

user_input_response = ["e", "E", "d", "D"]
ascii_unicode = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïð'
# ascii_unicode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' This was a test to don't load everithing
call_letter = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}
call_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
pixel_mosaic_size = 40  # change this value to modify the complexity of the mosaic


# declare a class to be loaded externally

class WhatToDo:
    """
    Diferent functions for the encryption porgram
    """
    # start declaring functions

    def is_not_used(self):   # function to avoid PyCharm message
        pass

    def ask_user_encrypt_or_decrypt(self=None):

        """
        Prompt user to encrypt or decrypt text.
        :return: (user_answer=string,message_to_print=string,exit_value_binary(string))
        """
        self.is_not_used()
        times = 0
        user_answer = input("\nWhat you want to do, encrypt or decrypt? (E or D): ")

        if user_answer in user_input_response:
            message = input("\n\tType message: ")
            return user_answer, message, "1"

        elif user_answer not in user_input_response:
            while times <= 2:
                user_answer = input("\nPlease, what you want to do, encrypt or decrypt? (%d times remaining, E or D): " % (3-times))
                times += 1
                if user_answer in user_input_response:
                    message = input("Type message: ")
                    return user_answer, message, "1"
            return "0", "0", "0"

        message = input("Type message: ")
        return user_answer, message, "1"

    def ask_for_the_picture(self=None):

        """
        Prompt user to select a file.
        Returns it open and ready to use
        :return: (object=image)
        """

        self.is_not_used()
        path = fd.askopenfilename(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))  # select a file from the library and return the path.
        return path

    def image_to_values(self, path):

        """
        Analyze the image and returns a list of values with
        the sum of the rgb color (max=(255,255,255)) for each pixel
        :return: (list=each_pixel_sum(rgb))
        """

        self.is_not_used()
        img = Image.open(path)                              # to work with the image, first is necessary to open it (basically is loaded)
        img_rgb = img.convert('RGB')                        # to use a color picker have to be sure to transform image to color profile to RGB

        img_small = img_rgb.resize((pixel_mosaic_size, pixel_mosaic_size), resample=Image.BILINEAR)   # transform image to 16*16 pixels

        list_of_tuples_of_pixels = []
        list_of_sum_of_rgb_values = []
        for pixelsV in range(pixel_mosaic_size):            # loop through vertical pixels
            for pixelsH in range(pixel_mosaic_size):        # loop through vertical pixels

                list_of_tuples_of_pixels.append(img_small.getpixel((pixelsV, pixelsH)))

        for RGB_tuple in list_of_tuples_of_pixels:
            list_of_sum_of_rgb_values.append(sum(RGB_tuple))

        return list_of_sum_of_rgb_values

    def encrypt_or_decrypt(self, message_passed, hash_of_pixels, val):

        """
        Function to encrypt or decrypt the code.
        Each letter from the string is read and value
        assigned looping trough the asccii code.
        :return: (object=image)
        """

        self.is_not_used()
        list_unicode = (list(ascii_unicode))
        message = (list(message_passed))

        message_list = []

        print(hash_of_pixels)

        if val == "E" or val == "e":
            for characters in message:

                val = list_unicode.index(characters)
                pixel_val = hash_of_pixels[message.index(characters)]
                num_val_color = val + pixel_val

                turns = math.floor(num_val_color / len(ascii_unicode))
                position = num_val_color % len(ascii_unicode)
                character_final = list_unicode[position]

                message_list.append(character_final + call_letter.get(turns))

        else:
            for characters in message:
                if (message.index(characters) % 2) == 0 or message.index(characters) == 0:

                    var = (message.index(characters) + 1)
                    var_str = str(message[var])
                    val1 = call_number.get(var_str)
                    print("val1 - " + str(val1))
                    val2 = ascii_unicode.index(characters)
                    print("val2 - " + str(val2))

                    hash_division = hash_of_pixels[message.index(characters)]

                    print("hash division " + str(hash_division))
                    len_ascii = (len(ascii_unicode)*int(val1) + int(val2))-(hash_of_pixels[message.index(characters)])

                    print(ascii_unicode[int(len_ascii)])

        return message_list

    def show_final_message(self, final_message):

        self.is_not_used()
        print("\n"+"".join(final_message))
        return

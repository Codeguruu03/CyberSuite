import os
from stegano import lsb
import pyfiglet as fig
from colorama import Fore
# from lib import hide_text_in_image, extract_text_from_image

def hide_text_in_image(image_path, text):
    # Hide the text within the image
    secret_image = lsb.hide(image_path, text)
    
    # Get the directory and file name without extension
    directory, filename = os.path.split(image_path)
    filename_without_extension, extension = os.path.splitext(filename)
    
    # Save the image with the hidden text
    secret_image_path = os.path.join(directory, f"{filename_without_extension}_hidden{extension}")
    secret_image.save(secret_image_path)
    print("Text hidden successfully in the image:", secret_image_path)
    return secret_image_path

def extract_text_from_image(image_path):
    # Extract the text from the image
    try:
        # Extract the text from the image
        extracted_text = lsb.reveal(image_path)
        print("Extracted text from the image:", extracted_text)
    except IndexError:
        print("No hidden message found in the image.")

def main():
    while True:
        # Print the ASCII art text using pyfiglet
        for i in fig.figlet_format('                    Steganografy    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)

        # Print some information about steganography
        print(Fore.GREEN + "Steganography is the art of concealing messages or data within other innocuous data, such as images, audio files, or text. By embedding information in this manner, steganography allows for covert communication, where the presence of the hidden data is not readily apparent to observers".center(120) + Fore.LIGHTCYAN_EX)

        # Ask for the user's choice
        choice = input("Choose an option:\n1. Hide text in an image\n2. Extract text from an image\n3. Go back to main page\n4. Exit\nEnter your choice (1/2/3/4): ")

        if choice == '1':
            # Ask for the user's choice for hiding text
            hide_choice = input("Choose what you want to hide:\n1. Message\n2. File\n3. Back to main menu\nEnter your choice (1/2/3): ")

            if hide_choice == '1':
                # Ask for the message to hide
                message = input("Enter the message you want to hide: ")
                image_path = input("Enter the path to the image: ")
                secret_image_path = hide_text_in_image(image_path, message)

            elif hide_choice == '2':
                # Ask for the file to hide
                file_path = input("Enter the path to the file: ")
                with open(file_path, 'r') as file:
                    file_content = file.read()

                image_path = input("Enter the path to the image: ")
                secret_image_path = hide_text_in_image(image_path, file_content)

            elif hide_choice == '3':
                continue

            else:
                print("Invalid choice.")

        elif choice == '2':
            # Ask for the image to extract text from
            image_path = input("Enter the path to the image: ")
            extract_text_from_image(image_path)

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python main.py')
            break

        elif choice == '4':
            print("Exiting..."  + Fore.RESET)
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

import os
from stegano import lsb
import pyfiglet as fig
from colorama import Fore
from utils import validate_image_file, validate_file_path, print_error, print_success
    # from lib import hide_text_in_image, extract_text_from_image

def hide_text_in_image(image_path, text):
        try:
            # Hide the text within the image
            secret_image = lsb.hide(image_path, text)
            
            # Get the directory and file name without extension
            directory, filename = os.path.split(image_path)
            filename_without_extension, extension = os.path.splitext(filename)
            
            # Save the image with the hidden text
            secret_image_path = os.path.join(directory, f"{filename_without_extension}_hidden{extension}")
            secret_image.save(secret_image_path)
            print(Fore.GREEN + "Text hidden successfully in the image: " + secret_image_path + Fore.RESET)
            return secret_image_path
        except FileNotFoundError:
            print(Fore.RED + f"Error: Image file '{image_path}' not found." + Fore.RESET)
            return None
        except Exception as e:
            print(Fore.RED + f"Error hiding text in image: {e}" + Fore.RESET)
            return None

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
            for i in fig.figlet_format('                    StegGenie    ', font='big', width=200).split('\n\n'):
                print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)

            # Print some information about steganography
            print(Fore.GREEN + "StegGenie is a steganography tool that conceals messages or data within images. Users can hide text or files within images and extract hidden information from them. With an intuitive interface and ASCII art banners, StegGenie enables covert communication and secure data concealment.".center(120) + Fore.LIGHTCYAN_EX)

            # Ask for the user's choice
            choice = input("Choose an option:\n1. Hide text in an image\n2. Extract text from an image\n3. Go back to main page\n4. Exit\nEnter your choice (1/2/3/4): ")

            if choice == '1':
                # Ask for the user's choice for hiding text
                hide_choice = input("Choose what you want to hide:\n1. Message\n2. File\n3. Back to main menu\nEnter your choice (1/2/3): ")

                if hide_choice == '1':
                    # Ask for the message to hide
                    message = input("Enter the message you want to hide: ")
                    if not message:
                        print(Fore.RED + "Error: Message cannot be empty." + Fore.RESET)
                        continue
                    image_path = input("Enter the path to the image: ")
                    if not os.path.exists(image_path):
                        print(Fore.RED + f"Error: Image '{image_path}' not found." + Fore.RESET)
                        continue
                    secret_image_path = hide_text_in_image(image_path, message)

                elif hide_choice == '2':
                    # Ask for the file to hide
                    file_path = input("Enter the path to the file: ")
                    try:
                        with open(file_path, 'rb') as file:
                            file_content = file.read().decode('utf-8')
                    except FileNotFoundError:
                        print(Fore.RED + f"Error: File '{file_path}' not found." + Fore.RESET)
                        continue
                    except UnicodeDecodeError:
                        print(Fore.RED + "Error: File contains non-text data. Please use a text file." + Fore.RESET)
                        continue

                    image_path = input("Enter the path to the image: ")
                    if not os.path.exists(image_path):
                        print(Fore.RED + f"Error: Image '{image_path}' not found." + Fore.RESET)
                        continue
                    secret_image_path = hide_text_in_image(image_path, file_content)

                elif hide_choice == '3':
                    continue

                else:
                    print("Invalid choice.")

            elif choice == '2':
                # Ask for the image to extract text from
                image_path = input("Enter the path to the image: ")
                if not os.path.exists(image_path):
                    print(Fore.RED + f"Error: Image '{image_path}' not found." + Fore.RESET)
                    continue
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

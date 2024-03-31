from stegano import lsb
import os


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
    extracted_text = lsb.reveal(image_path)
    print("Extracted text from the image:", extracted_text)
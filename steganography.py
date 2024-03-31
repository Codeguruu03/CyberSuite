from stegano import lsb

# Hide a secret message within an image
image_path = "nary.jpeg"
secret_message = "Hello How are you!!!!."

# Hide the message within the image
secret_image = lsb.hide(image_path, secret_message)

# Save the image with the hidden message
secret_image_path = "secret_image_with_message.png"
secret_image.save(secret_image_path)

print("Secret message hidden successfully.")

# Extract the hidden message from the image
extracted_message = lsb.reveal(secret_image_path)

print("Extracted message:", extracted_message)

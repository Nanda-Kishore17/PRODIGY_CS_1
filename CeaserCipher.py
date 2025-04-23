def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    
    return result

# User Input
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode! Use 'encrypt' or 'decrypt'.")
else:
    output = caesar_cipher(message, shift, mode)
    print(f"Result: {output}")

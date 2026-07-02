def caesar_decode(text, shift):
    decoded = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded += chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit() or char.isspace() or char == ':':
            decoded += char
        # Skip symbols
    return decoded


# Encoded repeating signal
encoded_signal = (
    "QrydSulphFrruglqdwhv:Vhfwru-7Doskd &$&_*_!"
    "QrydSulphFrruglqdwhv:Vhfwru-7Doskd&$&_*_!"
    "QrydSulphFrruglqdwhv:Vhfwru-7-Doskd&$&_*_!"
    "QrydSulphFrruglqdwhv:Vhfwru-7-Doskd&$&_*_!"
    "QrydSulphFrruglqdwhv:Vhfwru-7Doskd& $&_*_!"
    "QrydSulphFrruglqdwhv:Vhfwru-7-Doskd"
)

# Split by repeated pattern (approximate block)
blocks = encoded_signal.split("!")

# Try Caesar shifts from 1 to 25
for shift in range(1, 26):
    print(f"Shift {shift}:")
    decoded_blocks = [caesar_decode(block, shift) for block in blocks if block.strip()]
    print(" ".join(decoded_blocks))
    print()

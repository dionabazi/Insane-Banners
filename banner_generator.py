import pyfiglet
import time
import sys

def generate_banner(text, font='slant'):
    try:
        banner = pyfiglet.figlet_format(text, font=font)
        return banner
    except pyfiglet.FontNotFound:
        return f"Error: The font '{font}' is not available."

def animate_text(text, delay=0.01):
    for char in text:
        # Print the character without newline and flush the output
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after finishing

def main():
    # Display a default banner with your name "dionabazi" with animation
    print("\nBy:\n")
    animated_text = generate_banner("dionabazi", font='slant')
    for line in animated_text.splitlines():
        animate_text(line)  # Animate each line

    # Proceed with the rest of the script
    text = input("Enter the text for the banner: ")
    print("\nSuggested fonts for anonymous or skull themes:\n")
    
    # List the themed fonts
    themed_fonts = ['slant', 'banner3-D', 'ghost', 'standard', 'big', 'graffiti', 'skull']
    print(", ".join(themed_fonts))
    
    font = input("\nChoose a font from the above list (or press enter for default 'slant'): ")
    if not font:
        font = 'slant'  # Use default font if none is specified

    # Check if the chosen font is available in pyfiglet
    available_fonts = pyfiglet.FigletFont.getFonts()
    if font not in available_fonts:
        print(f"Error: The font '{font}' is not available. Using the default 'slant' font.")
        font = 'slant'

    # Generate and print the selected banner
    banner = generate_banner(text, font)
    print("\nGenerated Banner:\n")
    print(banner)

if __name__ == "__main__":
    main()

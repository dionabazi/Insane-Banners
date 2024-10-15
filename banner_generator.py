import pyfiglet

def generate_banner(text, font='slant'):
    try:
        # Generate the banner with the specified font
        banner = pyfiglet.figlet_format(text, font=font)
        return banner
    except pyfiglet.FontNotFound:
        return f"Error: The font '{font}' is not available."

def main():
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

    # Generate and print the banner
    banner = generate_banner(text, font)
    print("\nGenerated Banner:\n")
    print(banner)

if __name__ == "__main__":
    main()

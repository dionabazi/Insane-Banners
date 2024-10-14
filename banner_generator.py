import pyfiglet

def generate_banner(text, font='slant'):
    banner = pyfiglet.figlet_format(text, font=font)
    return banner

def main():
    text = input("Enter the text for the banner: ")
    print("\nSuggested fonts for anonymous or skull themes:\n")
    
    # List some themed fonts
    themed_fonts = ['slant', 'banner3-D', 'ghost', 'standard', 'big', 'graffiti', 'skull']
    print(", ".join(themed_fonts))
    
    font = input("\nChoose a font from the above list (or press enter for default 'slant'): ")
    if not font:
        font = 'slant'  # Default font

    try:
        banner = generate_banner(text, font)
        print("\nGenerated Banner:\n")
        print(banner)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

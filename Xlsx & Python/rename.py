import os

def rename_files(directory):
    greek_to_english = {
        'Α': 'a', 'Β': 'b', 'Γ': 'g', 'Δ': 'd', 'Ε': 'e',
        'Ζ': 'z', 'Η': 'h', 'Θ': 'th', 'Ι': 'i', 'Κ': 'k',
        'Λ': 'l', 'Μ': 'm', 'Ν': 'n', 'Ξ': 'x', 'Ο': 'o',
        'Π': 'p', 'Ρ': 'r', 'Σ': 's', 'Τ': 't', 'Υ': 'y',
        'Φ': 'f', 'Χ': 'ch', 'Ψ': 'ps', 'Ω': 'o',
        'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e',
        'ζ': 'z', 'η': 'h', 'θ': 'th', 'ι': 'i', 'κ': 'k',
        'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x', 'ο': 'o',
        'π': 'p', 'ρ': 'r', 'σ': 's', 'τ': 't', 'υ': 'y',
        'φ': 'f', 'χ': 'ch', 'ψ': 'ps', 'ω': 'o'
    }

    for filename in os.listdir(directory):
        new_name = filename
        for greek_char, english_char in greek_to_english.items():
            new_name = new_name.replace(greek_char, english_char)
        os.rename(os.path.join(directory, filename),
                  os.path.join(directory, new_name))

directory = "C:\\Users\\Charis\\Desktop\\New folder\\img\\new\\all"

rename_files(directory)

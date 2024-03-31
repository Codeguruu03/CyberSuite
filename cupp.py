import itertools

def generate_wordlist(names, keywords, years, separators):
    wordlist = []

    for name in names:
        for keyword in keywords:
            for year in years:
                for separator in separators:
                    # Generate combinations of name, keyword, year, and separator
                    combination = [name, keyword, year, separator]
                    wordlist.append(''.join(combination))

    return wordlist

# Example input data
names = ['john', 'emma']
keywords = ['password', '123', 'admin']
years = ['1990', '1995']
separators = ['', '_', '-']

# Generate wordlist
wordlist = generate_wordlist(names, keywords, years, separators)

# Print generated wordlist
for password in wordlist:
    print(password)

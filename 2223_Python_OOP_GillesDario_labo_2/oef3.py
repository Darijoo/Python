letter = input("Geef een letter: ")

if letter == "a"or"e"or"i"or"o"or"u":
    print(f"De letter {letter} is een klinker!")
elif letter == "y":
    print("y kan als klinker en medeklinker gelden!")
elif len(letter) > 1:
    print("De uitkomst kon niet berekend worden!") 
else:
    print(f"{letter} is een medeklinker!")
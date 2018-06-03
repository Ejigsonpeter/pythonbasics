statement = "The quick brown fox jumped over the lazy dogs"

for letter in statement:
    if letter == "e":
          break
    print("Current letter ", letter)


for letter in statement:
    if letter == "q":
        continue
    print("the current letter ",letter)
      
    

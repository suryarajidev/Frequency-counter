# Frequency counter

string = "python programming"

def count_letters(string):
  letters = {}
  for char in string:

    works = True
    try:
      letters[char]
    except:
      works = False

    if works:
      letters[char] += 1
    else:
      letters[char] = 1

  return letters

count_letters(string)

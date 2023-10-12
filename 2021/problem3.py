numerals = {
  1: "I",
  5: "V",
  10: "X",
  50: "L",
  100: "C",
  500: "D",
  1000: "M"
}


def main(n):
  digits = []
  x = n
  while x >= 10:
    digits.append(x % 10)
    x //= 10
  digits.append(x)
  digits = digits[::-1]

  roman_chars = []
  for p, digit in enumerate(digits):
    place = len(digits) - p - 1
    if digit < 4:
      for _ in range(digit):
        roman_chars.append(numerals[10 ** place])
    elif digit == 4:
      roman_chars.append(numerals[10 ** place])
      roman_chars.append(numerals[(10 ** place) * 5])
    elif 4 < digit < 9:
      roman_chars.append(numerals[(10 ** place) * 5])
      for _ in range(digit - 5):
        roman_chars.append(numerals[10 ** place])
    elif digit == 9:
      roman_chars.append(numerals[10 ** place])
      roman_chars.append(numerals[10 ** (place + 1)])

  roman_numeral = "".join(roman_chars)
  if len(digits) == len(roman_numeral):
    print(f"{roman_numeral} ROMAN-EQUIVALENT")
  else:
    print(f"{roman_numeral} NOT ROMAN-EQUIVALENT")

main(int(input()))

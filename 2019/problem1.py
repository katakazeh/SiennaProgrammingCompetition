# Conversion factor to teaspoons
ratios = {
  "TEASPOONS": 1,
  "TABLESPOONS": 3,
  "CUPS": 48,
  "PINTS": 96,
  "QUARTS": 192,
  "GALLONS" : 768
}

num, start_unit, end_unit = input().split()
num = int(num)

teaspoons = ratios[start_unit] * num
print(teaspoons // ratios[end_unit])

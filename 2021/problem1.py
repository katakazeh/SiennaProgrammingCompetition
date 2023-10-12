knots = {
  tuple([0]): "CALM",
  tuple(range(1, 3+1)): "LIGHT-AIR",
  tuple(range(4, 6+1)): "LIGHT-BREEZE",
  tuple(range(7, 10+1)): "GENTLE-BREEZE",
  tuple(range(11, 16+1)): "MODERATE-BREEZE",
  tuple(range(17, 21+1)): "FRESH-BREEZE",
  tuple(range(22, 27+1)): "STRONG-BREEZE",
  tuple(range(28, 33+1)): "NEAR-GALE",
  tuple(range(34, 40+1)): "GALE",
  tuple(range(41, 47+1)): "SEVERE-GALE",
  tuple(range(48, 55+1)): "STORM",
  tuple(range(56, 63+1)): "VIOLENT-STORM"
}

mph = {
  tuple([0]): "CALM",
  tuple(range(1, 3+1)): "LIGHT-AIR",
  tuple(range(4, 7+1)): "LIGHT-BREEZE",
  tuple(range(8, 12+1)): "GENTLE-BREEZE",
  tuple(range(13, 18+1)): "MODERATE-BREEZE",
  tuple(range(19, 24+1)): "FRESH-BREEZE",
  tuple(range(25, 31+1)): "STRONG-BREEZE",
  tuple(range(32, 38+1)): "NEAR-GALE",
  tuple(range(39, 46+1)): "GALE",
  tuple(range(47, 54+1)): "SEVERE-GALE",
  tuple(range(55, 63+1)): "STORM",
  tuple(range(64, 72+1)): "VIOLENT-STORM"
}

unittables = {
  "KNOTS": knots,
  "MPH": mph
}


strength = int(input())
unit = input()


if (strength >= 73 and unit == "MPH") or (strength >= 64 and unit == "KNOTS"):
  print("HURRICANE")
else:
  for key in unittables[unit]:
    if strength in key:
      print(unittables[unit][key])

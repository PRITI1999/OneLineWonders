print("POS CLUB"+' '*18+"P   W   D   L  GF  GA  GD PTS",*[("\n{:>3} {:21}{:>2}"+"{:>4}"*7).format(*__import__("re").findall(r"[\d\-]+|(?=\w)[^\d\-]+(?![\d\-])",line))for line in __import__("sys").stdin])

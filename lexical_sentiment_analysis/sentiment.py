from sys import stdin
from analyzer import analyzer

if __name__ == "__main__":
  analyze = analyzer()

  for line in stdin:
    line = line.strip()
    print(line)
    print(analyze(line))
    print()
def PatternCount(text, pattern):    #returns the number of times that a k-mer Pattern appears as a substring of text.
    count = 0;
    for i in range(len(text)-len(pattern)+1):
        if text[i:(i+len(pattern))] == pattern:
            count = count + 1
    return count

with open('rosalind_ba1a.txt', 'r') as f:
    inputs = f.read().splitlines()
for i in range(1, len(inputs)):
    count = PatternCount(inputs[0], inputs[1])
    print(count)

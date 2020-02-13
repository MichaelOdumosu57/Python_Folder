from urllib.request import urlopen
with urlopen('https://docs.python.org/3.8/tutorial/stdlib.html') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        print(line)

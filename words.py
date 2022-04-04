from urllib.request import urlopen

story = urlopen('https://filesamples.com/samples/document/txt/sample3.txt')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
story.close()

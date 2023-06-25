import re

def most_common(file_path):
    d = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if is_url_path(word):
                    if word in d:
                        d[word] += 1
                    else:
                        d[word] = 1
    return d

def is_url_path(word):
    regex_pattern = r'^www\..*\.(com|org|edu|gov|net)$'
    if re.search(regex_pattern, word):
        return True
    else:
        return False

file_path = "text_log_url.txt"
url_path_counts = most_common(file_path)
sorted_url_paths = sorted(url_path_counts, key=url_path_counts.get, reverse=True)
print("Most common URL paths:")
for url_path in sorted_url_paths[:5]:
    print(url_path, url_path_counts[url_path])

# one two three www.google.com four
# five six www.google.com seven eight
# nine ten eleven www.amazon.com twelve
# nine eleven www.facebook.com twelve
# ten eleven www.amazon.com twelve
# nine ten eleven www.facebook.net twelve
# nine eleven www.amazon.net twelve
# nine eleven www.google.com twelve

from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
print(page)

# Basic WebScraper
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# Extract Text From HTML With String Methods
title_index = html.find("<title>")
print(title_index)
start_index = title_index + len("<title>")
print(start_index)
end_index = html.find("</title>")
print(end_index)
title = html[start_index:end_index]
print(title)
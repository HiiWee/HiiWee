import feedparser, time

URL = "https://hiiwee.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
### Hi there 👋

Hi, I'm Hoseok Lee, a passionate backend developer!
Always open to learning and collaborating, so feel free to reach out!

- [e-mail](mailto:wpdlzhf159@gmail.com) 
- [LinkedIn](https://www.linkedin.com/in/%ED%98%B8%EC%84%9D-%EC%9D%B4-01278b264/)


### 📌 Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()

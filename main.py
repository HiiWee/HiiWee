import feedparser, time

URL = "https://hiiwee.tistory.com//rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
### Hi there 👋
백엔드 공부를 하고 있는 학생입니다.   
좋은 구조, 코드란 무엇인지 궁금해하며   
그것들을 판단할 수 있는 능력을 가지기 위해 노력 중 입니다.   
`Graceful code comes from hard work!!!`

🌱 I’m currently learning ...

<a href="https://www.java.com/ko/" target="_blank"><img src="https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white"/></a>
<a href="https://spring.io/" target="_blank"><img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white"/></a>


![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=HiiWee&&show_icons=true&theme=highcontrast)
<!--
**HiiWee/HiiWee** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...

- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

## ✅ Latest Blog Post

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

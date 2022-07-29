---
hide:
  - navigation
  - toc

tags:
  - contributors
  - helpers
---

# Our Contributors

## These are our amazing contributors ❤️ 

<table>
{% for i in contributors_data %}
  <tr>
  {% for j in i %}
    <td align="center"><a href="{{j.profile}}"><img src="{{j.avatar_url}}" width="100px;" alt="{{j.name}} Profile Photo" loading="lazy"/><br /><sub><b>{{j.name}}</b></sub></a><br />{% for k in j.contributions %}&nbsp;<a href="#{{k}}-{{j.login}}" id="{{k}}-{{j.login}}">{{k|contribution_to_emoji}}</a>{% endfor %}<br /><a href="{{config.repo_url}}commits?author={{j.login}}" target="_blank">Commits History</a></td>
  {% endfor %}
  </tr>
{% endfor %}
</table>

<script async="async" data-cfasync="false" src="//pl17523944.highperformancegate.com/86bde6f923ad7ce4a09df3fd7396a340/invoke.js"></script>
<div id="container-86bde6f923ad7ce4a09df3fd7396a340"></div>

![Minato And Naruto](https://i.imgur.com/knPSUxI.jpg){ loading=lazy }

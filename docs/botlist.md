---
tags:
  - botlist
  - listing
  - widgets
---

{{bot_name}} is listed in the following botlists


<table>
{% for i in botlists_data %}
  <tr>
  {% for j in i %}
    <td align="left">{{j.name}}</td>
    <td align="left"><a href="{{j.https_url}}/{{bot_discord_id}}" target="_blank"><b>{{j.name}}</b> profile page</a></td>
  {% endfor %}
  </tr>
{% endfor %}
</table>

# Widgets

<a href="https://discordbotlist.com/bots/{{bot_discord_id}}" target="_blank"><img src="https://discordbotlist.com/api/v1/bots/{{bot_discord_id}}/widget" loading="lazy"></a>

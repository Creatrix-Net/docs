---
title: Application Commands List
tags:
  - commands
  - application commands
  - context menus
  - slash commands
---

List of all `slash commands` and `context menu's` available in the bot.

{% for i in application_commands %}
## {{i.name|title}}

{% if i.description %}
{{i.description}}
{% endif %}

{% if i.options is not none %}
<table>
<tr>
    <th>Name</th>
    <th>Description</th>
    <th>Required</th>
    <th>Type</th>
  </tr>
{% for j in i.options %}
<tr>
    <td>{{ j.name }}</td>
    <td>{{ j.description }}</td>
    <td>{{ j.required }}</td>
    <td>{{ j.type }}</td>
  </tr>
{% endfor %}
</table>
{% endif %}
<hr/>
{% endfor %}
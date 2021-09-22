```python
These are the commands list, You can check them out! :)
``` 
***
{% for i in commands %}
- ## __{{i.name}}__

<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Usage</th>
    <th>Vote Locked</th>
  </tr>
  {% for j in i.commands_list %}
  <tr>
    <td>{{j.cmd_name}}</td>
    <td>{{j.description}}</td>
    <td>{{j.examples|slice(1)}}</td>
    <td>{% if j.vote_locked %}✔️{% else %}❌{% endif %}</td>
  </tr>
  {% endfor %}
</table>

***
{% endfor %}

```python
These are the commands list, You can check them out! :)
``` 
***
{% for i in commands %}
- ## __{{i.name}}__

{% for j in i.commands_list %}
 ### __{{j.name}}__
<table style="box-shadow: 5px 5px 5px 5px black;">
  <tr>
    <td>
    <h3>{{ i.description|format_description }}</h3>
    {% if i.discord %}
    <a title="{{ i.name|capitalize }} Discord" href="{{ i.discord }}" target="_blank"><i class='bx bxl-discord' style="font-size: 40px; color: #5865F2;"></i></a>
    {% endif %}
    {% if i.website %}
    <a title="{{ i.name|capitalize }} Website" href="{{ i.website }}" target="_blank"><i class='bx bx-globe' style="font-size: 40px;"></i></a>
    {% endif %}
    {% if i.invite %}<a title="{{ i.name }} Invite Link" href="{{ i.invite }}" target="_blank"><i class='bx bx-link' style="font-size: 40px;"></i></a>{% endif %}
    {% if i.twitter %}<a title="{{ i.name }} Twitter Account" href="{{ i.twitter }}" target="_blank"><i class='bx bxl-twitter' style="font-size: 40px; color: #00acee;"></i></a>{% endif %}
    </td>
  </tr>
</table>
{% endfor %}
{% endfor %}

---
tags:
  - partners
---

<link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>

# Partners

```python
Hi these are our partners, please go and check these amazing sites out!
```

<script async="async" data-cfasync="false" src="//pl17523944.highperformancegate.com/86bde6f923ad7ce4a09df3fd7396a340/invoke.js"></script>
<div id="container-86bde6f923ad7ce4a09df3fd7396a340"></div>

{% for i in partners %}
## __{{ i.name }}__
<table {% if i.shadow %}style="box-shadow: 5px 5px 5px 5px {{i.shadow}};"{% endif %}>
  <tr>
    <td><img src="{{ i.logo or i.profile_logo }}" loading="lazy" width="350px" {% if not i.no_round %}style="border-radius: 50%;"{% endif %}></td>
    <td>
    <a title="{{ i.name }}" href="{{ i.website }}" target="_blank"><h1><strong>{{ i.name }}</strong></h1></a>
    <h3>{{ i.description|format_description|safe }}</h3>
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



<script src="https://unpkg.com/boxicons@2.0.9/dist/boxicons.js"></script>

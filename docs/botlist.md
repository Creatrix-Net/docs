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

[![!Discord Botlist Widget](https://discordbotlist.com/api/v1/bots/{{bot_discord_id}}/widget)](https://discordbotlist.com/bots/{{bot_discord_id}}){ target=_blank } 

***

[![!Void Bots Widget](https://voidbots.net/api/embed/{{bot_discord_id}}?theme=dark){ loading=lazy width=36% }](https://voidbots.net/bot/{{bot_discord_id}}){ target=_blank }

***

[![!Discord Services Widget](https://discordservices.net/bot/{{bot_discord_id}}/widget.svg)](https://discordservices.net/bot/{{bot_discord_id}}){ target=_blank } 

***

[![!Top.gg Widget](https://top.gg/api/widget/{{bot_discord_id}}.svg){ loading=lazy }](https://top.gg/bot/{{bot_discord_id}}){ target=_blank }

***

[![!Fateslist Widget](https://widgets.fateslist.xyz/{{bot_discord_id}}?target_type=bot&format=png){ loading=lazy }](https://fateslist.xyz/bot/{{bot_discord_id}}){ target=_blank } 

***

[![!Discord List Space Widget](https://api.discordlist.space/v2/bots/{{bot_discord_id}}/widget?background=7289DA&radius=6){ loading=lazy }](https://discordlist.space/bot/{{bot_discord_id}}){ target=_blank } 

***

[![!Bots For Discord Widget](https://discords.com/bots/api/bot/{{bot_discord_id}}/widget){ loading=lazy }](https://discords.com/bots/bots/{{bot_discord_id}}){ target=_blank } 

***

[![!vCodes Widget](https://vcodes.xyz/api/widget/{{bot_discord_id}}.svg){ loading=lazy }](https://vcodes.xyz/bot/{{bot_discord_id}}){ target=_blank } 

***

[![Infinity Botlist Widget](https://infinitybots.gg/bots/{{bot_discord_id}}/widget?size=large){ loading=lazy }](https://infinitybots.gg/bots/{{bot_discord_id}}){ target=_blank } 

***

[![Botlist.me Widget](https://api.botlist.me/api/v1/embed/{{bot_discord_id}}){ loading=lazy }](https://botlist.me/bots/{{bot_discord_id}}){ target=_blank } 


***

[![!Blist Widget](https://blist.xyz/api/v2/bot/{{bot_discord_id}}/widget){ loading=lazy }](https://blist.xyz/bot/{{bot_discord_id}}){ target=_blank } 

***

[![!Discord Botlist EU Widget](https://widget.discord-botlist.eu/{{bot_discord_id}}){ loading=lazy }](https://discord-botlist.eu/bots/{{bot_discord_id}}){ target=_blank }

***

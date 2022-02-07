<style>
    article{
        font-family: monospace;
        padding: 0 3px;
    }
</style>

    Use ")help command" for more info on a command.
    Use ")help category" for more info on a category.
    Use the dropdown menu below to select a category.

    Support Server
    For more help, consider joining the official server over at https://discord.gg/{{config.discord_invite_code}}
    
    How do I use this bot?
    Reading the bot signature is pretty simple.
    
    <argument>
    This means the argument is required.
    
    [argument]
    This means the argument is optional.
    
    [A|B]
    This means that it can be either A or B.
    

    [argument...]
    This means you can have multiple arguments.
    
    Now that you know the basics, it should be noted that...
    You do not type in the brackets!

{% for i in commands %}
## {{i.name}}
{% if i.description %}
{{i.description}}
{% endif %}

{% for j in i.commands_list %}
### - {{ j.name }}
{{ j.short_doc }}

{% if j.params %}
    Parameters Required: {{j.params}}
{% endif %}
{% if j.usage %}
    Usage: {{j.usage}}
{% endif %}
{% if j.aliases %}
    Aliases: {{j.aliases}}
{% endif %}

<hr/>
{% endfor %}

<hr/>
{% endfor %}



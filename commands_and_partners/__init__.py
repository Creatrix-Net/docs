import functools
import json
import os
import random
import markdown
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    import dotenv
    dotenv.load_dotenv(BASE_DIR/ os.path.join('config', '.env'))
except:
    pass

def discord_api_req(
    path: str,
    method: str = "post" or "get",
    data: dict = None,
    content_type: str = "application/json",
):
    base_api = "https://discord.com/api"
    headers = {
        "User-Agent": "Minato Namikaze Website",
        "X-Ratelimit-Precision": "millisecond",
        "Authorization": f"Bot {os.environ.get('BOT_TOKEN')}",
        "Content-Type": content_type,
    }
    req = requests.request(url=base_api + path, headers=headers, method=method.upper(), data=data)
    content = req.json()
    return content

def get_the_user_image_url(bot_id: int) -> str:
    users_data = discord_api_req(f'/users/{bot_id}','get')
    return f'https://cdn.discordapp.com/avatars/{bot_id}/{users_data.get("avatar")}.png?size=512'

class Partners:
    def __init__(self, json_dict: dict):
        for i in json_dict:
            if json_dict.get("bot"):
                setattr(self, "profile_logo", get_the_user_image_url(json_dict.get("bot_id")))
            setattr(self, i, json_dict[i])

class Command:
    def __init__(self, json_dict: dict):
        self.name = json_dict["name"]
        self.short_doc = json_dict["short_doc"]
        self.usage = json_dict.get("usage")
        self.aliases = ', '.join(json_dict.get("aliases")) if json_dict.get("aliases") is not None else None
        self.description = json_dict.get("description")
        self.parent = json_dict.get("parent") if len(json_dict.get("parent")) > 0 else None
        self.params = ', '.join(json_dict.get("params")) if json_dict.get("params") is not None else None
            
class CommandGroups:
    def __init__(self, list_dict: list, name: str):
        self.name = name
        self.description = list_dict.get('description')
        self.commands_list = [Command(list_dict['cog_commands_list'][count]) for count,i in enumerate(list_dict['cog_commands_list'])]


class ApplicationCommandsOptions:
    def __init__(self, json_dict: dict):
        self.name = json_dict["name"]
        self.description = json_dict["description"]
        self.required = json_dict["required"]
        self.type = json_dict["type"]

class ApplicationCommands:
    def __init__(self, json_dict: dict):
        self.name = json_dict["name"]
        self.description = json_dict["description"]
        self.options = [ApplicationCommandsOptions(i) for i in json_dict.get("options")] if len(json_dict.get("options"))>0 is not None else None


def define_env(env):
    global BASE_DIR
    
    @functools.lru_cache
    def partners(*args, **kwargs):
        file_path = BASE_DIR / os.path.join('config', 'partners.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
        def add_data(name: str, dict_data: dict):
            dict_data.update({'name': name})
            return Partners(dict_data)
        random_data = [ add_data(i, data[i]) for i in data ]
        random.shuffle(random_data)
        return random_data
    
    env.variables['partners'] = partners()
    
    def commands_groups():
        req = requests.get(
            'https://raw.githubusercontent.com/The-4th-Hokage/yondaime-hokage/master/minato_namikaze/lib/data/commands.json',
        )
        commands_json = req.json()
        return [CommandGroups(commands_json['commands'][i], i) for i in commands_json['commands']]
    
    def application_commands_groups():
        req = requests.get(
            'https://raw.githubusercontent.com/The-4th-Hokage/yondaime-hokage/master/minato_namikaze/lib/data/commands.json',
        )
        commands_json = req.json()
        return [ApplicationCommands(i) for i in commands_json['application_commands']]
    
    env.variables['commands'] = commands_groups()
    env.variables['application_commands'] = application_commands_groups()
    
    @functools.lru_cache
    @env.filter
    def format_description(x):
        '''Formats the bot's markdown description to HTML one'''
        return markdown.markdown(x.replace('\n', '<br/>').replace('\t','&nbsp;&nbsp;&nbsp;&nbsp;'))

    @functools.lru_cache
    @env.filter
    def reverse(x):
        "Reverse a string (and uppercase)"
        return x.upper()[::-1]

    @functools.lru_cache    
    @env.filter
    def capitalize(x):
        "Reverse a string (and uppercase)"
        return x.capitalize()
            

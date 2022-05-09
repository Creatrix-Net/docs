import functools
import json
import os
import random
import typing
from pathlib import Path

import markdown
import requests
import time

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    import dotenv
    dotenv.load_dotenv(BASE_DIR/ os.path.join('config', '.env'))
except:
    pass

contributors_mapping = {'audio': '\U0001f50a', 'a11y': '\U0000267f', 'bug': '\U0001f41b', 'blog': '\U0001f4dd', 'business': '\U0001f4bc', 'code': '\U0001f4bb', 'content': '\U0001f58b', 'data': '\U0001f523', 'doc': '\U0001f4d6', 'design': '\U0001f3a8', 'example': '\U0001f4a1', 'eventorganizing': '\U0001f4cb', 'financial': '\U0001f4b5', 'fundingfinding': '\U0001f50d', 'ideas': '\U0001f914', 'infra': '\U0001f687', 'maintenance': '\U0001f6a7', 'mentoring': '\U0001f9d1\U0001f3eb', 'platform': '\U0001f4e6', 'plugin': '\U0001f50c', 'projectmanagement': '\U0001f4c6', 'question': '\U0001f4ac', 'research': '\U0001f52c', 'review': '\U0001f440', 'security': '\U0001f6e1', 'tool': '\U0001f527', 'translation': '\U0001f30d', 'test': '\U000026a0', 'tutorial': '\U00002705', 'talk': '\U0001f4e2', 'usertesting': '\U0001f4d3', 'video': '\U0001f4f9'}

@functools.lru_cache(maxsize=10)
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
    time.sleep(5)
    return content

def get_the_user_image_url(bot_id: int) -> str:
    users_data = discord_api_req(f'/users/{bot_id}','get')
    return f'https://cdn.discordapp.com/avatars/{bot_id}/{users_data.get("avatar")}.png?size=512'

def _chunk(iterator, max_size: int):
    ret = []
    n = 0
    for item in iterator:
        ret.append(item)
        n += 1
        if n == max_size:
            yield ret
            ret = []
            n = 0
    if ret:
        yield ret

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
        self.options = [ApplicationCommandsOptions(i) for i in json_dict.get("options")] if len(json_dict.get("options")) > 0 else None


class Contributors:
    def __init__(self, json_dict: dict):
        self.login = json_dict['login']
        self.name = json_dict['name']
        self.avatar_url = json_dict['avatar_url']
        self.profile = json_dict['profile']
        self.contributions = json_dict['contributions']


class Botlist:
    def __init__(self, name: str, value:str):
        self.name = name.title()
        self.url = value
        self.http_url = 'http://'+value
        self.https_url = 'https://'+value


def define_env(env):
    global BASE_DIR
    
    def partners(*args, **kwargs):
        file_path = BASE_DIR / os.path.join('config', 'partners.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
        def add_data(name: str, dict_data: dict):
            dict_data.update({'name': name})
            return Partners(dict_data)
        random_data = [add_data(i, data[i]) for i in data ]
        random.shuffle(random_data)
        return random_data
    
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
    
    def contributors_data():
        req = requests.get(
            'https://raw.githubusercontent.com/The-4th-Hokage/yondaime-hokage/master/.all-contributorsrc'
        )
        json_data = req.json()
        return [Contributors(i) for i in json_data['contributors']]
    
    def botlists_data():
        req = requests.get(
            'https://raw.githubusercontent.com/The-4th-Hokage/listing/master/listing.json'
        )
        json_data = req.json()
        return [Botlist(name=i, value=json_data[i]) for i in json_data]
    
    env.variables['commands'] = commands_groups()
    env.variables['partners'] = partners()
    env.variables['application_commands'] = application_commands_groups()
    env.variables['contributors_data'] = _chunk(contributors_data(), 7)
    env.variables['botlists_data'] = _chunk(botlists_data(), 2)
    
    @functools.lru_cache
    @env.filter
    def format_description(x):
        '''Formats the bot's markdown description to HTML one'''
        return markdown.markdown(x.replace('\n', '<br/>').replace('\t','&nbsp;&nbsp;&nbsp;&nbsp;'))

    @functools.lru_cache
    @env.filter
    def reverse(x):
        """Reverse a string (and uppercase)"""
        return x.upper()[::-1]

    @functools.lru_cache    
    @env.filter
    def capitalize(x):
        """Reverse a string (and uppercase)"""
        return x.capitalize()
    
    @functools.lru_cache    
    @env.filter
    def contribution_to_emoji(contrib: typing.Literal[
        "a11y",
        "audio",
        "blog",
        "bug",
        "business",
        "code",
        "content",
        "data",
        "design",
        "doc",
        "eventorganizing",
        "example",
        "financial",
        "fundingfinding",
        "ideas",
        "infra",
        "maintenance",
        "mentoring",
        "platform",
        "plugin",
        "projectManagement",
        "question",
        "review",
        "security",
        "talk",
        "test",
        "tool",
        "translation",
        "tutorial",
        "usertesting",
        "video",
    ]):
        """Contribution to emoji"""
        return contributors_mapping.get(contrib.lower())
            

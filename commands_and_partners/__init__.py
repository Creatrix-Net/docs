import json

from pathlib import Path
import os, requests

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    import dotenv
    dotenv.load_dotenv(BASE_DIR/ os.path.join('config', '.env'))
except:
    pass

class Partners:
    def __init__(self, json_dict: dict):
        for i in json_dict:
            setattr(self, i, json_dict[i])

class Command:
    def __init__(self, json_dict: dict):
        for i in json_dict:
            setattr(self, i, json_dict[i])
            
class CommandGroups:
    def __init__(self, list_dict: list, name: str):
        self.name = name.capitalize().strip(' ')
        self.commands_list = [Command(list_dict[count]) for count,i in enumerate(list_dict)]


def define_env(env):
    global BASE_DIR
    
    def partners(*args, **kwargs):
        file_path = BASE_DIR / os.path.join('config', 'partners.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
        def add_data(name: str, dict_data: dict):
            dict_data.update({'name': name.capitalize()})
            return Partners(dict_data)
        return [ add_data(i, data[i]) for i in data ]
    
    env.variables['partners'] = partners()
    
    def commands_groups():
        req = requests.get(
            'https://fateslist.xyz/api/v2/bots/779559821162315787/commands',
            headers={'Authorization': os.environ.get('FATES_USER_TOKEN')}
        )
        commands_json = req.json()
        return [CommandGroups(commands_json[i], i) for i in commands_json]
    
    env.variables['commands'] = commands_groups()
    

    @env.filter
    def format_description(x):
        '''Formats the bot's markdown description to HTML one'''
        return x.replace('\n', '<br/>')

    @env.filter
    def reverse(x):
        "Reverse a string (and uppercase)"
        return x.upper()[::-1]
    
    @env.filter
    def capitalize(x):
        "Reverse a string (and uppercase)"
        return x.capitalize()
            

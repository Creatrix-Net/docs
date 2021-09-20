import json

from pathlib import Path
import os, ast, requests

BASE_DIR = Path(__file__).resolve().parent.parent

class Partners:
    def __init__(self, json_dict: dict):
        for i in json_dict:
            setattr(self, i, json_dict[i])

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
            

---
title: Commands Help
enable:
  - navigation
  - toc

tags:
  - commands
  - message commands
  - application commands
  - context menus
---

**Minato Namikaze** provides 2 different types of commands, namely `Message Commands` and `Application Commands`

## Message Commands
These types of commands can easily typing `[prefix]command_name sub_command_name` in discord [See the GIF below]

    The prefix for the bot is ) or m! or minato
    i.e. either of following would work
    )help
    m!help
    minato help
    
    Also by mentioning Minato you invoke commands i.e.
    @Minato Namikaze help

    And in DM's only m! works i.e. only m!help in DM's

To get a list of full messagable commands click the button below:

[Message Commands List](message_commands.md){ .md-button }

![How to interaction with bot via message commands](/assets/commands/message_commands.gif)

<hr/>

## Application Commands

```Application commands are commands that an application can register to Discord. They provide users a first-class way of interacting directly with your application that feels deeply integrated into Discord.``` : This is the [Discord definition](https://discord.com/developers/docs/interactions/application-commands#application-commands)

Here in **Minato Namikaze** the `application commands are categorized` into two different types:

- [Slash Commands](#slash-commands)

- [Context Menus](#context-menus)

### Slash Commands

Slash Commands are the new, exciting way to interact with bots on Discord. With Slash Commands, all you have to do is type / and you're ready to use the bot. You can easily see all the commands a bot has, and validation and error handling help you get the command right the first time.
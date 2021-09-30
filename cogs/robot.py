# Gets a random robot from various wikis and returns
# a string with the name of the machine and the URL to its page

import requests, bs4, random
from discord.ext import commands

def gundam():
    # Download wiki page with list of robots
    res = requests.get('https://gundam.fandom.com/wiki/List_of_Mobile_Weapons')

    try: # check for errors or fail
        res.raise_for_status()
    except Exception:
        return 'Unable to get list of robots!'

    # Extract list items
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select('li> a[title]')

    # Initialize empty dictionary
    result = {}

    # Loop through all items in list and save machine name and URL to dictionary
    for l in links:
        machine = l.get('title')
        link = l.get('href')
        if 'Category' in machine:
            # Likely a better way to do this, but this catches 
            # the garbage at the end of the list
            break
        else:
            result[machine] = 'https://gundam.fandom.com' + link
    machine, url = random.choice(list(result.items())) # Pick a random machine

    # Save that result to a string and return it
    message = machine + ': ' + url
    return message

def valvrave():
    # Download wiki page with list of robots
    res = requests.get('https://kakumeikivalvrave.fandom.com/wiki/Category:Mecha')

    try: # check for errors or fail
        res.raise_for_status()
    except Exception:
        return 'Unable to get list of robots!'

    # Extract list items
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.category-page__member-link')

    # Initialize empty dictionary
    result = {}

    # Loop through all items in list and save machine name and URL to dictionary
    for l in links:
        machine = l.get('title')
        link = l.get('href')
        if machine != 'Valvrave':
            result[machine] = 'https://kakumeikivalvrave.fandom.com' + link
    machine, url = random.choice(list(result.items())) # Pick a random machine

    # Save that result to a string and return it
    message = machine + ': ' + url
    return message

def ttgl():
    # Download wiki page with list of robots
    res = requests.get('https://gurrenlagann.fandom.com/wiki/Category:Mecha')

    try: # check for errors or fail
        res.raise_for_status()
    except Exception:
        return 'Unable to get list of robots!'

    # Extract list items
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.category-page__member-link')

    # Initialize empty dictionary
    result = {}

    # Loop through all items in list and save machine name and URL to dictionary
    for l in links:
        machine = l.get('title')
        link = l.get('href')
        result[machine] = 'https://gurrenlagann.fandom.com' + link
    machine, url = random.choice(list(result.items())) # Pick a random machine

    # Save that result to a string and return it
    message = machine + ': ' + url
    return message

def lfo():
    # Download wiki page with list of robots
    res = requests.get('https://eurekaseven.fandom.com/wiki/Light_Finding_Operation')

    try: # check for errors or fail
        res.raise_for_status()
    except Exception:
        return 'Unable to get list of robots!'

    # Extract list items
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select('li> a[title]')

    # Initialize empty dictionary
    result = {}

    # Loop through all items in list and save machine name and URL to dictionary
    for l in links:
        machine = l.get('title')
        link = l.get('href')
        if 'Special:Categories' in machine:
            # Likely a better way to do this, but this catches 
            # the garbage at the end of the list
            break
        else:
            result[machine] = 'https://eurekaseven.fandom.com/wiki' + link
    machine, url = random.choice(list(result.items())) # Pick a random machine

    # Save that result to a string and return it
    message = machine + ': ' + url
    return message

class robot(commands.Cog, name='Get a Waifu!'):
    @commands.command(help='Responds with a random robot')
    async def robot(self, ctx):
        func = random.choice([gundam, valvrave, ttgl, lfo])
        await ctx.send(func())

def setup(bot):
    bot.add_cog(robot(bot))
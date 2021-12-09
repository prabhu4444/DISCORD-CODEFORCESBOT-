import discord
import requests
import json
import random
import time
import asyncio
from discord import Embed, Color, Member, utils, File
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
from datetime import datetime
from random import randint
import string

class challengeProblem:
    difficulty = 0

    def __init__(self, problemStatement):
        self.problemStatement = problemStatement


def read_token():
    with open("./parent/bot/token.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip()

token=read_token()

client=discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    channels = ["stalk"]
    if str(message.channel) in channels:
        if message.content.startswith("!stalk"):
            handle = ""
            flag=0
            mess = message.content
            for ele in mess:
                if ele ==' ':
                    flag=1
                elif flag == 1:
                    handle =handle+ele

            embed = discord.Embed(
                description="This may take some time...",
                color=Color(randint(0, 0xFFFFFF)))
            await message.channel.send(content=None, embed=embed)

            link = "https://codeforces.com/api/user.status?handle="
            link = link + handle
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            sub = json_obj['result']

            data = []
            mult = {}

            for x in sub:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult:
                    data.append(x)
                    mult[x['problem']['name']] = 1
                if(len(data) == 10):
                    break

            if(len(data) == 0):
                embed = discord.Embed(
                    description=f'[{handle}](https://codeforces.com/profile/{handle}) has not solved any problems yet.',
                    color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)

            pname = ""
            prating = ""
            for x in data:
                pname += f"[{x['problem']['name']}](https://codeforces.com/problemset/problem/{x['problem']['contestId']}/{x['problem']['index']})\n"
                y = x['problem']
                if 'rating' not in y:
                    prating += "Not Assigned on Codeforces yet\n"
                else:
                    prating += f"{x['problem']['rating']}\n"

            embed = Embed(color=Color.green())
            embed.add_field(name="Recent problems Solved by", value=f"[{handle}](https://codeforces.com/profile/{handle})", inline=False)
            embed.add_field(name="Problem Name", value=pname, inline=True)
            embed.add_field(name="Rating", value=prating, inline=True)
            await message.channel.send(content=None, embed=embed)

        elif message.content.startswith("!lags"):
            handle1 = ""
            handle2 = ""
            mes = message.content
            flag = 0
            for ele in mes:
                if ele == ' ':
                    flag = flag + 1
                elif flag == 1:
                    handle1 = handle1 + ele
                elif flag == 2:
                    handle2 = handle2 + ele

            link = "https://codeforces.com/api/user.status?handle="
            link1 = link + handle1
            link2 = link + handle2

            embed = discord.Embed(
                description="This may take some time...",
                color=Color(randint(0, 0xFFFFFF)))
            await message.channel.send(content=None, embed=embed)

            request_link = requests.get(link1)
            json_obj = json.loads(request_link.text)
            sub1 = json_obj['result']

            request_link = requests.get(link2)
            json_obj = json.loads(request_link.text)
            sub2 = json_obj['result']

            mult1 = {}
            mult2 = {}

            for x in sub2:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult1:
                    mult1[x['problem']['name']] = 1

            for x in sub1:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult2:
                    mult2[x['problem']['name']] = 1


            data = []
            mult3 = {}

            print(len(mult1))
            print(len(mult2))

            for x in sub2:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult2 and x['problem']['name'] not in mult3:
                    data.append(x)
                    mult3[x['problem']['name']]  =  1
                if(len(data) == 10):
                    break

            print(len(data))

            if(len(data) == 0):
                embed = discord.Embed(description=f'[{handle1}](https://codeforces.com/profile/{handle1}) donot lags any problems from [{handle2}](https://codeforces.com/profile/{handle2})',color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None,embed=embed)

            pname = ""
            prating = ""
            for x in data:
                pname += f"[{x['problem']['name']}](https://codeforces.com/problemset/problem/{x['problem']['contestId']}/{x['problem']['index']})\n"
                y = x['problem']
                if 'rating' not in y:
                    prating += "Not Assigned on Codeforces yet\n"
                else:
                    prating += f"{x['problem']['rating']}\n"

            embed = Embed(color=Color.green())
            embed.add_field(name="Some Problems you haven't solved of late ", value=f"[{handle2}](https://codeforces.com/profile/{handle2})", inline=False)
            embed.add_field(name="Problem Name", value=pname, inline=True)
            embed.add_field(name="Rating", value=prating, inline=True)
            await message.channel.send(content=None, embed=embed)

        elif message.content.startswith("!hardest"):
            handle = ""
            flag = 0
            mess = message.content
            for ele in mess:
                if ele == ' ':
                    flag = 1
                elif flag == 1:
                    handle = handle + ele

            embed = discord.Embed(
                description="This may take some time...",
                color=Color(randint(0, 0xFFFFFF)))
            await message.channel.send(content=None, embed=embed)

            link = "https://codeforces.com/api/user.status?handle="
            link = link + handle
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            sub = json_obj['result']

            data = []
            mult = {}

            for x in sub:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult:
                    y = x['problem']
                    if 'rating' not in y:
                        continue
                    data.append([x['problem']['rating'], x])
                    mult[x['problem']['name']] = 1

            if (len(data) == 0):
                embed = discord.Embed(
                    description=f'[{handle}](https://codeforces.com/profile/{handle}) has not solved any rated problems yet.',
                    color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)
            else:
                fdata = sorted(data, key = lambda x: x[0], reverse=True)
                pname = ""
                prating = ""
                count=0
                for y, x in fdata:
                    count = count + 1
                    pname += f"[{x['problem']['name']}](https://codeforces.com/problemset/problem/{x['problem']['contestId']}/{x['problem']['index']})\n"
                    prating += f"{x['problem']['rating']}\n"
                    if count == 10:
                        break

                embed = Embed(color=Color.green())
                embed.add_field(name="Hardest Problem Solved by: ",
                                value=f"[{handle}](https://codeforces.com/profile/{handle})", inline=False)
                embed.add_field(name="Problem Name", value=pname, inline=True)
                embed.add_field(name="Rating", value=prating, inline=True)
                await message.channel.send(content=None, embed=embed)

        elif message.content.startswith("!challenge"):
            handle1 = ""
            handle2 = ""
            tim = ""
            flag = 0
            mess = message.content
            for ele in mess:
                if ele == ' ':
                    flag+=1
                elif flag == 1:
                    handle1 = handle1 + ele
                elif flag == 2:
                    handle2 = handle2 + ele
                elif flag == 3:
                    tim = tim + ele

            if(handle1 == handle2):
                embed = discord.Embed(
                    description="Dijkstra will predict the future for you! The result of the match you proposed will be a tie... You challenged yourself",color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)
            elif tim != '60' and tim != '120':
                embed = discord.Embed(
                    description="1 and 2 hours are the only valid times for challenging an opponent.", 
                            color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)
            else:
                res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
                embed = discord.Embed(
                    description=f'Both the players kindly change your first name on this [link](https://codeforces.com/settings/social) to `{res}` within 60 seconds',
                    color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)

                await asyncio.sleep(60)
                print("Back")
                link1 = f"https://codeforces.com/api/user.info?handles={handle1}"
                request_link = requests.get(link1)
                did1 = json.loads(request_link.text)

                link2 = f"https://codeforces.com/api/user.status?handle={handle2}&from=1&count=1"
                request_link = requests.get(link2)
                did2 = json.loads(request_link.text)

                flag1 = 0
                flag2 = 0

                nam1 = did1["result"][0]
                nam2 = did2["result"][0]

                if nam1['firstName'] == res:
                    flag1 = 1

                if nam1['firstName'] == res:
                    flag2 = 1

                if flag1 == 1 and flag2 == 1:
                    embed = discord.Embed(
                        description="Starting your Match within few seconds.",
                        color=Color(randint(0, 0xFFFFFF)))
                    await message.channel.send(content=None, embed=embed)

                    tags = ['implementation', 'dp', 'math', 'greedy', 'brute force', 
                        'data structures', 'constructive algorithms', 'dfs and similar', 
                        'sortings', 'binary-search', 'graphs', 'trees', 'strings', 'number-theory',
                        'geometry', 'combinatorics', 'two-pointers', 'dsu', 'bitmasks', 
                        'probabilities', 'shortest-paths', 'hashing', 'divide-and-conquer', 
                        'games', 'matrices', 'flows', 'string-suffix-structures', 'expression-parsing', 
                        'graph-matchings']

                    pick = random.choice(tags)
                    print(pick)

                    link = "https://codeforces.com/api/problemset.problems?tags="
                    link = link + pick

                    request_link = requests.get(link)
                    json_obj = json.loads(request_link.text)
                    obj_result = json_obj['result']
                    data = obj_result['problems']

                    give = []
                    mult = {}

                    fdata = []
                    problemSet=[]

                    for x in data:
                        if 'rating' not in x:
                            continue
                        if x['rating'] <= 2000:
                            tempObj=challengeProblem(fdata)
                            tempObj.difficulty=x['rating']
                            problemSet.append(tempObj)
                            fdata.append(x)

                    while True:
                        x = random.choice(fdata)
                        if x['name'] not in mult:
                            mult[x['name']] = 1
                            give.append(x)
                        if(tim == '60' and len(give) == 3):
                            break
                        if(len(give) == 5):
                            break

                    pname = ""
                    i = 0

                    for x in give:
                        pname += f"[{x['name']}](https://codeforces.com/problemset/problem/{x['contestId']}/{x['index']})\n"
                        i+=1

                    embed = Embed(color=Color.green())
                    embed.add_field(name="Best of Luck! Your Match Starts Now!",
                                value=f"[{handle1}](https://codeforces.com/profile/{handle1}) vs [{handle2}](https://codeforces.com/profile/{handle2})", inline=False)
                    if(tim == '60'):
                        val = "A\nB\nC"
                    else:
                        val = "A\nB\nC\nD\nE"
                    embed.add_field(name="Index", value=val, inline=True)
                    embed.add_field(name="Problem Name", value=pname, inline=True)
                    await message.channel.send(content=None, embed=embed)

                    if(tim == '60'):
                        clk = 60*60
                    else:
                        clk = 120*60

                    await asyncio.sleep(clk)

                    sc1 = 0
                    sc2 = 0
                    print("Game Over!")
                    link1 = f"https://codeforces.com/api/user.status?handle={handle1}&from=1&count=30"
                    request_link = requests.get(link1)
                    json_obj = json.loads(request_link.text)
                    sub1 = json_obj['result']

                    link2 = f"https://codeforces.com/api/user.status?handle={handle2}&from=1&count=30"
                    request_link = requests.get(link2)
                    json_obj = json.loads(request_link.text)
                    sub2 = json_obj['result']

                    msub1 = {}

                    for x in sub1:
                        for y in give:
                            if x['problem']['name'] == y['name'] and x['verdict'] == 'OK' and y['name'] not in msub1:
                                sc1 = sc1 + 100
                                msub1[y['name']] = 1

                    msub2 = {}

                    for x in sub2:
                        for y in give:
                            if x['problem']['name'] == y['name'] and x['verdict'] == 'OK' and y['name'] not in msub2:
                                sc2 = sc2 + 100
                                msub2[y['name']] = 1


                    embed = Embed(color=Color.green())
                    embed.add_field(name=f"Match Concluded.",
                                        value=f"[{handle1}](https://codeforces.com/profile/{handle1}) vs [{handle2}](https://codeforces.com/profile/{handle2})\n{sc1}    -    {sc2}",
                                        inline=False)
                    await message.channel.send(content=None, embed=embed)

                else:
                    embed = discord.Embed(
                        description=f"[{handle1}](https://codeforces.com/profile/{handle1}) and [{handle2}](https://codeforces.com/profile/{handle2}) Match cannot be Started! Try Again!",
                        color=Color(randint(0, 0xFFFFFF)))
                    await message.channel.send(content=None, embed=embed)

        elif message.content == '.help':
            embed = discord.Embed(title="Help", 
                            description="Hi! On this channel, you will be using the bot for stalking other users or competing with them on Codeforces.", 
                            color=Color.red(), timestamp=datetime.utcnow())
            
            #await message.channel.send(file=File("discord-codeforces-bot/attachments/search-engine.png"))
            await message.channel.send(file=File("./search-engine.png"))

            embed.set_author(name="Support Bot")
            val = "Displays the recent problems solved by the user"
            embed.add_field(name="!stalk handle", value=val,inline=False)
            embed.add_field(name="!lags handle1 handle2", value="Displays some of the problems solved by user2 which user1 has not solved.", inline=False)
            embed.add_field(name="!hardest handle",value="Displays some of the hardest problem solved by the user",inline=False)
            embed.add_field(name="!challenge handle1 handle2 time(60 or 120 minutes)", 
                            value="Holds an hour or two long match between the users with mentioned handles", inline=False)
            await message.channel.send(content=None, embed=embed)

client.run(token)

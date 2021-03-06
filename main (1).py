import os
import json
import urllib.request
import random
import discord
from discord.ext import commands
import requests
from secrets import spotify_user_id,  discover_weekly_id
from datetime import date
from refresh import Refresh

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.discover_weekly_id = discover_weekly_id
        self.tracks = ""
        self.new_playlist_id = ""

    def find_songs(self):

        print("Finding songs in discover weekly...")
        # Loop through playlist tracks, add them to list

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)

        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()

        print(response)

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        print(self.tracks)
        self.add_to_playlist()

    def create_playlist(self):
        # Create a new playlist
        print("Trying to create playlist...")
        today = date.today()

        todayFormatted = today.strftime("%d/%m/%Y")

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)

        request_body = json.dumps({
            "name": todayFormatted + " discover weekly", "description": "Discover weekly rescued once again from the brink of destruction by your friendly neighbourhood python script", "public": True
        })

        response = requests.post(query, data=request_body, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })

        response_json = response.json()

        return response_json["id"]

    def add_to_playlist(self,args):
        # add all songs to new playlist
        print("Adding songs...")

        self.new_playlist_id = '3HgXydiVriyvnW6cEu8Jnt'

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.new_playlist_id, args)

        response = requests.post(query, headers={"Content-Type": "application/json",
                                                 "Authorization": "Bearer {}".format(self.spotify_token)})

        print(response)

    def call_refresh(self,args):

        print("Refreshing token")

        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        self.add_to_playlist(args)

correct = 'wrong'
difficulty = 'easy'
category = 'null'
answers = []
difficult = 'null'
tokenID= '1234'

amounts = {}
userAnswers = {}

bot = commands.Bot(
	command_prefix="-",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

@bot.command()
async def history(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 23
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def books(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 10
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    await ctx.send(user.mention + '\nCategory is: '+data[0]+'\nDifficuly is: '+data[1]+'\n'+data[2]+'\nAnswer options:'+"\n>>> Option A: "+data[3]+'\nOption B: '+data[4]+'\nOption C: '+data[5]+'\nOption D: '+data[6]+'\nRespond with ?answers A,B,C or D with your response')

@bot.command()
async def entertainment(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = random.randrange(10, 16)
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def theatre(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 13
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def add(ctx,*args): 
    songs= ""
    for f in args:
        songs+=f+","
    songs = songs[:-1]

        
    a = SaveSongs()
    a.call_refresh(songs)
    await ctx.send("Added your song to the public playlist, it can be found here:\nhttps://open.spotify.com/playlist/3HgXydiVriyvnW6cEu8Jnt")
    
@bot.command()
async def film(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 11
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)



@bot.command()
async def trivia(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = random.randrange(9, 32)
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def computers(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 18
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def cartoons(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 32
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def animals(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 27
    print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def boardgames(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 16
    print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def videogames(ctx):
    global userAnswers
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 15
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)


@bot.command()
async def tv(ctx):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    data = [6]
    quizVar = 14
    #print(quizVar)
    data = url_request(quizVar)
    userAnswers[id] = int(data[7])
    _saveA()
    #print(userAnswers[id])
    embed=discord.Embed(title='TRIVIA')
  
    embed.add_field(name='Category:',value=data[0],inline=True)
    embed.add_field(name='Difficulty',value=data[1],inline=True)
    embed.add_field(name='Question',value=data[2],inline=False)
    embed.add_field(name='A: '+data[3],value='______',inline=False)
    embed.add_field(name='B: '+data[4],value='______ ',inline=False)
    embed.add_field(name='C: '+data[5],value='______ ',inline=False)
    embed.add_field(name='D: '+data[6],value='______ ',inline=False)
    embed.set_footer(text =  'Reply -answer (a,b,c or d) to answer')
    await ctx.send(embed=embed)




@bot.command()
async def answer(ctx,*,args):
    id = str(ctx.message.author.id)
    user = bot.get_user(int(id))
    if id not in amounts:
        amounts[id] = 0
        await ctx.send("You are now registered")
        _save()

    #print(userAnswers[id])

    correct = userAnswers[id]
    if correct == 1:
      correct = 'A'
    elif correct == 2:
      correct = 'B'
    elif correct == 3:
      correct = 'C'
    elif correct == 4:
      correct = 'D'
    elif correct ==0:
      correct = 'https://media1.tenor.com/images/255df1d886da07cd869f7425a6b73014/tenor.gif?itemid=11397484'

    if args == 'a':
      args = 'A'
    elif args == 'b':
      args = 'B'
    elif args == 'c':
      args = 'C'
    elif args == 'd':
      args = 'D'
    
    embed=discord.Embed(title="Answer")
    print(correct)

    if args == correct:
      amounts[id] +=10
      values = "Your total score is: "+str(amounts[id])
      embed.add_field(name="CORRECT!", value=values, inline=False)
      _save()
    else:
      values = "Correct answer was: "+str(correct)
      embed.add_field(name="INCORRECT!", value=values,inline=False)

    await ctx.send(embed=embed)
    userAnswers[id] = 0

embed=discord.Embed(title="Trivia Bot Categories")
embed.add_field(name="-trivia", value="Gives a question from a random category", inline=False)
embed.add_field(name="-history", value="Gives a history question", inline=False)
embed.add_field(name="-books", value="Gives a book question", inline=False)
embed.add_field(name="-film", value="Gives a film question", inline=False)
embed.add_field(name="-entertainment", value="Gives a question from the film category", inline=False)
embed.add_field(name="-theatre", value="Gives a question from the theatre category", inline=False)
embed.add_field(name="-animals", value="Gives a question from the animal category", inline=False)
embed.add_field(name="-videogames", value="Gives a question from the video games category", inline=False)
embed.add_field(name="-computers", value="Gives a question from the computer category", inline=False)
embed.add_field(name="-cartoons", value="Gives a question from the cartoons category", inline=False)
embed.add_field(name="-boardgames", value="Gives a question from the boardgames category", inline=False)
embed.add_field(name="-tv", value="Gives a question from the television category", inline=False)

@bot.command()
async def categories(ctx):
    id = str(ctx.message.author.id)
    global embed
    await ctx.send(embed=embed)



bot.author_id = 487258918465306634  # Change to your discord id!!!

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

def _saveA():
    with open('answers.json', 'w+') as f:
        json.dump(userAnswers, f)
        
def url_request(value : int):
    global tokenID
    url = 'https://opentdb.com/api.php?amount=1&category='+str(value) +'&type=multiple&token='+tokenID

    data = [6]
    response = urllib.request.urlopen(url)
    data = json.load(response)
    print('Data is:')
    print(data)
    responsecode = data['response_code']
    if str(responsecode) == '4':
      url2 = 'https://opentdb.com/api_token.php?command=reset&token='+tokenID
      response2 = urllib.request.urlopen(url2)
      data2 = json.load(response2)
    elif str(responsecode)== '3':
        url2 = 'https://opentdb.com/api_token.php?command=request'
        response2=urllib.request.urlopen(url2)
        data2 = json.load(response2)
        tokenID=data2['token']
        print(tokenID)
        data = url_request(value)
        return data
    else:   
        print(data['response_code'])
        question = data['results']
        for f in question:
            data[0] = f['category']
            data[1] = f['difficulty']
            correctAnswer = f['correct_answer']
            answers = f['incorrect_answers']
            data[2] = f['question']

        answers.append(correctAnswer)

        random.shuffle(answers)


        global correct 
        correct = correctAnswer

        global difficulty
        difficulty = difficult

        answers[0] = answers[0].replace("&#039;","'")
        answers[1] = answers[1].replace("&#039;","'")
        answers[2] = answers[2].replace("&#039;","'")
        answers[3] = answers[3].replace("&#039;","'")

        if answers[0] == correct:
          correct = 1
        if answers[1] == correct:
          correct = 2
        if answers[2] == correct:
          correct = 3
        if answers[3] == correct:
          correct = 4

        answers[0]=answers[0].replace('&amp;','&')
        answers[1]=answers[1].replace('&amp;','&')
        answers[2]=answers[2].replace('&amp;','&')
        answers[3]=answers[3].replace('&amp;','&')


        data[3]=answers[0]
        data[4]=answers[1]
        data[5]=answers[2]
        data[6]=answers[3]
        data[7]=correct


        data[2]=data[2].replace('&quot;','"')
        data[2]=data[2].replace('&#039;',"'")

        return data



@bot.event 
async def on_ready():  # When the bot is ready
    global amounts
    # Opening JSON file 
    f = open('amounts.json',) 
    data = json.load(f) 
    #print(data)
    amounts = data
    print("I'm in")
    activity = discord.Game(name="Type -categories for how to play!")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    #print(bot.user)  # Prints the bot's username and identifier

@bot.command(pass_contex=True)
async def leaderboard(ctx):
  leaderboard = {}
  for f in amounts:
    print('f is: '+f+'\n')
    user = bot.fetch_user(f)
    print('username is: '+user.display_name)
    try:
    	leaderboard[user.name] = amounts[f]
    except:
        leaderboard[user] = amounts[f]

  sortedV = sorted(leaderboard.items(),key = lambda t:t[1])
  sortedV.reverse()
  print(sortedV)
  #print(sortedV)
  await ctx.send("**TRIVIA BOT LEADERBOARD**")
  count = 1
  for f in sortedV:
    await ctx.send(">>> "+str(count)+" "+str(f))
    count = count+1

@bot.command(pass_context=True)
async def score(ctx):
    id = str(ctx.message.author.id)
    if id in amounts:
        await ctx.send("Your total score is {} ".format(amounts[id]))
    else:
        await ctx.send("You do not have an account")

@bot.command()
async def ping(ctx):
    await ctx.send('-ping')

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.


token = 'No Token Here'
bot.run(token)  # Starts the bot



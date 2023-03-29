import praw
import time

username = "RestComplex2111"
secret = "my2wieMOdMbf85vEKPX198hjuqpxqQ"
client_id = "r0Nk2GkbbY8z84bWDqrigQ"
password = "jziXoN4qo#@@HL"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0"
subs = ['computervision', 'plantclinic', 'houseplants', 'whatsthisplant','linuxmint', 'MechanicalKeyboards', 'NatureIsFuckingLit', 'ProCreate', 'scuba', 'opensource', 'datascience', 'ObsidiaMD', 'PowerBI', 'dogsonroofs', 'DramaticHouseplants', 'AnimalsBeingDerps', 'funny', 'gifs', 'aww', 'science', 'technology', 'books', 'movies', 'music', 'food', 'gaming']

def write_line(line, file_name):
        with open(file_name, 'a') as file:
            file.write(line)

def user_login(client_id, client_secret,username,password,user_agent):
    # reddit api login
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent=user_agent)
    return reddit

reddit = user_login(client_id, secret, username, password, user_agent)

subreddit = reddit.subreddit('+'.join(subs))

count = 1
for submission in subreddit.stream.submissions(skip_existing=True):
    submision_id = submission.id
    date_posted = time.ctime(submission.created_utc)	
    vote_count = submission.score
    title = submission.title
    sub = submission.subreddit

    line = f"{submision_id}, {sub}, {date_posted}, {vote_count}, {title}\n"

    if vote_count <= 1:
        if count % 2 == 0:
            submission.upvote()
            write_line(line, 'upvoted.txt')
        else:
            write_line(line, 'not_upvoted.txt')
    count += 1
from InstaBot import InstaBot
import random
import sys
import datetime


def main():
    # Get username and password from Command line
    if len(sys.argv) != 4:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    logPath = sys.argv[3] + "/log.txt"

    likes = random.randint(50, 85)
    hashtags = ["love", "instagood", "photooftheday", "fashion", "beautiful", "happy", "cute", "tbt", "like4like",
                "followme", "picoftheday", "follow", "me", "selfie", "summer", "art", "instadaily", "friends", "repost",
                "nature", "girl", "fun", "style", "smile", "food", "instalike", "likeforlike", "family", "travel",
                "fitness", "igers", "tagsforlikes", "follow4follow", "nofilter", "life", "beauty", "amazing",
                "instamood", "instagram", "photography"]

    hashtag = hashtags[random.randint(0, 39)]

    bot = InstaBot(username, password)
    bot.get_post(hashtag)
    bot.like_photos(likes)
    bot.signout()

    current_time = datetime.datetime.now()
    msg = "Bot ran at " + current_time.strftime("%d-%b-%Y (%H:%M:%S.%f)") + " and liked " + str(likes) + " photos.\n"

    logFile = open(logPath, "a")
    logFile.write(msg)
    logFile.close()


if __name__ == "__main__":
    main()

import os
import textwrap
from typing import Generator

import praw
from discord import Embed, SyncWebhook
from dotenv import load_dotenv
from praw.models import Submission

load_dotenv()

r = praw.Reddit(os.getenv("BOT_USERNAME"), user_agent=os.getenv("USER_AGENT"))  # type: ignore

webhook = SyncWebhook.from_url(os.getenv("WEBHOOK_URL"))  # type: ignore

print("Logged in and awaiting subreddit stream.")


def do_feed(post: Submission):

    e = Embed(title=textwrap.shorten(post.title, width=256), url=post.shortlink)
    e.set_author(
        name=f"u/{post.author.name}",
        url=f"https://reddit.com/u/{post.author.name}",
        icon_url=post.author.icon_img,
    )

    # if a thumbnail exists, let's add it
    # there are better and bigger images we could use,
    # but it requires a lot of checking and sanitizing, so this is fine
    thumbnail = post.thumbnail
    if thumbnail != "self":
        e.set_thumbnail(url=thumbnail)

    if post.selftext:
        e.description = f">>> {textwrap.shorten(post.selftext, width=512)}"

    webhook.send(embed=e)


sub_stream: Generator[Submission, None, None] = r.subreddit(os.getenv("SUBREDDIT")).stream.submissions(skip_existing=True)  # type: ignore

for post in sub_stream:
    do_feed(post)

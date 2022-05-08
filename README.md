
# Subreddit Feed

A small script to listen to a subreddit's incoming posts and spits them out into a Discord channel using a webhook.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`USER_AGENT` - reddit's requirement to running reddit bots.

`BOT_USERNAME` - The name of the bot you're using. This is to load the praw.ini file. If you don't know how to make a praw.ini file, please refer to [praw's Github repository](https://github.com/praw-dev/praw)

`SUBREDDIT` - The subreddit or subreddits (multiple can be delimited with `+`) that you want to send posts from.

`WEBHOOK_URL` - The Discord webhook url for the output channel. If you want to send the message to a thread, that requires passing the thread like so: `webhook.send(thread=discord.Object(thread_id))`

## Deployment

To deploy this script after filling in the environment variables + `praw.ini`, just run

```bash
  pip install -r requirements.txt
  python ./feed.py
```


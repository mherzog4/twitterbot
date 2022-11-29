
import tweepy


import config


def about_me(client: tweepy.Client) -> None:
 
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")


def get_my_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
    me = client.get_user(username="mattherzog5")
    response = client.get_users_tweets(me.data.id)
    return response.data


if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_SECRET,
    )
    print("=== About Me ===")
    about_me(client)
    print()
    print("=== My Tweets ===")
    for tweet in get_my_tweets(client):
        print(tweet, end="\n\n")
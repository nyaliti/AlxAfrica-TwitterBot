# Alxafrica Twitter Retweet Bot

This bot retweets tweets from the user @alx_africa.

## Dependencies

- Tweepy: Python library for accessing the Twitter API
- Python-dotenv: Library for managing environment variables

## Setup

1. Install Tweepy and Python-dotenv:

   ```bash
   pip install tweepy python-dotenv

2. Create a .env file with your Twitter API credentials:
```bash
CONSUMER_KEY='your_consumer_key'
CONSUMER_SECRET='your_consumer_secret'
ACCESS_TOKEN='your_access_token'
ACCESS_TOKEN_SECRET='your_access_token_secret'
```
3. Deploy the bot using Azure Functions:
<ul>
<li> Sign in to the Azure portal (https://portal.azure.com) or create a new account if you don't have one.</li>

<li>Create a new Azure Functions resource.</li>
<li>Configure the Azure Function by adding the environment variables mentioned in step 2.</li>
<li>In the Azure portal, navigate to your Function App and open the Function.</li>
<li>Replace the existing code with the code from main.py.</li>
<li>Save the function and monitor the logs to ensure successful execution.</li>
</ul>

4. Confirm the bot is working:
<ul>
<li>Send a tweet mentioning `@alxafrica`.</li>
<li>Monitor the logs in the Azure portal to verify that the bot successfully retweets the tweet.</li>
<li>Check the target Twitter account to confirm if the tweet has been retweeted.</li>
</ul>

<p>
Now you have successfully deployed the Alxafrica Twitter Retweet Bot on Azure Functions. The bot will automatically retweet tweets from the user `@alxafrica`. Ensure that you have installed the required dependencies, set up the environment variables, and deployed the bot on Azure Functions. Follow the provided steps to confirm that the bot is functioning as expected.
</p>
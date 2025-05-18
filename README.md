# BOTS

This repo illustrates how the Telegram and Discord APIs can be used to create messaging bots for the Telegram and Discord (TBA) clients.

The bots make a POST request to an API to generate a response to a user message.

- In my case this is my private LLM server that is running as a dockerised application on my home network.
- The OpenAI or OpenRouter APIs can quite easily be used as an alternative.
- Discord bot TBA.

## Build Docker Image

```bash
export APP_VERSION=0.0.0
docker build --tag scriptorpius:$APP_VERSION .
```

## Run Docker Image

```bash
docker run -d -e ENV=$ENV -e USERNAME=$USERNAME -e PASSWORD=$PASSWORD -e MONGO_HOST=$MONGO_HOST -e BOT_TOKEN=$BOT_TOKEN -e API_URL=$API_URL scriptorpius:$APP_VERSION
```
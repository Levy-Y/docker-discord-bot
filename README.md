# docker-discord-bot

This repository contains the required files to build a Docker container, which is running a python discord bot.

## Getting Started

To get started with this bot, you will need to have Docker installed on your system. You can download Docker [here](https://www.docker.com/products/docker-desktop/).

## Installation

Follow these steps to run the bot:

1. Clone the repository using the following command: <br>
```bash
git clone https://github.com/Levy-Y/docker-discord-bot
```

2. Navigate to the directory using the following command: <br>
```bash
cd docker-discord-bot
```

3. Open the **docker-compose.yml** file and replace *YOURTOKEN* with your Discord bot token.

4. Run the following command to build the Docker image: <br>
```bash
docker build ./
```

6. To start the container enter the following command: <br>
```bash
docker-compose up -d
```
*(Note: this will start the container in detached mode)*

## Option B:
You can also just run the docker-compose_NO-BUILD.yml file after cloning this repository, like:
```bash
docker-compose -f docker-compose_NO-BUILD.yml up -d
```
*(Note: you'll need the bot.py otherwise the command will exit)*

## Usage
The bot will now be running and ready to respond to commands. You can add the bot to your Discord server by creating a new application and adding a bot to it. Follow the steps outlined in the [Discord Developer Portal](https://discord.com/developers/applications) to create a new application and add a bot to it.

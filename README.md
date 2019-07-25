# Bot for tracking your time from google calendar

![video](./gif.gif)

This bot helps you generate useful reports of you time spent
on projects. For this you use a system of special [tags] in
your google calendar

# Deploying
1. cp .env.example .env
2. generate the bot token with bot father and
paste to .env
3. go to [google console](https://console.developers.google.com/apis/credentials?project=quickstart-1553576795082) and click
"create credentials" and choose "service account key"
to generate the secrets.json

4. docker-compose up
5. follow bot instructions

# max-flood-bot
Max flood bot

Build image:
```commandline
docker build . -t max-bot
```

Run cmd:
```commandline
docker run --name max-bot --rm -i -t max-bot bash
```

Run server:
```commandline
docker run --name max-bot --rm -e "PORT=80" -e "DEBUG=1" --env-file ./.env  max-bot
```

# STAR

work-in-progress

## Getting started

STAR lets you monitor the run or restart your simulation and lets you know when it crashes all on either your phone via DISCORD or a via a website interface (responsive).

### Quick Start

#### Check for Redis

```bash
  redis-server --version
```

if the output says something along the lines of `command not found`,
you can install it from your operating system's package manager(for more details).

#### Installing STAR

The easiest way to try out STAR is to go to one of these pages and follow the instructions

- [ only discord ](http://abhishek-deshmukh.github.io)
- [ only webpage ](http://abhishek-deshmukh.github.io)
- [ both discord and webpage ](http://abhishek-deshmukh.github.io)

## Developer Guide

#### How to start the back-end

- source the `env`
- `cd STAR/backend`
- `./start.sh`

#### How to start the bot

- source the `env`
- `cd STAR/front_discord_bot`
- `python3 bot.py`

#### How to start the website

- `cd STAR/front_website`
- `npm install`
- `npm run build`
- `cd ./dist`
- `python -m http.server`

derived from the work of James Powell
A tool of doing and monitoring remote development easier.

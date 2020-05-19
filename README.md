<img src="./STAR/static/logo.svg.png" width="200px;">

# STAR

version: 0.0.0

STAR can be used to convert your script into a website within minutes.


## Getting started

STAR lets you monitor the run or restart your simulation and lets you know when it crashes all on either your phone via DISCORD or a via a website interface (responsive).

### Quick Start

#### Check for Redis

```bash
  $ redis-server --version
```

if the output says something along the lines of `command not found`,
you can install it from your operating system's package manager(for more details).

#### Installing STAR

The easiest way to try out STAR is to, go to [this Blog post](https://deshmukh-blog.netlify.app/detail/2.html) and follow the instructions.

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

### ToDo-s
[ ] other languages support
[ ] make output human readable
[ ] allow more than single object output

##### Credits

derived from the work of James Powell
A tool of doing and monitoring remote development easier.

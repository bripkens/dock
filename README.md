# dock
**dock** is a shell script to help you easily bootstrap databases and other
tools that you need for development purposes. Instead of installing something
like MongoDB or Redis natively on your machine, you can run it in a Docker
container with just a single command `dock mongodb`. The main purpose of
**dock** is to make the interaction with Docker dead simple for quick prototypes
and hackathons.

## Typical usage

```
$ dock redis
Starting redis (using /Users/ben/.dock/programs/redis)
b35bd1175e720b563f333fdcd27a33a35e0e05ce9bc79bbb3b69dd67ceb71867
Redis started. Listening on port 6379.
```

For additional usage instructions, run `dock` without arguments.

## Installation
First make sure that you have [Docker](https://docs.docker.com/) running on
your machine.

### Installation on OS X using [Homebrew](http://brew.sh/)
```
brew tap bripkens/dock
brew install dock
```

### Upgrade on OS X using Homebrew
```
brew upgrade dock
```

### Installation on other platforms
Just download `dock` and put it somewhere on your $PATH. Then:
```
chmod +x /path/to/dock   # Make dock executable
dock -u                  # Initialise dock
```

You can automate this with the following one-liner (assuming ~/bin is on your $PATH).
```
curl https://raw.githubusercontent.com/bripkens/dock/master/dock -so ~/bin/dock && \
     chmod +x ~/bin/dock && \
     dock -u && \
     echo "dock installation successful. Try running 'dock'"
```

## Supported programs
For a list of supported programs run `dock -l` or check out this repository's
[programs/](https://github.com/bripkens/dock/tree/master/programs) directory.
Feel free to send a pull request for any awesome Docker containers that are
still missing!

## Credits
dock was written by Ben Ripkens ([@BenRipkens](https://twitter.com/BenRipkens)).

Structure and readme are heavily inspired by Simon Whitaker's [gibo](https://github.com/simonwhitaker/gibo).

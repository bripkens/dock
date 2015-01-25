# dock
**dock** is a shell script to help you easily bootstrap databases and other
tools that you need for development purposes. Instead of installing something
like MongoDB or Redis natively on your machine, you can run it in a Docker
container with just a single command `dock mongodb`. The main purpose of
**dock** is to make the interaction with Docker dead simple for quick prototypes
and hackathons.

## Typical usage

```
$ dock redis jenkins mongodb rabbitmq

Starting redis (using /Users/ben/.dock-formulas/formulas/redis)
Container started
Name:           redis
IP:             192.168.59.103
Ports:          6379

Starting jenkins (using /Users/ben/.dock-formulas/formulas/jenkins)
Container started
Name:           jenkins
IP:             192.168.59.103
Ports:          8472

Starting mongodb (using /Users/ben/.dock-formulas/formulas/mongodb)
Container started
Name:           mongodb
IP:             192.168.59.103
Ports:          27017

Starting rabbitmq (using /Users/ben/.dock-formulas/formulas/rabbitmq)
Container started
Name:           rabbitmq
IP:             192.168.59.103
Ports:          5672 15672
Admin user:     admin
Admin pw:       A3y6crBkMk8k
```

For additional usage instructions, run `dock` without arguments.

## Installation
First make sure that you have [Docker](https://docs.docker.com/) running on
your machine. Then continue with the installation of dock:

*As of the time of writing the Homebrew Docker installer is broken. [boot2docker](https://github.com/boot2docker/osx-installer/releases) is currently the easiest way to get a working Docker environment on OS X.*

*dock versions >= 1.0.0 are compatible with boot2docker 1.3 and beyond. Please use v0.6.3 when you are using an old boot2docker version or upgrade your boot2docker installation.*

### Installation on OS X using [Homebrew](http://brew.sh/)
```
brew tap bripkens/dock
brew install dock
```

### Upgrade on OS X using Homebrew
```
brew update
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
[formulas/](https://github.com/bripkens/dock/tree/master/formulas) directory.
Feel free to send a pull request for any awesome Docker containers that are
still missing!

## Private formulas
Dock will look for custom formulas in a `.dock-formulas` directory relative to
your current working directory. So if you need a formula for a custom docker
image that you don't want to make public through docker hub, you can put your
formulas there.

## Contributing formulas
I will gladly accept your formulas. The following points describe the basic
process of adding a new formula.

 - [Fork this repository](https://github.com/bripkens/dock/fork)
 - `git clone <your fork>`
 - Add a new file to the `formulas/` directory
 - Check out existing formulas for the basic formula structure
 - Try the new formula locally `bash forumlas/<my new formula>`
 - Commit, push and open a pull request

## Credits
dock was written by Ben Ripkens ([@BenRipkens](https://twitter.com/BenRipkens)).

Structure and readme are heavily inspired by Simon Whitaker's [gibo](https://github.com/simonwhitaker/gibo).

# dock changelog

## 1.2.1
 - `dock --redock` was removed as the parent shell's environment cannot
   be manipulated.

## 1.2.0
 - Thanks to [@britter](https://github.com/britter) you now set Docker
   environment variables via `dock --redock`.

## 1.1.0

 - Thanks to [@britter](https://github.com/britter) it is now possible to have
   private formulas. dock will search for `.dock-formulas/` directories in
   your current working directory and will start matching formulas.
 - Docker 1.3 changed the console output on which dock relied. This resulted
   in issues when a formula was started for the first time.
 - Docker provides information about image downloads. This information will now
   be forwarded to dock users.
 - `dock --rm` will now only stop containers that were started via dock. This
   is done by prefixing all container names with `dock-`.

## 1.0.0

 - environment variables are automatically set to the new
   IANA registered port 2376. This is a breaking change for
   boot2docker users. Please update to boot2docker and
   Docker 1.3.

## 0.6.3

 - `redock` needs to be run before checking Docker availability.

# Postcards [![PyPI version](https://img.shields.io/pypi/v/postcards.svg)](https://badge.fury.io/py/postcards)

Postcards is a set of python scripts that allow you to send postcards with the Swiss Postcard Creator.

## Install
This package requires python 3.6 or later.

```sh
# pip for python3 is required
pip install postcards
```

or install from source (checkout latest tag)

```sh
git clone git@github.com:abertschi/postcards.git
cd postcards/
pip install .
```

Installation of `postcards` will expose these console scripts:
```
postcards
postcards-folder
postcards-pexels
postcards-random
postcards-chuck-norris
postcards-birthdays
```
Issue `--help` for more information.

## Usage
```
$ postcards -h

usage: postcards [-h] [-v] {generate,send,encrypt,decrypt} ...

Postcards is a CLI for the Swiss Postcard Creator

positional arguments:
  {generate,send,encrypt,decrypt}
    generate            generate an empty configuration file
    send                send postcards
    encrypt             encrypt credentials to store in configuration file
    decrypt             decrypt credentials

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increases log verbosity for each occurrence.

sourcecode and documentation: https://github.com/abertschi/postcards

```

## Getting started
Create a configuration file by issuing
```bash
$ postcards generate
```
A [configuration file](./postcards/template_config.json)
holds various information relevant to send postcards.

### Examples
Issue `postcards send --help` for more information about sending postcards.

```bash
# Send a postcard
$ postcards send --config config.json \
    --picture https://images.pexels.com/photos/365434/pexels-photo-365434.jpeg \
    --message "Happy <br/> coding!"


# Encrypt user passwords to store in configuration file
$ postcards encrypt mypassword


# Send a postcard with encrypted passwords stored in configuration file
$ postcards send --config config.json \
    --key \
    --picture https://images.pexels.com/photos/365434/pexels-photo-365434.jpeg \
    --message "Happy coding"
```

## Plugins
Postcards is designed in a plugin based approach.
Plugins set the text and / or picture of your postcards.

Postcard pictures and text can always be overwritten by commandline by issuing
`--picture <picutre>` and `--message <message>`.

These plugins are available:
- [Plugin: postcards-folder](#plugin-postcards-folder)
- [Plugin: postcards-pexels](#plugin-postcards-pexels)
- [Plugin: postcards-random](#plugin-postcards-random)
- [Plugin: postcards-chuck-norris](#plugin-postcards-chuck-norris)
- [Plugin: postcards-birthdays](#plugin-birthdays)
- [Build your own plugin](#build-your-own-plugin)

### Plugin: postcards-folder
Send pictures from a folder.  

Add the following object to your configuration file
```json
{
 "payload": {
    "folder": "./pictures",
    "move": true
  }
}
```

- `folder`: location to a folder containing your images (required)
- `move`: set to false if sent picture should not be moved to a subdirectory `./sent/` (default: true)

#### Example
```
$ postcards-folder send --config ./my-config.json --message "coding rocks"
```
#### Slice a picture into tiles
`postcards-folder` comes with a command called `slice` to create tiles from an image.
This is useful to create a poster-like picture with postcards.

Issue `postcards-folder slice --help` for more information.

### Plugin: postcards-pexels  
Send postcards with random pictures from www.pexels.com.

No configuration is necessary in your configuration file.

#### Example
```
$ postcards-pexels send --config ./config.json --message "coding rocks"
```

### Plugin: postcards-random  
Surprise, surprise! This plugin chooses an arbitrary picture from the
internet as postcard picture.
Picture may be inappropriate, so use with caution.

No configuration is necessary in your configuration file.

#### Example
```
$ postcards-random send --config ./config.json \
  --message "So much of life, it seems to me, is determined by pure randomness. \
   So is this postcard picture."
```

### Plugin: postcards-chuck-norris  
Chuck Norris's first program was kill -9!

Receive postcards with Chuck Norris statements.
A postcard picture is chosen according to the nouns found in the joke. Pictures are from www.pexels.com

No configuration is necessary in your configuration file.

#### Example
```
$ postcards-chuck-norris send --config ./config.json --category nerdy --duplicate-file duplicates.txt
```
- Issue `postcards-chuck-norris send --help` for more information about the additional flags.

### Plugin: postcards-birthdays  

Check if it's a friend's birthday in the next few days and send him a birthday postcard. Can be scheduled to run once a day on a pi.

A birthday.json file is required.

```json
{
 "birthdays":[
   {
      "birthdate":"07.02.1812",
      "recipient": {
        "firstname": "charles",
        "lastname": "dickons",
        "street": "48 Doughty St",
        "zipcode": "WC1N 2LX",
        "city": "London"
      },
    }
  ],
  "wishes":[
      "Happy Birthday",
      "Tanti Auguri",
      "Hoffe hesch ä super Tag"
  ]
}
```

- `days-ahead`: number of days early postcards will be sent


#### Example
```
$ postcards-birthday send --birthdays ./birthday.json --days-ahead 3
```

### Build your own plugin
1. Extend the class `postcards.Postcards()`
2. Overwrite `def get_img_and_text(self, payload, cli_args)`
3. Add CLI parser functionality by overwriting `enhance_*_subparser` methods

```python
from postcards.postcards import Postcards
import sys

class MyPlugin(Postcards):

    def get_img_and_text(self, plugin_config, cli_args):
      return {
            'img': '...',
            'text': '...'
        }

if __name__ == '__main__':
    MyPlugin().main(sys.argv[1:])

```
```sh
$ python my_plugin.py --help
```

## Release notes
### v0.0.8, 2018-03-28
- v0.0.7 broke due to changes in the postcardcreator API
 - update `postcard-creator` to `0.0.8`

### v0.0.7, 2017-11-22
- Bug fixing release
- Remove unused dependencies
- update `postcard-creator` API wrapper to `0.0.6`

### v0.0.6, 2017-08-13
- Bug fixing

### v0.0.5, 2017-08-12
- Introduce new plugin `postcards-chuck-norris`
- Add flag `--all-accounts` to global `postcards`


## Development notes
```sh
pip install -r requirements-dev.txt
pip install -e .
```

## Related
- [postcard_creator_wrapper](https://github.com/abertschi/postcard_creator_wrapper) - Python API wrapper around the Swiss Postcard Creator

## Author
Andrin Bertschi and [friends](https://github.com/abertschi/postcards/graphs/contributors)

## License

MIT

# How to install

```bash
pip install baltimorestrings.argparse_showhelp
```

# How to use

Use just like a normal argparse, but import like this:

```python3
from baltimorestrings.argparse_showhelp import ArgumentParserShowHelpOnError as ArgumentParser
```

It'll show the help output if a user messes up the arguments, and it uses a Formatter
that doesn't strip `\n`s from helptext.

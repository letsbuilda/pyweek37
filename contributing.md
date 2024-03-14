# Contributing
Follow these steps to start working on this game.

## Rye
Rye is the preferred manager for this project. Install it [here](https://rye-up.com/guide/installation/).

Once installed, simply run these commands to launch the game.
```bash
rye sync
rye run pyweek37
```

## Pip
If you don't want to use Rye, you may also use pip.

Set up your venv and run the following:
```bash
python -m pip install -r requirements.lock
python -m src.pyweek37
```

# Pushing
Before you push, please make sure you run `rye fmt` (or `black` if you don't have rye) to format the code.

Note that you cannot push directly to main, you must push to a branch. Create one with `git branch <my-feature>`.
Once you push, someone must review the changes and approve them before they are merged into main.

# Acknowledgement
Please list your name below if you read through this document and can run the game:
- Anonymous4045

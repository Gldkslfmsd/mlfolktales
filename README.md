# mlfolktales

## What is this?

This is a contribution to folkloristics research. We created an automatic
classifier of folktales from mtfd.org by their ATU index. Read report in
`report/` directory for more info.

## What do you find here?

Many of source codes in this repo are one-purpose scripts, many of scripts
can serve as an entry-points for their purpose.

Here is a short summary of the non-self-explanatory files:

`clf*.py`

- codes used for classification

`dp*.py`

- dp = data preprocessing

`feat*.py`

- feature extraction/selection/design/...

`gen*.py`

- generated source codes

## How to run

Use virtualenv:

`virtualenv -p python3 p3`

and virtual environment:

`source p3/bin/python3`

Firstly, installed required packages:

`pip install -r pip_requirements.txt`

And then good luck ;) 

If you want to contribute and add a new module:

`pip freeze > pip_requirements.txt`

and commit `pip_requirements.txt`

## Contributions

Dominik Macháček @Gldkslfmsd <dominik.machacek-at-matfyz.cz>

- `wc -lc *.py observations/*.py`
- 1117 lines of source code
- 33118 bytes of source code

Martin Banzer @tensorride <martin.banzer-at-gmx.de>

- `wc -lc martin/*/*/*.py martin/*/*/*/*.py`
-  6382 lines of source code
-  164529 bytes of source code

Simon Ahrendt @SimonAhrendt 

- `wc -lc crawler/*.py`
- 501 lines of source code
- 17948 bytes of source code

This project was created on Saarland University, Saarbrücken, Germany, on
a project seminar "Similarity Computations in Folktale Texts" in year 2016/17. Our supervisor is Thierry Declerck.

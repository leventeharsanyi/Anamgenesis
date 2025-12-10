# Anamgenesis

Small Streamlit demo app using **Python 3.12** and **Poetry**.

## Requirements
- Python 3.12
- Poetry
- Git

## Setup

```bash
git clone https://github.com/leventeharsanyi/Anamgenesis
cd anamgenesis
poetry env use python3.13
poetry shell
poetry install
```

## Adding an env file and put a secret key there
The .env should be at the level of pyproject.toml. For testing purposes add a secret like this to the env. Also add the ELEVENSLAB api key.

```bash
MY_SECRET_MESSAGE=You_did_it!
ELEVENLABS_API_KEY=<YOUR_API_KEY>
```

## Running the app

```bash
poetry run streamlit run app/main.py
```
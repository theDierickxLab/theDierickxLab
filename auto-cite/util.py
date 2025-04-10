from sys import exit
import os
import subprocess
import json
import yaml
from yaml.loader import SafeLoader
from datetime import datetime

yaml.Dumper.ignore_aliases = lambda *args: True

directory = os.path.dirname(os.path.realpath(__file__))

default_date = [1900, 1, 1]

os.system("")

palette = {
    "white": "\033[97m",
    "gray": "\033[90m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}

levels = {1: "purple", 2: "cyan", 3: "white"}

def log(message="", level=1, color=""):
    if not color:
        color = levels[level]

    if level == 1:
        message = message.upper()

    print(f"{(level - 1) * '  '}{palette[color]}{message}{palette['reset']}\n")


def get_cached(source, citations):
    _cache = source.get("_cache")
    if not _cache:
        return
    matches = [citation for citation in citations if citation.get("_cache") == _cache]
    if len(matches) == 1:
        return matches[0]

def date_part(citation, index):
    try:
        return citation.get("issued").get("date-parts")[0][index]
    except Exception:
        return default_date[index]


def clean_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except Exception:
        return "-".join(str(part) for part in default_date)


def load_data(filename, type_check=True):

    path = os.path.join(directory, filename)

    if not os.path.isfile(path):
        raise Exception(f"Can't find {filename}")

    try:
        file = open(path, encoding="utf8")
    except Exception as e:
        raise Exception(e or f"Can't open {filename}")

    try:
        with file:
            data = yaml.load(file, Loader=SafeLoader)
    except Exception:
        raise Exception(f"Can't parse {filename}. Make sure it's valid YAML.")

    if type_check:
        if type(data) != list:
            raise Exception(f"Top level of {filename} is not a list")

        for entry in data:
            if type(entry) != dict:
                raise Exception(f"Not all entries in {filename} are dictionaries")
    return data


def save_data(filename, data):
    path = os.path.join(directory, filename)

    try:
        file = open(path, mode="w")
    except Exception:
        raise Exception(f"Can't open {filename} for writing")

    try:
        with file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
    except Exception:
        raise Exception(f"Can't dump {filename} as YAML")

    note = "# DO NOT EDIT, GENERATED AUTOMATICALLY FROM SOURCES.YAML (AND ELSEWHERE)\n# See https://github.com/greenelab/lab-website-template/wiki/Citations"
    try:
        with open(path, "r") as file:
            data = file.read()
        with open(path, "w") as file:
            file.write(f"{note}\n\n{data}")
    except Exception:
        raise Exception(f"Can't write to {filename}")


def cite_with_manubot(source):
    id = source.get("id")

    try:
        commands = ["manubot", "cite", id, "--log-level=WARNING"]
        output = subprocess.Popen(commands, stdout=subprocess.PIPE).communicate()
    except Exception as e:
        log(e, 3, "gray")
        raise Exception("Manubot could not generate citation")

    try:
        manubot = json.loads(output[0])[0]
    except Exception:
        raise Exception("Couldn't parse Manubot response")

    citation = {}


    citation["id"] = id

    citation["title"] = manubot.get("title", "")

    citation["authors"] = []
    for author in manubot.get("author", []):
        given = author.get("given", "")
        family = author.get("family", "")
        citation["authors"].append(given + " " + family)

    container = manubot.get("container-title", "")
    collection = manubot.get("collection-title", "")
    publisher = manubot.get("publisher", "")
    citation["publisher"] = container or publisher or collection

    year = date_part(manubot, 0)
    month = date_part(manubot, 1)
    day = date_part(manubot, 2)
    citation["date"] = f"{year}-{month}-{day}"

    citation["link"] = manubot.get("URL", "")

    return citation

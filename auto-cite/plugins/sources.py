from util import *


def main(data):
    all_sources = []

    for entry in data:
        log(entry.get("id", "[no ID]"), 3, "white")

        all_sources.append(entry)

    return all_sources

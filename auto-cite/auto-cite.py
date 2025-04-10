from util import *
from importlib import import_module
from dict_hash import sha256

config = {}
try:
    config = load_data("../_config.yaml", type_check=False).get("auto-cite")
    if not config:
        raise Exception("Couldn't find auto-cite key in config")
except Exception as e:
    log(e, 3, "red")
    exit(1)

log("Compiling list of sources to cite")

sources = []

will_exit = False

for plugin in config.get("plugins", []):
    name = plugin.get("name", "[no name]")
    files = plugin.get("input", [])

    log(f"Running {name} plugin")

    for file in files:
        log(file, 2)

        plugin_sources = []
        try:
            data = load_data(file)
            plugin_sources = import_module(f"plugins.{name}").main(data)
        except Exception as e:
            log(e, 3, "red")
            will_exit = True

        log(f"Got {len(plugin_sources)} sources", 2, "green")

        for source in plugin_sources:
            source["_plugin"] = name
            source["_input"] = file
            source["_cache"] = sha256(source)
            sources.append(source)

if will_exit:
    log("One or more input files or plugins failed", 3, "red")
    exit(1)

log("Generating citations for sources")

citations = []
try:
    citations = load_data(config["output"])
except Exception as e:
    log(e, 2, "yellow")

will_exit = False

new_citations = []

for index, source in enumerate(sources):
    log(f"Source {index + 1} of {len(sources)} - {source.get('id', '[no ID]')}", 2)
    new_citation = {}
    cached = get_cached(source, citations)

    if cached:
        log("Using existing citation", 3)
        new_citation = cached

    elif source.get("id", "").strip():
        log("Using Manubot to generate new citation", 3)
        try:
            new_citation = cite_with_manubot(source)
        except Exception as e:
            log(e, 3, "red")
            if source.get("_plugin") == "sources":
                will_exit = True
            continue
    else:
        log("Passing source through", 3)

    new_citation.update(source)
    new_citation["date"] = clean_date(new_citation.get("date"))

    new_citation.pop("_plugin")
    new_citation.pop("_input")

    new_citations.append(new_citation)

if will_exit:
    log("One or more sources failed to be cited", 3, "red")
    exit(1)

log("Exporting citations")

try:
    save_data(config["output"], new_citations)
except Exception as e:
    log(e, 2, "red")
    exit(1)

log(f"Exported {len(new_citations)} citations", 2, "green")

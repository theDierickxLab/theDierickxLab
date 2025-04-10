import logging
from urllib.request import Request, urlopen
import json
from util import *


endpoint = "https://pub.orcid.org/v2.0/$ORCID/works"
headers = {"Accept": "application/json"}


def main(data):
    all_sources = []
    
    will_exit = False

    for index, entry in enumerate(data):
        log(
            f"ORCID {index + 1} of {len(data)} - {entry.get('orcid', '[no ORCID]')}",
            3,
            "cyan",
        )

        id = entry.get("orcid")
        if not id:
            log('No "orcid" key', 3, "red")
            will_exit = True
            continue

        try:
            url = endpoint.replace("$ORCID", id)
            request = Request(url=url, headers=headers)
            response = json.loads(urlopen(request).read())

        except Exception as e:
            log(e, 3, "red")
            will_exit = True
            continue

  
        works = response["group"]
        for work in works:
            for id in work["external-ids"]["external-id"]:
    
                id_type = id["external-id-type"]
                id_value = id["external-id-value"]

                source = {"id": f"{id_type}:{id_value}"}

                log(source.get("id", "[no ID]"), 3)


                source.update(entry)


                all_sources.append(source)


    if will_exit:
        log("One or more ORCIDs failed", 3, "red")
        exit(1)

    return all_sources

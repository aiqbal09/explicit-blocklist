import os
import requests
from pathlib import Path


API_KEY = os.environ["NEXTDNS_API_KEY"]
PROFILE_ID = os.environ["NEXTDNS_PROFILE_ID"]

LIST_FILE = Path("lists/all.txt")


def load_domains():

    domains = []

    for line in LIST_FILE.read_text().splitlines():

        line = line.strip()

        if line and not line.startswith("#"):
            domains.append(line)

    return domains


def get_existing():

    url = (
        f"https://api.nextdns.io/profiles/"
        f"{PROFILE_ID}/denylist"
    )

    response = requests.get(
        url,
        headers={
            "X-Api-Key": API_KEY
        }
    )

    response.raise_for_status()

    return response.json()


def add_domain(domain):

    url = (
        f"https://api.nextdns.io/profiles/"
        f"{PROFILE_ID}/denylist"
    )

    payload = {
        "domain": domain
    }

    r = requests.post(
        url,
        headers={
            "X-Api-Key": API_KEY
        },
        json=payload
    )

    if r.status_code not in [200, 201]:

        print(
            "Failed:",
            domain,
            r.text
        )

    else:

        print(
            "Added:",
            domain
        )


def main():

    domains = load_domains()

    existing = get_existing()

    current = {
        x["domain"]
        for x in existing.get(
            "data",
            []
        )
    }


    for domain in domains:

        if domain not in current:

            add_domain(domain)


if __name__ == "__main__":
    main()
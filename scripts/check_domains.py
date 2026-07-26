import asyncio
from pathlib import Path

import dns.resolver
import httpx


def load_domains():

    domains = set()

    for file in Path("lists").glob("*.txt"):

        for line in file.read_text().splitlines():

            line=line.strip()

            if line and not line.startswith("#"):
                domains.add(line)

    return sorted(domains)


def dns_check(domain):

    try:
        dns.resolver.resolve(domain)
        return True

    except Exception:
        return False


async def http_check(domain):

    try:

        async with httpx.AsyncClient(
            timeout=5
        ) as client:

            r = await client.get(
                f"https://{domain}",
                follow_redirects=True
            )

            return r.status_code

    except Exception:

        return None


async def main():

    domains = load_domains()

    dead=[]

    for domain in domains:

        dns_ok=dns_check(domain)

        status=await http_check(domain)

        print(
            domain,
            dns_ok,
            status
        )

        if not dns_ok and status is None:
            dead.append(domain)


    Path(
        "reports/dead-domains.md"
    ).write_text(
        "# Dead domains\n\n"
        +
        "\n".join(
            f"- {x}"
            for x in dead
        )
    )


asyncio.run(main())
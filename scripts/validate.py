from pathlib import Path
import re

DOMAIN = re.compile(
    r"^[a-z0-9][a-z0-9.-]+\.[a-z]{2,}$"
)

errors = []

for file in Path("lists").glob("*.txt"):

    seen = set()

    for number, line in enumerate(
        file.read_text().splitlines(),
        start=1
    ):

        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line in seen:
            errors.append(
                f"{file}:{number} duplicate {line}"
            )

        seen.add(line)

        if not DOMAIN.match(line):
            errors.append(
                f"{file}:{number} invalid {line}"
            )


if errors:
    print("\n".join(errors))
    exit(1)

print("All lists are valid")

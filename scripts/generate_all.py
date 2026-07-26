from pathlib import Path

LIST_DIR = Path("lists")
OUTPUT = LIST_DIR / "all.txt"

domains = set()

for file in LIST_DIR.glob("*.txt"):
    if file.name == "all.txt":
        continue

    for line in file.read_text().splitlines():
        line = line.strip()

        if line and not line.startswith("#"):
            domains.add(line.lower())


OUTPUT.write_text(
    "\n".join(sorted(domains)) + "\n",
    encoding="utf-8"
)

print(f"Generated {OUTPUT}")
print(f"Domains: {len(domains)}")
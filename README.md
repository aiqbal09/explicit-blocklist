# Explicit-blocklist

A community-maintained DNS blocklist collection for:

- NextDNS
- AdGuard Home
- Pi-hole
- uBlock Origin
- Other DNS/content filters

## Categories

- Manga
- Manhwa
- Manhua
- Web novels
- Light novels
- Fanfiction
- Anime
- Webtoons

## Usage

Each file contains one domain per line.

Example:

manganato.com  
mangafire.to  
goodnovel.com

## Generate combined list

Run:

```bash
python scripts/generate_all.py

```

This creates:

lists/all.txt

## Validate lists

Run:

```bash
python scripts/validate.py
```

Checks:

- invalid domains
    
- duplicates
    
- formatting issues
    

## Domain monitoring

GitHub Actions automatically checks domains weekly.

Failed domains are reported but not automatically removed.

## Philosophy

This project intentionally avoids automatic blocking decisions.

Domains are reviewed before removal because:

- sites may temporarily go offline
    
- domains may migrate
    
- mirrors may return


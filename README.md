# bohemik.cz – nový web (draft)

Statický web pro GitHub Pages. Publikuje se složka `docs/`.

## Struktura

- `docs/index.html` – hlavní stránka (vychází z návrhu 8)
- `docs/assets/` – písmo Clash Display, fotky, loga, ilustrace, styly a skripty
- `docs/templates/` – všechny návrhy designu (přehled + varianty 1–8). Na webu na ně nic neodkazuje a mají `noindex`.
- `stary-web.md` – obsah původního webu bohemik.cz (zdroj obsahu tam, kde podklady od Bohemiku nic neuvádějí)

Podklady od klienta (`documentsFromBohemik/`) jsou v `.gitignore` a do repozitáře se nenahrávají.

## Lokální náhled

```
python -m http.server 8123 --directory docs
```

a otevřít http://localhost:8123

## Nasazení na GitHub Pages

1. Vytvořit repozitář na GitHubu a nahrát do něj tuto složku.
2. Na GitHubu: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, větev `main`, složka `/docs`.
3. Web poběží na `https://<uživatel>.github.io/<repozitář>/`, návrhy na `…/templates/`.

## Před spuštěním na bohemik.cz

- Odstranit `<meta name="robots" content="noindex, nofollow">` z `docs/index.html`.
- Ověřit čísla 29 zakázek a 20 zaměstnanců. Roky na trhu se počítají samy od roku založení 2012 (`data-since` v `index.html`).
- Web3Forms: doplnit `access_key` ve formuláři a odebrat blokování odeslání ve skriptu.
- Stránka ochrany osobních údajů, detail referencí, kariéra.
- Logo a ilustrace jako SVG, fotky v plném rozlišení.
- Vlastní doména: soubor `docs/CNAME` a DNS záznamy.

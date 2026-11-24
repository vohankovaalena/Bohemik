# bohemik.cz – nový web (draft)

Statický web pro GitHub Pages. Publikuje se složka `docs/`.

## Struktura

- `docs/index.html` – hlavní stránka (základ z návrhu 7, ilustrované karty a reference z návrhu 5, prolínání fotek z návrhu 8)
- `docs/reference/`, `docs/kariera/`, `docs/kontakt/` – podstránky (adresy `/reference/`, `/kariera/`, `/kontakt/`)
- `docs/reference/<stavba>/` – detail každé reference
- `scripts/reference.py` – generátor stránky Reference a detailů referencí (viz níže)
- `docs/assets/` – písmo Clash Display, fotky, loga, ilustrace, styly a skripty; `site.css` jsou společné styly webu
- `docs/templates/` – všechny návrhy designu (přehled + varianty 1–8). Na webu na ně nic neodkazuje a mají `noindex`.
- `stary-web.md` – obsah původního webu bohemik.cz (zdroj obsahu tam, kde podklady od Bohemiku nic neuvádějí)

Podklady od klienta (`documentsFromBohemik/`) jsou v `.gitignore` a do repozitáře se nenahrávají.

## Lokální náhled

```
python3 -m http.server 8123 --directory docs
```

a otevřít http://localhost:8123

## Úprava referencí

Stránky v `docs/reference/` se needitují ručně. Data všech staveb (název, investor, období, popis, zakázky, fotky) jsou v `scripts/reference.py`. Po úpravě dat stránky znovu vygenerujte:

```
python3 scripts/reference.py
```

Fotky patří do `docs/assets/img/ref/` a zapisují se do pole `fotky` dané stavby. První fotka je náhled, při dvou a více fotkách se na detailu zobrazí galerie. Stavba bez fotky má zástupný obrázek s postavičkami.

## Nasazení na GitHub Pages

Repozitář: https://github.com/vohankovaalena/Bohemik

Web se nasazuje automaticky při každém pushi do `main` workflowem `.github/workflows/pages.yml`, který publikuje složku `docs/`. V nastavení repozitáře musí být **Settings → Pages → Source: GitHub Actions**.

- Web: https://vohankovaalena.github.io/Bohemik/
- Návrhy: https://vohankovaalena.github.io/Bohemik/templates/

## Před spuštěním na bohemik.cz

- Odstranit `<meta name="robots" content="noindex, nofollow">` z `docs/index.html`.
- Ověřit čísla 29 zakázek a 20 zaměstnanců. Roky na trhu se počítají samy od roku založení 2012 (`data-since` v `index.html`).
- Web3Forms: doplnit `access_key` ve formuláři v `docs/kontakt/index.html` a odebrat blokování odeslání ve skriptu.
- Stránka ochrany osobních údajů (odkazuje na ni i souhlas ve formuláři).
- Fotky referencí: Fotka Kolektorů Praha má jen 275 × 183 px (na detailu je rozmazaná), potřeba větší. Neznámý autor: Trubín (vypadá jako fotobanka, ověřit licenci), ZŠ Ležáků Hlinsko, ZŠ Komenského Slaný, Kolektory Praha. Fotky ČNB, Homolka a Planetárium jsou podle starého webu z Wikimedia Commons, ale konkrétní soubor a autora se nepodařilo dohledat. Zdroje fotek se zapisují do `FOTO` v `scripts/reference.py` a zobrazují se malým písmem dole na detailu zakázky.
- Ověřit popisek první fotky v hero („Naše zázemí v Dobříši“) a aktuálnost pozic a kontaktů na stránkách Kariéra a Kontakt.
- Logo a ilustrace jako SVG, fotky v plném rozlišení.
- Vlastní doména: soubor `docs/CNAME` a DNS záznamy.

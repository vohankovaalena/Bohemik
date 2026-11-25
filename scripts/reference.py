#!/usr/bin/env python3
"""Generátor stránek s referencemi.

Z dat v seznamu REFERENCE níže vytvoří:
  docs/reference/index.html         přehled všech staveb (dlaždice s fotkou)
  docs/reference/<slug>/index.html  detail každé stavby

Úprava referencí: upravte data níže a spusťte  python3 scripts/reference.py
Fotky patří do docs/assets/img/ref/. Stavba bez fotky dostane zástupný obrázek
s postavičkou. Další fotky do galerie se přidávají do seznamu "fotky".
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs"

# Druh zakázky: "vz" = generální dodávka veřejné zakázky, "tzb" = dodávka a montáž technologií.
# Rozdělení vychází ze starého webu („Stavební činnosti včetně technologií“ = vz,
# „D+M technologií“ = tzb) a musí ho potvrdit Bohemik.
DRUH = {
    "vz": ("Veřejné zakázky", "Generální dodávka: stavební práce včetně technologií"),
    "tzb": ("TZB", "TZB: dodávka a montáž technologií včetně stavebních přípomocí"),
}

# Seřazeno od nejnovější. Údaje pocházejí ze stránky Reference starého webu (stary-web.md).
REFERENCE = [
    dict(slug="trubin", nazev="Dětská skupina Trubín", investor="Obec Trubín", druh="vz",
         obdobi="05/2025-03/2026",
         perex="Nový objekt pro dětské skupiny včetně zpevněných ploch a parkování.",
         text="Pro obec Trubín jsme postavili nový objekt pro dětské skupiny. Součástí dodávky byly také zpevněné plochy a parkování.",
         zakazky=["Objekt pro dětské skupiny včetně zpevněných ploch a parkování"],
         fotky=["trubin.jpg"]),
    dict(slug="vinohrady", nazev="Nemocnice Královské Vinohrady", investor="Fakultní nemocnice Královské Vinohrady", druh="vz",
         obdobi="03/2025-03/2026",
         perex="Modernizace onkologického centra a stavební úpravy pracoviště CT a PET/CT.",
         text="Ve Fakultní nemocnici Královské Vinohrady jsme jako generální dodavatel modernizovali centrum vysoce specializované onkologické a hematoonkologické péče a stavebně upravili pracoviště CT a PET/CT v pavilonu H. Dodávka zahrnovala stavební práce včetně technologií.",
         zakazky=["Modernizace centra vysoce specializované onkologické a hematoonkologické péče",
                  "Stavební úpravy pracoviště CT a PET/CT v 1. NP pavilonu H"],
         fotky=["vinohrady.jpg"]),
    dict(slug="planetarium", nazev="Planetárium Praha", investor="Hvězdárna a planetárium hl. m. Prahy, p. o.", druh="tzb",
         obdobi="03/2025-12/2025",
         perex="Rekonstrukce vzduchotechniky, klimatizace, vytápění a měření a regulace.",
         text="V pražském planetáriu jsme zrekonstruovali vzduchotechniku, klimatizaci, ústřední vytápění a systém měření a regulace. Technologie jsme dodali a namontovali včetně stavebních přípomocí.",
         zakazky=["Rekonstrukce VZT, klimatizace, ÚT a MaR"],
         fotky=["planetarium.jpg"]),
    dict(slug="kolektory-praha", nazev="Kolektory Praha", investor="Hlavní město Praha", druh="vz",
         obdobi="05/2024-01/2026",
         perex="Opravy pražských kolektorů včetně vzduchotechniky a pochozích roštů.",
         text="Pro hlavní město Prahu jsme opravovali podzemní kolektory: OCK kolektoru MoKo B6 a B7, vzduchotechniku kolektoru Modřany K2 a pochozí rošty v kolektorech Žižkov, KC1A, Panská a Milošova chodba.",
         zakazky=["Oprava OCK kolektoru MoKo B6, B7",
                  "Oprava systému vzduchotechniky kolektoru Modřany K2, PÚ 7, 8 a 9",
                  "Oprava pochozích roštů v kolektorech Žižkov, KC1A, Panská a Milošova chodba"],
         fotky=["kolektory-praha.jpg"]),
    dict(slug="ikem", nazev="IKEM", investor="Institut klinické a experimentální medicíny", druh="vz",
         obdobi="04/2024-07/2025",
         perex="Stavební úpravy objektů D a G a výměna VZT jednotky operačního sálu.",
         text="V Institutu klinické a experimentální medicíny jsme provedli stavební úpravy v objektech D a G a vyměnili vzduchotechnickou jednotku operačního sálu 4.",
         zakazky=["Stavební úpravy v objektech D a G", "Výměna VZT jednotky operačního sálu 4"],
         fotky=["ikem.jpg"]),
    dict(slug="letiste-praha", nazev="Letiště Praha, Hangár F", investor="Czech Airlines Technics, a.s.", druh="vz",
         obdobi="06/2024-12/2024",
         perex="Stavební úpravy pro lakovací kabinu v Hangáru F.",
         text="Pro Czech Airlines Technics jsme na Letišti Praha připravili Hangár F pro lakovací kabinu. Stavební úpravy zahrnovaly i technologie.",
         zakazky=["Úpravy pro lakovací kabinu v Hangáru F"],
         fotky=["letiste-praha.jpg"]),
    dict(slug="ntm", nazev="Národní technické muzeum", investor="Národní technické muzeum", druh="tzb",
         obdobi="05/2024-11/2024",
         perex="Doplnění chlazení do 2. a 3. patra budovy muzea.",
         text="V budově Národního technického muzea v Praze jsme doplnili chlazení do 2. a 3. patra. Technologie jsme dodali a namontovali včetně stavebních přípomocí.",
         zakazky=["Doplnění chlazení do 2. a 3. patra v budově NTM"],
         fotky=["ntm.jpg"]),
    dict(slug="zs-komenskeho-slany", nazev="ZŠ Komenského Slaný", investor="Město Slaný", druh="vz",
         obdobi="09/2023-03/2025",
         perex="Půdní vestavba základní školy.",
         text="Pro město Slaný jsme vestavěli nové prostory do podkroví základní školy Komenského.",
         zakazky=["Půdní vestavba ZŠ Komenského"],
         fotky=["zs-komenskeho-slany.jpg"]),
    dict(slug="thomayerova-g1", nazev="Thomayerova nemocnice, pavilon G1", investor="Fakultní Thomayerova nemocnice", druh="tzb",
         zhotovitel="subdodávka pro generálního dodavatele AVERS, spol. s r.o.",
         obdobi="07/2023-12/2024",
         perex="Vzduchotechnika a chlazení při energeticky úsporné renovaci pavilonu.",
         text="V rámci energeticky úsporné renovace pavilonu G1 jsme pro generálního dodavatele AVERS dodali a namontovali vzduchotechniku a chlazení celého objektu.",
         zakazky=["Dodávka a montáž VZT zařízení a chlazení objektu G1"],
         fotky=["thomayerova.jpg"]),
    dict(slug="rakovnik", nazev="Nemocnice Rakovník", investor="Masarykova nemocnice Rakovník", druh="vz",
         obdobi="12/2022-11/2023",
         perex="Rekonstrukce akutní péče.",
         text="V Masarykově nemocnici Rakovník jsme jako generální dodavatel zrekonstruovali prostory akutní péče včetně technologií.",
         zakazky=["Rekonstrukce akutní péče Masarykovy nemocnice Rakovník"],
         fotky=["rakovnik.jpg"]),
    dict(slug="bazen-kralupy", nazev="Bazén Kralupy nad Vltavou", investor="Město Kralupy nad Vltavou", druh="vz",
         obdobi="07/2022-02/2023",
         perex="Třetí etapa rekonstrukce plaveckého bazénu.",
         text="Pro město Kralupy nad Vltavou jsme realizovali třetí etapu rekonstrukce plaveckého bazénu včetně technologií.",
         zakazky=["Rekonstrukce objektu plaveckého bazénu, III. etapa"],
         fotky=["bazen-kralupy.jpg"]),
    dict(slug="zimni-stadion-slany", nazev="Zimní stadion Slaný", investor="Město Slaný", druh="vz",
         zhotovitel="subdodávka pro generálního dodavatele Tost s.r.o.",
         obdobi="06/2022-12/2022",
         perex="Výměna střešního pláště zimního stadionu včetně zateplení.",
         text="Při rekonstrukci střechy zimního stadionu ve Slaném jsme jako subdodavatel generálního dodavatele Tost vyměnili střešní plášť včetně zateplení.",
         zakazky=["Zimní stadion Slaný: výměna střešního pláště včetně zateplení"],
         fotky=["zimni-stadion-slany.jpg"]),
    dict(slug="thomayerova-g3", nazev="Thomayerova nemocnice, pavilon G3", investor="Fakultní Thomayerova nemocnice", druh="vz",
         obdobi="02/2022-09/2022",
         perex="Rekonstrukce vzduchotechniky operačních sálů.",
         text="V pavilonu G3 Fakultní Thomayerovy nemocnice jsme zrekonstruovali vzduchotechniku operačních sálů včetně souvisejících stavebních prací.",
         zakazky=["Pavilon G3: rekonstrukce VZT operačních sálů"],
         fotky=["thomayerova.jpg"]),
    dict(slug="homolka", nazev="Nemocnice Na Homolce", investor="Fakultní nemocnice Motol a Homolka (dříve Nemocnice Na Homolce)", druh="vz",
         obdobi="od 10/2021",
         perex="Šest zakázek: přestavby pracovišť, PET, stravovací provoz i chlazení.",
         text="S Nemocnicí Na Homolce spolupracujeme od roku 2021. Jako generální dodavatel jsme zde přestavěli a rozšířili řadu pracovišť včetně technologií, od lůžkové chirurgie a dialyzačního střediska po pracoviště PET a stravovací provoz.",
         zakazky=["Přístavba a přestavba objektu 080 PET",
                  "Rekonstrukce stravovacího provozu",
                  "Přestavba a rozšíření lůžkových kapacit na oddělení chirurgie",
                  "Dialyzační středisko a rozšíření kapacity skladu SZM",
                  "Rekonstrukce chlazení OKBHI",
                  "Přestavba gastroenterologické ambulance II"],
         fotky=["homolka.jpg"]),
    dict(slug="bazen-slany", nazev="Bazén Slaný", investor="Víceúčelová sportovní hala Slaný, spol. s r.o.", druh="vz",
         obdobi="11/2021-05/2022",
         perex="Energeticky úsporná opatření při rekonstrukci plaveckého areálu.",
         text="V rámci rekonstrukce plaveckého areálu ve Slaném jsme realizovali energeticky úsporná opatření včetně technologií.",
         zakazky=["Energeticky úsporná opatření v rámci akce „Rekonstrukce plaveckého areálu Slaný“"],
         fotky=["bazen-slany.jpg"]),
    dict(slug="cnb", nazev="Česká národní banka", investor="Česká národní banka", druh="vz",
         obdobi="od 09/2020",
         perex="Dochlazení budovy ústředí, výměna vzduchotechniky a bezbariérový vstup.",
         text="Česká národní banka je naším partnerem od roku 2020. Pro budovu ústředí jsme zpracovali projektovou dokumentaci dochlazení a dochlazení jsme také realizovali. Vyměnili jsme patrové vzduchotechniky a vybudovali bezbariérový vstup v ulici Na Příkopě.",
         zakazky=["Projektová dokumentace „Dochlazení budovy ústředí ČNB“",
                  "Dochlazení budovy ústředí ČNB",
                  "Výměna patrových vzduchotechnik",
                  "Bezbariérový vstup Na Příkopě 28"],
         fotky=["cnb.jpg"]),
    dict(slug="zs-lezaku-hlinsko", nazev="ZŠ Ležáků Hlinsko", investor="Město Hlinsko", druh="tzb",
         obdobi="07/2020-08/2020",
         perex="Vzduchotechnika školní kuchyně.",
         text="Pro základní školu Ležáků v Hlinsku jsme dodali a namontovali vzduchotechniku školní kuchyně včetně stavebních přípomocí.",
         zakazky=["Vzduchotechnika do kuchyně ZŠ Ležáků"],
         fotky=["zs-lezaku-hlinsko.jpg"]),
]

# Zdroje fotek: uvádějí se malým písmem pod fotkou na detailu a na konci přehledu.
# U fotek z Wikimedia Commons licence vyžadují autora, licenci a odkaz.
COMMONS = "Wikimedia Commons"
FOTO = {
    "ikem.jpg": dict(autor="VitVit", licence="CC BY-SA 4.0", licence_url="https://creativecommons.org/licenses/by-sa/4.0/deed.cs",
                     zdroj=COMMONS, url="https://commons.wikimedia.org/wiki/File:IKEM_budova.JPG"),
    "thomayerova.jpg": dict(autor="VitVit", licence="CC BY-SA 4.0", licence_url="https://creativecommons.org/licenses/by-sa/4.0/deed.cs",
                            zdroj=COMMONS, url="https://commons.wikimedia.org/wiki/File:Kr%C4%8D_Thomayerova_nemocnice_hl._budova_2.jpg"),
    "letiste-praha.jpg": dict(autor="ŠJů", licence="CC BY-SA 3.0", licence_url="https://creativecommons.org/licenses/by-sa/3.0/deed.cs",
                              zdroj=COMMONS, url="https://commons.wikimedia.org/wiki/File:Leti%C5%A1t%C4%9B_Ruzyn%C4%9B,_termin%C3%A1l_1.jpg"),
    "ntm.jpg": dict(autor="Toklick", licence="CC BY-SA 4.0", licence_url="https://creativecommons.org/licenses/by-sa/4.0/deed.cs",
                    zdroj=COMMONS, url="https://commons.wikimedia.org/wiki/File:Budova_N%C3%A1rodn%C3%ADho_technick%C3%A9ho_muzea_na_Letn%C3%A9.jpg"),
    # Podle starého webu z Wikimedia Commons, konkrétní soubor a autora se nepodařilo dohledat (ověřit u Bohemiku).
    "cnb.jpg": dict(zdroj=COMMONS),
    "homolka.jpg": dict(zdroj=COMMONS),
    "planetarium.jpg": dict(zdroj=COMMONS),
    # Autor zatím neznámý: trubin.jpg, zs-lezaku-hlinsko.jpg, zs-komenskeho-slany.jpg, kolektory-praha.jpg
    "rakovnik.jpg": dict(autor="Masarykova nemocnice Rakovník"),
    "vinohrady.jpg": dict(autor="NANOPROGRESS, z.s."),
    "zimni-stadion-slany.jpg": dict(autor="Víceúčelová sportovní hala Slaný, spol. s r.o."),
    "bazen-slany.jpg": dict(autor="Víceúčelová sportovní hala Slaný, spol. s r.o."),
}


def zdroj_fotky(soubor):
    """Popisek zdroje fotky, např. 'VitVit, CC BY-SA 4.0, Wikimedia Commons' (s odkazy)."""
    f = FOTO.get(soubor)
    if not f:
        return ""
    casti = []
    if f.get("autor"):
        casti.append(e(f["autor"]))
    if f.get("licence"):
        casti.append(f'<a href="{f["licence_url"]}">{e(f["licence"])}</a>')
    if f.get("zdroj"):
        casti.append(f'<a href="{f["url"]}">{e(f["zdroj"])}</a>' if f.get("url") else e(f["zdroj"]))
    return ", ".join(casti)


ILU = ["sanony", "kalkulacka", "helma", "cihly", "trubky", "kabel", "naradi", "vzt", "boss"]
# Zástupné postavičky pro stavby bez fotky, každá stavba dostane jinou dvojici
ZASTUPCE = {"vz": [["cihly", "helma"], ["naradi", "sanony"], ["kalkulacka", "boss"], ["helma", "cihly"],
                   ["sanony", "naradi"], ["boss", "kalkulacka"]],
            "tzb": [["trubky", "vzt"], ["kabel", "trubky"], ["vzt", "kabel"]]}


def postavicky(ref):
    """Dvojice postaviček pro stavbu bez fotky (střídá se podle pořadí stavby)."""
    bez_fotky = [x["slug"] for x in REFERENCE if not x["fotky"] and x["druh"] == ref["druh"]]
    sada = ZASTUPCE[ref["druh"]]
    return sada[bez_fotky.index(ref["slug"]) % len(sada)]

PLURAL = lambda n, a, b, c: a if n == 1 else b if 1 < n < 5 else c


def roky(obdobi):
    """'05/2025-03/2026' -> '2025-2026', '06/2024-12/2024' -> '2024', 'od 10/2021' -> 'od 2021'."""
    if obdobi.startswith("od "):
        return "od " + obdobi[-4:]
    od, do = [x.strip()[-4:] for x in obdobi.split("-")]
    return od if od == do else f"{od}-{do}"


def e(s):
    return escape(s, quote=True)


def header(r):
    return f"""<header class="header"><div class="wrap">
  <a class="logo" href="{r}">bohemik.</a>
  <button class="nav-toggle" aria-expanded="false" aria-label="Menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
  <nav class="nav" data-nav>
    <a href="{r}#o-nas">o nás</a>
    <a href="{r}reference/" aria-current="page">reference</a>
    <a href="{r}kariera/">kariéra</a>
    <a href="{r}kontakt/">kontakt</a>
    <a class="ig" href="https://www.instagram.com/bohemik.cz/" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
    <a class="btn btn--dark" href="{r}kontakt/#poptavka">Poptat zakázku</a>
  </nav>
</div></header>"""


def footer(r):
    parade = "".join(f'<img class="ilu-hop" src="{r}assets/img/ilu/{i}.png" alt="">' for i in ILU)
    return f"""<div class="parade" aria-hidden="true">
  {parade}
</div>
<footer class="footer"><div class="wrap">
  <div class="footer__grid">
    <div><a class="logo" href="{r}">bohemik.</a><p>Česká stavební firma z Dobříše. Generální dodávky veřejných zakázek a TZB.</p></div>
    <div><h4>Kancelář</h4>Pražská 636<br>263 01 Dobříš<br><a href="tel:+420326722707">+420 326 722 707</a><br><a href="mailto:info@bohemik.cz">info@bohemik.cz</a></div>
    <div><h4>Web</h4><a href="{r}#o-nas">o nás</a><br><a href="{r}reference/">reference</a><br><a href="{r}kariera/">kariéra</a><br><a href="{r}kontakt/">kontakt</a></div>
    <div><h4>Sledujte nás</h4><a href="https://www.instagram.com/bohemik.cz/">Instagram ↗</a><br><a href="https://www.facebook.com/Bohemikcz">Facebook ↗</a><br><a href="https://www.linkedin.com/company/bohemik">LinkedIn ↗</a></div>
  </div>
  <div class="footer__legal"><span>Bohemik s.r.o. · IČ 24265021 · DIČ CZ24265021</span><a href="#">Ochrana osobních údajů</a></div>
</div></footer>

<script src="{r}assets/site.js?v=2026-11-25-1"></script>"""


def page(r, title, desc, body, script=""):
    return f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="{r}assets/base.css?v=2026-11-25-1">
<link rel="stylesheet" href="{r}assets/site.css?v=2026-11-25-1">
</head>
<body>
<!-- Vygenerováno skriptem scripts/reference.py, neupravujte ručně, změny dělejte v datech skriptu. -->

{header(r)}

{body}

{footer(r)}
{script}</body>
</html>
"""


def nahled(ref, r):
    """Obrázek dlaždice: fotka, nebo zástupné postavičky."""
    stitek = f'<span class="sticker">{DRUH[ref["druh"]][0]}</span>'
    if ref["fotky"]:
        return f'<div class="ref__img"><img src="{r}assets/img/ref/{ref["fotky"][0]}" alt="" loading="lazy">{stitek}</div>'
    ilu = "".join(f'<img src="{r}assets/img/ilu/{i}.png" alt="">' for i in postavicky(ref))
    return f'<div class="ref__img ref__img--ph">{ilu}{stitek}</div>'


def dlazdice(ref, r, odkaz):
    return f"""    <a class="ref ref--card" href="{odkaz}" data-c="{ref['druh']}">
      {nahled(ref, r)}
      <h3>{e(ref['nazev'])}</h3>
      <span class="ref__when">{roky(ref['obdobi'])}</span>
      <p class="ref__perex">{e(ref['perex'])}</p>
      <span class="ref__go" aria-hidden="true">→</span>
    </a>"""


def prehled():
    r = "../"
    karty = "\n".join(dlazdice(x, r, f"{x['slug']}/") for x in REFERENCE)
    body = f"""<section class="page-head"><div class="wrap">
  <div>
    <span class="eyebrow">Reference</span>
    <h1 class="h1">Stavíme pro nemocnice, banky <em>i&nbsp;města.</em></h1>
    <p class="lead">Vše na jednom místě: realizujeme generální dodávky, máme vlastní divizi TZB, zajišťujeme servis VZT.</p>
  </div>
  <div class="page-head__ilu" aria-hidden="true"><img class="ilu-hop" src="{r}assets/img/ilu/cihly.png" alt=""><img class="ilu-hop" src="{r}assets/img/ilu/trubky.png" alt=""><img class="ilu-hop" src="{r}assets/img/ilu/kabel.png" alt=""></div>
</div></section>

<section class="section" style="padding-top:30px"><div class="wrap">
  <div class="refs__head">
    <h2 class="h2">reference:</h2>
    <div class="tabs" role="group" aria-label="Filtr referencí">
      <button aria-pressed="true" data-f="vse">Vše</button><button aria-pressed="false" data-f="vz">Veřejné zakázky</button><button aria-pressed="false" data-f="tzb">TZB</button>
    </div>
  </div>
  <div class="refs refs--cards">
{karty}
  </div>
</div></section>

<section class="section cta" style="padding-top:0"><div class="wrap">
  <h2 class="h2">Hledáte referenci na konkrétní typ stavby?</h2>
  <p>Rádi vám pošleme podrobnosti nebo kontakt na investora.</p>
  <div class="cta__btns"><a class="btn btn--dark" href="{r}kontakt/#poptavka">Zeptejte se nás →</a></div>
</div></section>"""
    script = """<script>
  // Filtr dlaždic podle druhu zakázky
  (() => {
    const btns = document.querySelectorAll(".tabs button");
    const cards = document.querySelectorAll(".refs .ref");
    const filter = (f) => {
      btns.forEach((x) => x.setAttribute("aria-pressed", String(x.dataset.f === f)));
      cards.forEach((c) => { c.hidden = f !== "vse" && c.dataset.c !== f; });
    };
    btns.forEach((b) => b.addEventListener("click", () => filter(b.dataset.f)));
    // Odkaz reference/#vz nebo reference/#tzb (karty služeb na hlavní stránce) rovnou nastaví filtr
    const f = location.hash.slice(1);
    if (f === "vz" || f === "tzb") filter(f);
  })();
</script>
"""
    html = page(r, "Reference | bohemik.",
                "Referenční stavby Bohemik od roku 2020: generální dodávky veřejných zakázek a zakázky TZB pro nemocnice, banky a města.",
                body, script)
    (ROOT / "reference" / "index.html").write_text(html, encoding="utf-8")


def detail(i, ref):
    r = "../../"
    druh_stitek, druh_popis = DRUH[ref["druh"]]
    if ref["fotky"]:
        f = f'{r}assets/img/ref/{ref["fotky"][0]}'
        foto = f"""<div class="detail__photo"><img class="detail__bg" src="{f}" alt=""><img class="detail__fg" src="{f}" alt="{e(ref['nazev'])}"><span class="sticker">{druh_stitek}</span></div>"""
    else:
        ilu = "".join(f'<img class="ilu-hop" src="{r}assets/img/ilu/{x}.png" alt="">' for x in postavicky(ref))
        foto = f"""<div class="detail__photo detail__photo--ph"><div class="detail__ilu" aria-hidden="true">{ilu}</div><p>Fotografie stavby připravujeme.</p><span class="sticker">{druh_stitek}</span></div>"""
    popisek = ""
    if ref["fotky"] and zdroj_fotky(ref["fotky"][0]):
        popisek = f'<p class="credits">Foto: {zdroj_fotky(ref["fotky"][0])}</p>'
    galerie = ""
    if len(ref["fotky"]) > 1:
        galerie = '<div class="detail__gallery">' + "".join(
            f'<a href="{r}assets/img/ref/{x}"><img src="{r}assets/img/ref/{x}" alt="" loading="lazy"></a>' for x in ref["fotky"]) + "</div>"
    zhotovitel = "Bohemik s.r.o."
    if ref.get("zhotovitel"):
        zhotovitel += f'<small>{e(ref["zhotovitel"])}</small>'
    nz = len(ref["zakazky"])
    zakazky = "".join(f"<li>{e(z)}</li>" for z in ref["zakazky"])
    fakta = [("Investor", e(ref["investor"])), ("Zhotovitel", zhotovitel), ("Druh zakázky", e(druh_popis)),
             ("Období realizace", e(ref["obdobi"]))]
    dl = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in fakta)
    dalsi = "\n".join(dlazdice(REFERENCE[(i + k) % len(REFERENCE)], r, f"../{REFERENCE[(i + k) % len(REFERENCE)]['slug']}/") for k in (1, 2, 3))
    body = f"""<section class="detail"><div class="wrap">
  <a class="detail__back link" href="../">← Všechny reference</a>
  {foto}
  {galerie}
  <div class="detail__body">
    <div>
      <h1 class="h2">{e(ref['nazev'])}</h1>
      <p class="detail__text">{e(ref['text'])}</p>
      <h2 class="detail__h">{nz} {PLURAL(nz, 'zakázka', 'zakázky', 'zakázek')}</h2>
      <ul class="detail__jobs">{zakazky}</ul>
    </div>
    <dl class="detail__facts">{dl}</dl>
  </div>
  {popisek}
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <div class="refs__head"><h2 class="h2">další reference:</h2><a class="btn btn--line" href="../">Všechny reference →</a></div>
  <div class="refs refs--cards">
{dalsi}
  </div>
</div></section>

<section class="section cta" style="padding-top:0"><div class="wrap">
  <h2 class="h2">Máte podobnou stavbu?</h2>
  <p>Pošlete nám odkaz na zadávací dokumentaci nebo popište záměr. Ozveme se co nejdříve.</p>
  <div class="cta__btns"><a class="btn btn--dark" href="{r}kontakt/#poptavka">Poptat zakázku →</a><a class="btn btn--line" href="tel:+420326722707">+420 326 722 707</a></div>
</div></section>"""
    out = ROOT / "reference" / ref["slug"]
    out.mkdir(parents=True, exist_ok=True)
    html = page(r, f"{ref['nazev']} | reference | bohemik.",
                f"{ref['nazev']}: {ref['perex']} Investor {ref['investor']}, {ref['obdobi']}.", body)
    (out / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    prehled()
    for i, ref in enumerate(REFERENCE):
        detail(i, ref)
    print(f"Hotovo: přehled a {len(REFERENCE)} detailů v {ROOT / 'reference'}")

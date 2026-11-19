# Původní web bohemik.cz – stažený obsah

Staženo 19. 11. 2026 z https://www.bohemik.cz (web běží na Wixu). Texty jsou převzaté doslova, včetně překlepů, aby šly dohledat. Postřehy a návrhy pro nový web jsou v první části.

> **Jak s obsahem zacházet:** podklady od Bohemiku (PDF a e-mail) mají přednost, pokud v nich je konkrétní údaj. Kde v podkladech nic není nebo je jen zástupný znak (xxx), použije se údaj z tohoto starého webu.

---

## 1. Co z toho plyne pro nový web

### Fakta, která můžeme použít
- **Zaměstnanci:** na úvodní stránce stojí „rozšiřující se základna vlastních zaměstnanců. Kterých jsou dvě desítky“. Zhruba **20 zaměstnanců**, číslo je potřeba potvrdit.
- **Reference:** 16 referencí, které dohromady obsahují 29 zakázek (viz kapitola 4). Číslo „30+ realizovaných zakázek“ z návrhu je tedy mírně nadsazené, pokud Bohemik nemá další zakázky mimo výpis.
- **Certifikace:** „Všechny naše činnosti jsou prováděny v souladu s normou ISO 9001. Společnost je dále certifikována dle ISO 14001.“ Pro zadavatele veřejných zakázek je to silný argument, na novém webu by měla být vidět. Je potřeba ověřit platnost certifikátů a získat jejich PDF nebo loga.
- **Regionální servis:** Praha, Beroun, Příbram, Rakovník, Plzeň, Mladá Boleslav, Liberec, Písek, České Budějovice (přes regionální partnery).
- **Sociální sítě:**
  - Facebook https://www.facebook.com/Bohemikcz
  - Instagram https://www.instagram.com/bohemik.cz/
  - LinkedIn https://www.linkedin.com/company/bohemik
- **Zázemí:** „vlastní moderní zázemí v malebném městě Dobříš“, „nově vybudované administrativní zázemí na Dobříši“.

### Posun zaměření
Starý web prezentuje Bohemik hlavně jako **vzduchařskou firmu** (VZT, klimatizace, průmysl a automotive, ocelové konstrukce, průmyslové kabiny, servis domácích klimatizací). Nové zadání od Aleny staví na třech pilířích: **generální dodávky veřejných zakázek, TZB, servis VZT**.

Je potřeba rozhodnout, co ze starého webu zůstane:
- **Průmysl, ocelové konstrukce a průmyslové kabiny:** v novém zadání nejsou. Zrušit, nebo zmínit v O nás?
- **Servis domácích klimatizací a článek o závadách:** nové zadání mluví jen o servisu VZT na vlastních zakázkách.
- **Blog:** je prakticky prázdný (viz kapitola 10).

### Nesrovnalosti a chyby na starém webu
- **Servis 24/7:** některé stránky slibují „24/7 servis“, jinde stojí jen „hotline“. Je potřeba ověřit, než se 24/7 dostane na nový web.
- **Úvodní stránka má `noindex`:** vyhledávače ji nemají indexovat. Nejspíš chyba v nastavení Wixu, která škodí SEO.
- **Špatný titulek:** stránka `/stavbyvedouci` má titulek „Nabídka práce | Elektrikář technik MaR“.
- **Staré pracovní pozice jsou pořád dostupné:** stránky `/kopie-kariera` a `/kopie-elektrikar-technika-mar` nejsou v menu, ale jsou v sitemapě. Obsahují staré pozice (elektrikář, projektant VZT, konstruktér).
- **GDPR:** text je z 25. 5. 2018 a nepokrývá kontaktní formulář, doby uchování ani cookies. Na novém webu bude potřeba nový.
- **Překlepy, pokud budeme texty přebírat:**
  - „dlohotrvající“
  - „PRŮYMSL“
  - „monžáž“
  - „snižovnání“
  - „ždy“
  - „Mladá Bolaslav“
  - „Česé Budějovice“
  - „lakovavcí“
  - „procoviště“
  - „zkušeního“
  - „aby naplnili očekávání“
  - „maximalizujezte“
  - „standart“
- **Kontaktní osoby:** jsou uvedené jen na některých stránkách. Martin Kulička (poptávky) a Matěj Rychlý (servis) jsou jen na stránce o závadách klimatizací. Je potřeba ověřit, kdo je aktuální.
- **Autorská práva u fotek:** u řady fotek referencí je uvedeno „Image Copyright: WikiMedia Commons“. Na novém webu musí být u takových fotek správně uvedený autor a licence, nebo je nahradit vlastními fotkami.

---

## 2. Struktura starého webu

**Hlavní menu:** Domů · Služby · Servis · Kdo jsme · Reference · Kariéra · Náš příběh (blog) · Kontakty

**Rychlé odkazy v patičce:** O nás · Volná pracovní místa · Reference · Servis klimatizace · Servis klimatizací pro firmy · Nejčastější závady klimatizací · Kontakty

**Patička na všech stránkách:**
> Projektujeme, dodáváme a servisujeme technologické celky. Kontaktujte nás s poptávkou, obraťte se na nás s radou nebo přijeďte na kávu a přesvědčte se o našich kvalitách.
>
> Bohemik s.r.o., Pražská 636, 263 01 Dobříš · IČ: 24265021, DIČ: CZ24265021 · info@bohemik.cz · +420 326 722 707 · ©Bohemik s.r.o. 2025

### Všechny stránky (podle sitemapy) a návrh přesměrování

GitHub Pages neumí přesměrování na serveru. Stará adresa se proto vyřeší přesměrovací stránkou (meta refresh + canonical) na novou.

| Stará URL | Titulek (SEO) | Návrh cíle na novém webu |
|---|---|---|
| `/` | Stavební práce, Vzduchotechnika a klimatizace \| Bohemik | `/` |
| `/kdo-jsme` | O firmě \| Bohemik s.r.o. \| Dobříš | `/o-nas/` |
| `/sluzby` | Služby \| Bohemik s.r.o. \| Dobříš | `/o-nas/` nebo `/` |
| `/servis-klimatizace` | Servis klimatizací a vzduchotechniky \| Bohemik | `/reference/servis/` nebo `/kontakt/` |
| `/servis-klimatizaci-firmy` | Servis klimatizací pro firmy \| Bohemik s.r.o. | totéž |
| `/ocelove-konstrukce` | Ocelové konstrukce \| Bohemik s.r.o. \| Dobříš | `/o-nas/` (pokud obor zůstane) |
| `/prumyslove-kabiny-a-vestavby` | Průmyslové kabiny a vestavby \| Bohemik s.r.o. \| Dobříš | `/o-nas/` (pokud obor zůstane) |
| `/reference` | Reference \| Bohemik – vzduchotechnika a klimatizace pro přední instituce | `/reference/` (stejná cesta) |
| `/nabidka-volnych-pracovnich-mist` | Nabídka práce \| Bohemik s.r.o. \| Dobříš | `/kariera/` |
| `/stavbyvedouci` | Nabídka práce \| Elektrikář technik MaR *(chybný titulek)* | `/kariera/stavbyvedouci/` |
| `/rozpoctar` | Nabídka práce \| Rozpočtář/ Přípravář zakázek | `/kariera/rozpoctar/` |
| `/instalater-topenar` | Nabídka práce \| Instalatér - topenář | `/kariera/instalater-topenar/` |
| `/kontakty` | Kontakty Bohemik s.r.o. \| Dobříš | `/kontakt/` |
| `/nejcastejsi-zavady-klimatizaci` | Nejčastější závady domácích klimatizací | `/` (pokud obsah zanikne) |
| `/bohemik-ochrana-osobnich-kontaktu` | Ochrana osobních údajů \| Bohemik s.r.o. \| Dobříš | `/ochrana-osobnich-udaju/` |
| `/blog`, `/post/…`, `/blog/categories/…` | blog | `/` |
| `/kopie-kariera`, `/kopie-elektrikar-technika-mar` | staré kopie (mimo menu) | `/kariera/` |

---

## 3. Úvodní stránka (`/`)

**SEO popis:** Bohemik – profesionální dodavatel TZB. Nabízíme projekt, montáž a servis vzduchotechniky a klimatizace pro občanské i průmyslové stavby. Kontaktujte nás.

**Slider:**
- SPOLEHLIVÝ DODAVATEL – Technické zařízení budov pro občanské i průmyslové stavby
- PROFESIONÁLNÍ SLUŽBA – Komplexní servis a správa TZB

**CO UMÍME – Naše řešení jsou z velké míry dodávky na klíč**
> Firma Bohemik je ryze českou firmou s transparentní strukturou, která staví na mnoholetých zkušenostech profesionálů z oblastí TZB. Specializujeme se na dodávky, montáž, servis vzduchotechniky a klimatizace a navazujících profesí. Od prvního dne založení klademe důraz na kvalitu provedených služeb a dodávaných technologií a ekonomickou výhodnost provozování. Odměnou nám je rozšiřující se portfolio zákazníků, kteří se k nám rádi vrací a rozšiřující se základna vlastních zaměstnanců. Kterých jsou dvě desítky a společně řídí naše zakázky.

**Jsme spolehlivou a moderní službou pro dodávky a servis technického zařízení budov.** Každým rokem sílíme a rosteme.

**Vybraní zákazníci:** obrázek s logy (`loga_reference.jpg`)

**NAŠE SLUŽBY**
- Vzduchotechnika a klimatizace
- Rozvody chladu a tepla
- Měření a regulace
- Záruční a pozáruční servis zařízení
- Klimatizované vestavby
- Zakrytování průmyslových technologií s odsáváním
- Průmyslové kabiny pro automatická zařízení i ruční pracoviště
- Ocelové konstrukce pod vzduchotechnické a klimatizační jednotky
- Pochozí obslužné konstrukce pod technologická zařízení

> Firma Bohemik je postavena na rodinných hodnotách a opravdových partnerstvích s našimi zákazníky.
>
> Firma Bohemik se orientuje na projekci dodávky a servis vzduchotechniky - klimatizace v oblasti občanských staveb a průmyslu převážně v oblasti automotive a strojírenství. Zařízení, která dodáváme, jsou vždy unikátní a s každým předávacím protokolem se prohlubují naše technické znalosti. Realizujeme rozsáhlé projekty větrání ve veřejných občanských stavbách, špičkových kancelářských komplexech i skladových halách. Všechny naše činnosti jsou prováděny v souladu s normou ISO 9001. Společnost je dále certifikována dle ISO 14001. Zakázky realizujeme převážně v Čechách. Servis klimatizací a vzduchotechniky realizujeme po celé ČR.

---

## 4. Reference (`/reference`)

**Nadpis:** Vybrané reference – Pracujeme tvrdě a jsme na to pyšní.

**Návrh kategorie** podle zadání (Generální dodávky veřejných zakázek / TZB / Servis): „Stavební činnosti včetně technologií“ = generální dodávka, „D+M technologií“ = TZB. Rozdělení musí potvrdit Bohemik.

| # | Reference | Investor | Zakázka / zakázky | Popis | Období | Návrh kategorie | Foto © |
|---|---|---|---|---|---|---|---|
| 1 | Základní škola Ležáků Hlinsko | Město Hlinsko | Vzduchotechnika do kuchyně ZŠ Ležáků | D+M technologií včetně stavebních přípomocí | 07–08/2020 | TZB | – |
| 2 | Česká národní banka | Česká národní banka | Výměna patrových vzduchotechnik; ČNB – Bezbariérový vstup Na Příkopě 28; Projektová dokumentace „Dochlazení budovy ústředí ČNB“; Dochlazení budovy ústředí ČNB | Stavební činnosti včetně technologií a projektová činnost | od 09/2020 do současnosti | Veřejné zakázky | WikiMedia Commons |
| 3 | Fakultní nemocnice Motol a Homolka | Fakultní nemocnice Motol a Homolka (v minulosti Nemocnice Na Homolce) | Přestavba gastroenterologické ambulance II; Přestavba a rozšíření lůžkových kapacit na oddělení chirurgie – DOKONČENÍ DÍLA; Dialyzační středisko a rozšíření kapacity skladu SZM; Rekonstrukce chlazení OKBHI v Nemocnici Na Homolce; Přístavba a přestavba objektu 080 PET; Rekonstrukce stravovacího provozu | Stavební činnosti včetně technologií | od 10/2021 do současnosti | Veřejné zakázky | WikiMedia Commons |
| 4 | Masarykova nemocnice Rakovník | Masarykova nemocnice Rakovník | Rekonstrukce akutní péče Masarykovy nemocnice Rakovník | Stavební činnosti včetně technologií | 12/2022 – 11/2023 | Veřejné zakázky | Masarykova nemocnice Rakovník |
| 5a | Fakultní Thomayerova nemocnice | Fakultní Thomayerova nemocnice | Pavilon G3 – operační sály – rekonstrukce VZT | Stavební činnosti včetně technologií | 02/2022 – 09/2022 | Veřejné zakázky | WikiMedia Commons |
| 5b | Fakultní Thomayerova nemocnice | Fakultní Thomayerova nemocnice, GD: AVERS, spol. s r.o. | FTN – realizace energeticky úsporné renovace pavilonu G1; dodávaná část: Dodávka a montáž VZT zařízení a chlazení objektu G1 | D+M technologií včetně stavebních přípomocí | 07/2023 – 12/2024 | TZB | WikiMedia Commons |
| 6 | Plavecký bazén v Kralupech | Město Kralupy nad Vltavou | Rekonstrukce objektu plaveckého bazénu Kralupy nad Vltavou – III. etapa | Stavební činnosti včetně technologií | 07/2022 – 02/2023 | Veřejné zakázky | – |
| 7 | Plavecký bazén ve Slaném | Víceúčelová sportovní hala Slaný spol. s r.o. | Energeticky úsporná opatření v rámci akce „Rekonstrukce plaveckého areálu Slaný“ | Stavební činnosti včetně technologií | 11/2021 – 05/2022 | Veřejné zakázky | Víceúčelová sportovní hala Slaný, spol. s r.o. |
| 8 | IKEM | Institut klinické a experimentální medicíny | Stavební úpravy v objektech D a G; Výměna VZT jednotky OS 4 | Stavební činnosti včetně technologií | 04/2024 – 07/2025 | Veřejné zakázky | WikiMedia Commons |
| 9 | Planetárium v Praze | Hvězdárna a planetárium hl. m. Prahy, p. o. | Rekonstrukce VZT, klimatizace, ÚT a MaR v planetáriu Praha | D+M technologií včetně stavebních přípomocí | 03/2025 – 12/2025 | TZB | WikiMedia Commons |
| 10 | Národní technické muzeum v Praze | Národní technické muzeum | Doplnění chlazení do 2. a 3. patra v budově NTM | D+M technologií včetně stavebních přípomocí | 05/2024 – 11/2024 | TZB | WikiMedia Commons |
| 11 | ZŠ Komenského Slaný | Město Slaný | Půdní vestavba 2. Za Slaný *(takto na webu)* | Stavební činnosti včetně technologií | 09/2023 – 03/2025 | Veřejné zakázky | – |
| 12 | Kolektory Praha | Hlavní město Praha | Oprava OCK kolektoru MoKo B6, B7; Oprava systému vzduchotechniky kolektoru Modřany K2 – PÚ 7, 8 a 9; Oprava pochozích roštů v kolektoru Žižkov, KC1A, Panská, Milošova Chodba | Stavební činnosti včetně technologií | 05/2024 – 01/2026 | Veřejné zakázky | – |
| 13 | Letiště Praha | Czech Airlines Technics, a.s. | Úpravy pro lakovací kabinu v Hangáru F | Stavební činnosti včetně technologií | 06/2024 – 12/2024 | Veřejné zakázky | WikiMedia Commons |
| 14 | Budova pro dětskou skupinku v Trubíně | Obec Trubín | Objekt pro dětské skupiny, vč. zpevněných ploch a parkování | Stavební činnosti včetně technologií | 05/2025 – 03/2026 | Veřejné zakázky | – |
| 15 | Nemocnice Královské Vinohrady | Fakultní nemocnice Královské Vinohrady | Modernizace centra vysoce specializované onkologické a hematoonkologické péče FNKV; Stavební úpravy pracoviště CT a PETCT v 1NP pavilonu H | Stavební činnosti včetně technologií | 03/2025 – 03/2026 | Veřejné zakázky | NANOPROGRESS, z.s. |
| 16 | Zimní stadion ve Slaném | Město Slaný, GD: Tost s.r.o. | Zimní stadion Slaný – rekonstrukce střechy; dodávaná část: Výměna střešního pláště včetně zateplení | Stavební činnosti včetně technologií | 06/2022 – 12/2022 | Veřejné zakázky (subdodávka) | Víceúčelová sportovní hala Slaný, spol. s r.o. |

**Další reference zmíněné na stránce Služby** (na stránce Reference chybí):
- **Kongresové centrum Praha:** „Největší kongresové centrum v České Republice.“ VZT a klimatizace pro občanské stavby.
- **Proseat, Mladá Boleslav:** projekce, dodávka a montáž vzduchotechniky (průmysl).
- **Ministerstvo průmyslu a obchodu, Na Františku, Praha 1:** servis klimatizací. Hodí se jako reference do kategorie **Servis**.

---

## 5. Kdo jsme (`/kdo-jsme`)

**SEO popis:** Seznamte se s firmou Bohemik – český dodavatel v oblasti TZB s mnohaletou zkušeností, certifikacemi ISO a rodinným přístupem.

**Spolehlivé služby s vysokou technickou kvalitou – BOHEMIK DOBŘÍŠ**
> Opíráme se o dobré renomé v oboru a to se odráží v dlohotrvající přízni našich zákazníků.

**KDO JSME – Bohemik je v první řadě technickou firmou nadšených odborníků.**
> Firma Bohemik se orientuje na dodávky vzduchotechniky a chlazení v oblasti průmyslu a občanských staveb.
>
> Zaměřujeme se dodávku a servis TZB systémů, projekci a montáž nových klimatizačních a vzduchotechnických celků i modernizaci stávajících zařízení. Tvoříme tým s mezioborovým přesahem a naši práci děláme poctivě a tak, abychom se pod svými realizacemi nestyděli podepsat.
>
> Firma Bohemik disponuje vlastním moderním zázemím v malebném městě Dobříš, které je více než jen sídlo společnosti. Je to místo, kde vznikají vize a rádi tam trávíme čas.
>
> Systém kvality: Všechny naše činnosti jsou prováděny v souladu s normou ISO 9001. Společnost je dále certifikována dle ISO 14001.

**NAŠE VIZE – Našim motem je odbornost, zkušenost a inovace.**
> Opíráme se o dobré renomé v oboru. Dodáváme spolehlivou službu, která má za sebou znalosti a dovednosti našich odborníků, kteří svoji práci vykonávají s nadšením. Opíráme se o dobré renomé v oboru, které je založeno na skutečných partnerstvích a důvěře mezi jednotlivými talenty našeho týmu a neméně úspěšnými zákazníky, pro které přinášíme neprůstřelná technická řešení i hodnotné finanční úspory.
>
> Ať už se jedná o průmyslovou vzduchotechniku nebo vzduchotechniku pro občanské stavby, jsou naše realizace takové, aby naplnili očekávání.

**DOBRÁ PRÁCE – Přátelská politika ve firmě** *(stejný blok je i na stránkách pracovních pozic)*
> Věříme, že je Bohemik firmou, o které se dobře mluví a kde se zaměstnanci cítí dobře.
>
> Zaujali Vás naše hodnoty? Nabídka pracovních míst je stále otevřená.
>
> Víme, že jsou naši zaměstnanci pro nás důležití, proto se neustále snažíme vyjít vstříc jednotlivým individualitám a zajišťujeme dobrou rovnováhu mezi prací a soukromým životem. Naše filozofie se proto opírá o různé potřeby jednotlivců například v podobě flexibilní pracovní doby. Tvoříme společně tým, kde má každý své zasloužené místo.
>
> Pracovní prostředí stavíme tak, abychom se do práce vraceli s radostí. Přinášíme kreativitu tam, kde hrají první ligu čísla, fyzikální zákony a moderní technologie.

---

## 6. Služby (`/sluzby`)

**SEO popis:** Bohemik Dobříš - Kvalitní dodavatel vzduchotechniky a klimatizace pro rozsáhle technologické celky. Zajistíme projekci dodávku a servis.

### DODÁVKY A INSTALACE TZB – Vzduchotechnika a klimatizace pro občanské stavby
> Spolehlivý dodavatel TZB, obchodní partner i služba o kterou se naši zákazníci mohou spolehlivě opřít.
>
> Dodáváme čerstvý vzduch do míst jako jsou kancelářské budovy, nákupní centra, knihovny a nemocnice. Nabízíme komplexní řešení pro vnitřní klima od počáteční projektové dokumentace až po implementaci do řídícího systému, zprovoznění a následný servis zařízení. Pro zajištění maximálního komfortu větrání dodáváme optimalizovaný mix výrobků s těmi nejvyššími standardy účinnosti a dle hygienických norem s ohledem na ekonomiku provozu a snižovnání energetických nároků.

Vzduchotechnika · Klimatizace · Administrativní budovy · Objekty veřejné správy · Strojovny vzduchotechniky a chlazení · Odsávání z gastro provozů · Filtrace · Vlhčení vzduchu · Filtrace aktivním uhlím · RTCH / Rozvody tepla a chladu · M+R / Měření a regulace · Servis TZB

*Vybraná reference: Kongresové centrum Praha.*

### PRŮMYSLOVÉ VĚTRÁNÍ – Vzduchotechnika a chlazení pro průmysl
> Bohemik jsou více než jen odborníci na průmyslové větrání. Požádejte naše portfolio dodávek ocelových konstrukcí a průmyslových kabin a vestavků.
>
> Větráme montážní i skladovací haly, Dodáváme vzduchotechniku a chlazení pro výrobní linky i rozsáhlé lakovny, kde dodržujeme celoročně striktní vzduchové parametry, které jsou nezbytné pro kvalitní sériovou výrobu. Odsáváme ze složitých průmyslových technologií. Zabýváme se filtrací nežádoucích látek. Dodáváme komplexní řešení na klíč od koncepčního řešení, projektovou dokumentaci, realizaci zakázky, zaregulování požadovaných parametrů až po zprovoznění a předání zařízení u zákazníka.

Průmyslová vzduchotechnika · Průmyslové chlazení · Vytápění průmyslových hal · Zvlhčování · Odsávání od průmyslových technologií · Filtrace aktivním uhlím · RTCH / Rozvody tepla a chladu · M+R / Měření a regulace · Servis vzduchotechniky a chlazení

*Vybraná reference průmysl: Proseat, Mladá Boleslav – projekce, dodávka a montáž vzduchotechniky.*

### GENERÁLNÍ DODÁVKY – Naše plná odpovědnost
> Bohemik přebírá plnou odpovědnost za realizaci stavební zakázky od A do Z.
>
> Jako generální dodavatel koordinujeme veškeré subdodavatele, řídíme harmonogram a zajišťujeme kvalitu každé fáze projektu — od přípravy projektové dokumentace přes stavební práce až po předání hotového díla investorovi. Naši zákazníci tak komunikují s jediným partnerem a mají jistotu, že projekt bude dokončen včas, v rozpočtu a bez kompromisů v kvalitě.

Koordinace subdodavatelů · Stavební a technologické práce · Projektová dokumentace · Technický dozor a řízení harmonogramu · Předání díla a dokumentace skutečného provedení · Záruční i pozáruční servis

> Tenhle text se hodí jako základ pro pilíř „Veřejné zakázky / generální dodávky“ na novém webu.

### SERVIS – Servis pro systémy větrání a klimatizace
> Firma Bohemik disponuje samostatným střediskem pro servis klimatizace a vzduchotechniky. Alespoň jeden z našich zaměstnanců je vám vždy k dispozici. Sami si vyberte způsob jak nás kontaktovat s poptávkou na záruční i pozáruční servis.
>
> Potřebujete spolehlivého dodavatele servisu pro klimatizace a vzduchotechniku? Volejte naší hotline: **SERVIS HOTLINE +420 725 309 691**

*Vybraná reference servis: Servis klimatizací v objektu Ministerstva průmyslu a obchodu, Na Františku, Praha 1.*

---

## 7. Servis

### Servis klimatizace (`/servis-klimatizace`)
**Servis klimatizací pro firmy a instituce – SERVISNÍ SLUŽBY PRO FIRMY**
- Profylaxe klimatizačních zařízení
- Záruční i pozáruční servis
- Servis VRV a VRF systémů
- Servis vzduchotechniky
- Revize požárních klapek
- Měření a regulace

**Servis klimatizace pro domácnosti – SERVISNÍ SLUŽBY PRO DOMÁCNOSTI**
- Vizuální kontrola klimatizace
- Funkční zkouška dle předpisů
- Vytvoření protokolu údržby
- Čištění součástí a výměna filtrů
- Odstranění zjištěných závad

**VŽDY PO RUCE – Servis klimatizace a vzduchotechniky ve vašem místě**
> Servisní středisko Bohemik je vždy po ruce. Praha, Beroun, Příbram, Rakovník, Plzeň, Mladá Boleslav, Liberec, Písek, České Budějovice,…
>
> Ať už jste ze středočeského kraje, nebo z jiného cípu České republiky jsou naši regionální partneři vždy v pozoru. Slouží jako operační střediska pro dodání rychlé a spolehlivé služby, zkracujeme našim zákazníkům čas nutný k dojezdu a garantujeme cenu za servisní výjezd. Servisní tým Bohemik naplánuje nejkratší cestu k vašemu zařízení a pošle ty nejlepší servisní techniky.

**NEZAPOMÍNEJTE NA ÚDRŽBU – Proč a kdy je správný čas na servis klimatizace?**
> Pravidelně servisovat auto bereme jako samozřejmost, stejný přístup k servisu se doporučuje pro váš systém větrání a klimatizace. Pravidelné kontroly odborníkem prodlužují životnost zařízení a správná výměna a čištění filtrů jsou podstatné minimum toho co bychom měli dělat pro své zdraví. Rádi Vám doporučíme četnost servisních prohlídek a zajistíme tak bezproblémový chod klimatizace.

### Servis klimatizací pro firmy (`/servis-klimatizaci-firmy`)
**Zajišťujeme firmám údržbu a servis ventilačních systémů po celé ČR**
> Servisní středisko Bohemik jsme postavili tak aby bylo spolehlivým partnerem pro firmy a jejich potřeby. Na rychlost a kvalitu služby se rychle zvyká. Vyzkoušejte si službu budoucnosti i vy a staňte se naším firemním zákazníkem.
>
> Přidejte se k inovátorům v oblasti správy a servisu klimatizačních systému a pozvedněte laťku na vyšší úroveň. Minimalizujete tak poruchovost a a maximalizujezte životnost zařízení. Ať už jste malá nebo velké firma stejný standart servisu klimatizací nabízíme všem.

**Servis klimatizací a chlazení pro veřejný i soukromý sektor**
> Provádíme záruční i pozáruční servis klimatizací a chladících systémů. Díky letitým zkušenostem našich servisních techniků a množství servisovaných zařízení, jsme schopni velmi rychle reagovat na servisní požadavek a odstranění závad pro většinu klimatizačních zařízení dostupných na českém trhu.

Mezititulky: „Ať už jste malá nebo velká firma, nabízíme stejný standard servisu všem.“ · „Buďte odvážní a nechte starosti s technickým zařízení budovy na nás.“ · **24/7 servis pro systémy větrání a klimatizace**, SERVIS HOTLINE +420 725 309 691. Stránka obsahuje kontaktní formulář.

### Nejčastější závady domácích klimatizací (`/nejcastejsi-zavady-klimatizaci`, totéž jako blogový článek z 16. 12. 2020)
- **Klimatizace nefouká a máme pocit, že dostatečně nechladí:** nejčastěji znečištěný filtr; doporučení nechat jednotku vyčistit.
- **Vytékající voda z vnitřní jednotky:** ucpaný odtok kondenzátu, v horším případě výměna čerpadla kondenzátu.
- **Únik vody z venkovní jednotky:** prasklá vanička pro kondenzát, dosluhující těsnění nebo neodborná instalace; odpojit napájení a volat servis.
- **Namrzlá klimatizace (namrzlý výparník):** ucpané filtry, nefunkční ventilátor nebo únik chladiva; nechat zkontrolovat odborníkem.

Ve spodní části stránky: „24/7 servis pro systémy větrání a klimatizace“, hotline +420 725 309 691 a kontaktní osoby:
- **Poptávky:** Martin Kulička, martin.kulicka@bohemik.cz, +420 602 666 187
- **Servis:** Matěj Rychlý, matej.rychly@bohemik.cz, +420 725 708 851

---

## 8. Ocelové konstrukce a průmyslové kabiny

### Ocelové konstrukce (`/ocelove-konstrukce`)
**Ocelové konstrukce z tenkostěnných a silnostěnných profilů**
> Bohemik jsou více než jen odborníci na průmyslové větrání.
>
> Pro naše zákazníky z oblasti průmyslu (převážně automotive), strojírenství a skladování, dodáváme na klíč ocelové konstrukce z tenkostěnných i silnostěnných profilů, které slouží především jako nosné ocelové konstrukce pod vzduchotechnické a klimatizační jednotky, případně pochozí obslužné konstrukce pod technologická zařízení včetně schodišť. Pro jednotlivé projekty volíme nejvhodnější technicko-ekonomické řešení, které vychází z požadavků na použití a prostředí, kde je ocelová konstrukce umístěna.

Ocelové konstrukce pod vzduchotechnické a klimatizační jednotky · Pochozí obslužné konstrukce pod technologická zařízení · Obslužná kovová schodiště · Ocelové lávky a podesty

### Průmyslové kabiny a vestavby (`/prumyslove-kabiny-a-vestavby`)
> Naším cílem je dodat zákazníkům co nejkomplexnější službu a spolehlivého partnera pro růst.
>
> Náš standard provedených prací se vztahuje na všechny subjekty zapojené do projektů, ať už se jedná o zaměstnance, dodavatele technologií či subdodavatele. Kromě služeb z oblasti HVAC dodáváme ocelové konstrukce, průmyslové kabiny a vestavky do hal, kde zúročujeme znalosti, které se prohlubují každým úspěšně předaným projektem. Jsme hrdi na rozsah činností, které umíme dnes nabídnout i na mezioborový přesah, kde můžeme zanechat otisk naší firemní kultury.

**Halové vestavky a průmyslové kabiny**
> Klimatizované vestavky, sloužící jako specializovaná pracoviště, navrhujeme s důrazem na vnitřní klimatické i zvukově izolační parametry. Pečlivě volené požárně odolné, případně zvukově izolační materiály, navrhujeme citlivě s důrazem na minimální dopad na životní prostředí. Nejčastější realizace jsou lakovací kabiny, kabiny s výbušným vnitřním prostředím, specializovaná pracoviště (laboratoře a velíny), případně pracoviště pro jednoúčelové stroje s vyšší hodnotou zvukové zátěže. V neposlední řadě je zakrytování průmyslových technologií, které vytvářejí nežádoucí odpadní teplo.

Klimatizované vestavky · Zakrytování průmyslových technologií s odsáváním · Průmyslové kabiny pro automatická zařízení i ruční pracoviště

---

## 9. Kariéra

### Výpis pozic (`/nabidka-volnych-pracovnich-mist`)
**Volná pracovní místa**
> Rosteme rychle a jsme stále na pozoru pro výjimečné talenty. Rozhlížíme se po dalších členech rodiny. Hledáme ty, jež mají chuť stále se zlepšovat a zejména osobnosti, za kterými ostatní přicházejí pro rady. Očekáváme hluboký zájem učit se novým věcem a být příkladem pro ostatní. Nabízíme pracovní příležitosti s velkým přesahem. Jestliže se Vám náš přístup líbí, neváhejte nás kontaktovat.
>
> Máme zájem o silné individuality i týmové hráče.

Každá pozice má štítek „NABÍDKA PRÁCE“, název, podtitulek, odstavec popisu, místo výkonu a tlačítko „Další informace“.

**Nezaujala Tě naše nabídka volných pracovních míst?**
> Lidí s kuráží si vážíme, proto podporujeme ty, jež přichází s novými nápady. Jestliže se Ti líbí naše filozofie a přijde Ti náš přístup k práci zajímavý, určitě nám neváhej napsat. Alena, která se v tuto chvíli věnuje hledání talentů, si s Tebou ráda popovídá o našem přístupu k práci. Zkus nám navrhnout, s čím bys nám mohl pomoct, protože v Bohemiku se vždy něco děje.

### Stavbyvedoucí (`/stavbyvedouci`)
**Ve výpisu:** Práce pro zkušeného stavbyvedoucího. Tato pozice je určena zkušenému stavbyvedoucímu, který se ujme řízení a koordinace stavebních projektů od zahájení až po předání díla. Budete zodpovídat za dodržování technologických postupů, harmonogramu a finančního plánu stavby, komunikovat s investory i dodavateli a vést potřebnou stavební dokumentaci. Čeká vás rozmanitá práce v menším, dynamickém kolektivu s možností profesního růstu a podpory při získání autorizace. Místo výkonu: Středočeský kraj.

**Co od vás očekáváme:**
- VŠ/SŠ vzdělání stavebního směru
- Autorizace IP00 nebo TP00 výhodou
- Znalost AutoCAD, KROS výhodou
- Praxi na obdobné pozici minimálně 2 roky
- Znalost a orientace v projektové dokumentaci
- Koordinace a řízení stavebních prací
- Kontrola dodržování technologických postupů stavby, harmonogramu a finančního plánu
- Komunikace s investorem a dodavateli stavby.
- Evidence příslušných dokladů a vedení stavební dokumentace.
- ŘP skupiny B

**Co nabízíme:**
- nerutinní práce v malém dynamickém kolektivu
- Pracovní smlouvu na dobu neurčitou, práci na plný úvazek
- 20 dní dovolené
- Možnosti školení a rozvoje (podpora při přípravě na autorizaci)
- Nástup možný ihned
- služební auto, telefon, notebook

Kontakt: info@bohemik.cz, nebo 602 417 831

### Rozpočtář / přípravář zakázek (`/rozpoctar`)
**Ve výpisu:** Práce pro pečlivého a samostatného rozpočtáře. Tato pozice je určena pečlivému a samostatnému rozpočtáři/přípraváři zakázek, který se bude podílet na přípravě a oceňování investičních celků v oblasti pozemního stavitelství. Vaším úkolem bude technická a administrativní podpora realizačního týmu, příprava podkladů pro objednávky, tendrování materiálu a subdodávek či zpracování změnových listů. Hledáme zkušeného profesionála se smyslem pro detail a schopností pracovat s projektovou dokumentací. Čeká vás moderní zázemí, přátelský kolektiv a zázemí stabilní, rostoucí společnosti. Místo výkonu: Středočeský kraj.

**Náplň práce:**
- Příprava a oceňování investičních celků pozemních staveb
- Administrativní a technická podpora realizačního týmu
- Příprava podkladů pro objednávání
- Tendrování materiálu/subdodávek
- Administrace změnových listů

**Požadujeme:**
- Vzdělání technického směru s maturitou
- Praxe na obdobné pozici nejméně 5 let
- Orientace v technických výkresech
- Uživatelská znalost MS Office
- Řidičský průkaz B (aktivní řidič)
- Zájem o další vzdělávání a školení
- Znalost AutoCAD výhodou (ne podmínkou)

**Co můžete očekávat:**
- Příjemný mladý kolektiv v dynamicky rozvíjející se stavební firmě
- Nově vybudované administrativní zázemí na Dobříši
- Nástup možný ihned
- Notebook a telefon

Kontakt: tel. 602 417 831, životopis na info@bohemik.cz. „Těšíme se!“

### Instalatér – topenář (`/instalater-topenar`)
**Ve výpisu:** Práce pro zručné topenáře. Tato pozice je určena zručnému instalatérovi – topenáři, který se bude podílet na montáži, opravách a údržbě vnitřních i venkovních rozvodů vody, kanalizace, plynu a topení. Součástí práce je také kontrola těsnosti, funkčnosti a kvality provedených instalací podle technické dokumentace. Hledáme spolehlivého odborníka s praxí, který se nebojí samostatné práce ani týmové spolupráce. Čeká vás stabilní zaměstnání, přátelský kolektiv a možnost dalšího profesního rozvoje. Místo výkonu: Středočeský kraj.

**Co od vás očekáváme:**
- Vyučení, SŠ technického směru výhodou
- Čtení technických výkresů a instalační dokumentace
- Praxi na obdobné pozici minimálně 2 roky
- Montáž, demontáž a opravy venkovních a vnitřních rozvodů vody, kanalizace, plynu a ústředního vytápění
- Kontrola těsnosti úniku provozních plynů a kapalin a funkčnosti provedených rozvodů a instalovaných zařízení.
- Dodržování zásad BOZP
- ŘP skupiny B

**Co nabízíme:**
- Příjemné pracovní prostředí v mladém kolektivu
- Pracovní smlouvu na dobu neurčitou, práci na plný úvazek
- 20 dní dovolené
- Možnosti školení a rozvoje
- Nástup možný ihned

Kontakt: info@bohemik.cz, nebo 602 417 831

### Staré pozice (stránka `/kopie-kariera`, mimo menu, nejspíš neaktuální)
Nadpis „Novinky ze života Bohemiku“, pozice:
- **Elektrikář – servisní technik klimatizace:** „Práce pro zručné elektrikáře, kteří neradi sedí na jednom místě.“ Vhodné i pro absolventy. Místo výkonu: Středočeský kraj, Severočeský kraj, Praha, Dobříš, Mladá Boleslav, Liberec, Most.
- **Projektant vzduchotechniky:** „Pěkná týmová práce v kanceláři s četnými výjezdy k zákazníkům.“ Místo výkonu: Dobříš, Praha a celá ČR.
- **Elektrikář – Technik MaR:** „Práce pro zkušeního ‚maráka‘.“ Zapojování VZT a klimatizačních jednotek, MaR.
- **Konstruktér ocelových konstrukcí / strojírenský technik:** AutoCAD, 3D, návrh ocelových konstrukcí; práce z kanceláře, z domova i u zákazníka.

Stránka `/kopie-elektrikar-technika-mar` je ve skutečnosti kopie servisní stránky („24/7 servis…“, „Rychlý kontakt“, regionální střediska).

---

## 10. Kontakty (`/kontakty`)

**Bohemik s.r.o.**
- IČ: 24265021
- DIČ: CZ24265021
- Datová schránka: cj8jye8
- Sídlo a provozovna: Pražská 636, 263 01 Dobříš
- Zápis: obchodní rejstřík vedený Městským soudem v Praze, spisová značka C 198858 *(z textu GDPR)*
- Email: info@bohemik.cz
- Tel: +420 326 722 707

**Osoby a linky:**

| Kdo | Role | E-mail | Telefon |
|---|---|---|---|
| Ing. Alena Bártová | Finance a administrativa (také nábor) | alena.bartova@bohemik.cz | +420 602 417 831 |
| Servis Hotline | Servisní dispečink | servis@bohemik.cz | +420 725 309 691 |
| Martin Kulička | Poptávky *(jen na stránce o závadách)* | martin.kulicka@bohemik.cz | +420 602 666 187 |
| Matěj Rychlý | Servis *(jen na stránce o závadách)* | matej.rychly@bohemik.cz | +420 725 708 851 |

**Formulář:** nadpis „Napište nám a zeptejte se na naše reference.“, tlačítko „Odeslat“, text pod ním „Tlačítkem odeslat potvrzuji souhlas se zpracováním osobních údajů.“ s odkazem na GDPR. Vedle formuláře je text o záručním a pozáručním servisu (stejný jako na stránce Servis pro firmy).

---

## 11. Ochrana osobních údajů (`/bohemik-ochrana-osobnich-kontaktu`)

Datováno: „V Dobříši dne 25/05/2018“. Struktura:
1. **Kdo zpracovává Vaše osobní údaje?** Bohemik s.r.o., IČO 24265021, Pražská 636, 263 01 Dobříš, zapsaná v OR u Městského soudu v Praze, sp. zn. C 198858, info@bohemik.cz.
2. **Jak a proč jsou Vaše osobní údaje zpracovávány?** Podle GDPR a zákona o zpracování osobních údajů, „abychom zajistili všechna naše i Vaše práva a povinnosti“. Bez automatizovaného rozhodování a profilování.
3. **Které Vaše osobní údaje zpracováváme?** Jen údaje získané přímo od subjektu, kvůli plnění smlouvy, právní povinnosti nebo se souhlasem.
4. **Jak chráníme Vaše osobní údaje?** Obecné prohlášení o řádné péči.
5. **Komu dalšímu poskytujeme Vaše osobní údaje a proč?** Nepředáváme bez souhlasu, kromě zákonné povinnosti nebo ochrany právních zájmů.
6. **Jaká máte práva?** Přístup, oprava, výmaz nebo omezení, námitka, přenositelnost, odvolání souhlasu, stížnost u ÚOOÚ (IČO 708 37 627, Pplk. Sochora 27, 170 00 Praha 7, https://www.uoou.cz).

**Co chybí pro nový web:** konkrétní účely a právní základy (kontaktní formulář, uchazeči o zaměstnání), doby uchování, příjemci a zpracovatelé (Web3Forms, hosting GitHub Pages), informace o cookies a analytice, datum aktualizace.

---

## 12. Blog (`/blog`, menu „Náš příběh“)

- **Kategorie:** Vzduchotechnika, Bohemik, Co nám dělá radost, Klimatizace.
- **Článek 1:** „Nejčastější závady domácích klimatizací a jejich řešení“ (16. 12. 2020, aktualizováno 17. 12. 2020, 2 min čtení). Obsahově totéž co stránka v kapitole 7.
- **Článek 2:** „Chodíme do práce rádi, protože nám tu je dobře“. Stránka se nenačítá (titulek „Post | Bohemik“, chyba widgetu). Článek je nejspíš smazaný nebo nepublikovaný.
- **RSS** (`/blog-feed.xml`) neobsahuje žádné články.

Blog je prakticky mrtvý. Na nový web ho nedoporučuju přenášet, novinky z firmy může nahradit Instagram.

---

## 13. Obrázky na starém webu

Odkazy vedou na originální velikost ve Wixu. Před použitím je potřeba ověřit práva, hlavně u fotek z Wikimedia Commons.

**Firma a zázemí**
- Logo: https://static.wixstatic.com/media/21d294_137cb3d662a045cb9488ad3670b7024a~mv2.png
- Logo malé: https://static.wixstatic.com/media/21d294_3232c2e3ea3f425eb985b0287a8d83dc~mv2.png
- Úvodní foto: https://static.wixstatic.com/media/21d294_6b38b3ea5afe4b5fbc7b4fa0cb53186c~mv2.jpg
- Loga zákazníků (jeden obrázek): https://static.wixstatic.com/media/21d294_0ddf397cd34e46579163849545c7c726~mv2.jpg
- Budova firmy Dobříš (`bohemik_dobris_firma_cb_edited.jpg`): https://static.wixstatic.com/media/21d294_7710386c90ac4d6ab76347faf85facef~mv2.jpg
- Foto z firmy (`bohemik_8.jpg`): https://static.wixstatic.com/media/21d294_44dcc96361d14c1ebc45ec0b4fe1799b~mv2_d_4032_2849_s_4_2.jpeg
- Kariéra banner: https://static.wixstatic.com/media/845dab_799354fb951c45dd8be063d1876e9601~mv2.webp
- Servisní ilustrace: https://static.wixstatic.com/media/21d294_64bf69bdce42433d8c8a641d666218a3~mv2.png
- Servisní technik: https://static.wixstatic.com/media/21d294_a993c7fdc79c4ccba1c06ab3d168fc57~mv2.jpg
- Kontakty (foto): https://static.wixstatic.com/media/21d294_c22dd7397a784ca48b563c2ad68adbfb~mv2.jpg
- Ing. Alena Bártová (portrét): https://static.wixstatic.com/media/845dab_95598d937f03404a99d0eaa4d7f17be1~mv2.webp
- Martin Kulička: https://static.wixstatic.com/media/21d294_e2a79d411cb24bf3b70faf76b322d3aa~mv2.jpg
- Matěj Rychlý: https://static.wixstatic.com/media/21d294_c450ecb5613e464190cf53f7bfbc1da6~mv2.jpg

**Služby**
- Kongresové centrum Praha: https://static.wixstatic.com/media/21d294_8721da4c3ba646acb2e28588c6a70fd3~mv2.jpg
- Průmysl / kabiny: https://static.wixstatic.com/media/21d294_974119118b934fa29fe07cb54b8beaab~mv2_d_4032_2008_s_2.jpeg
- MPO Praha (servis): https://static.wixstatic.com/media/21d294_5212d19d9d40455ead4f1a1f4b9a1791~mv2.jpg
- Ocelové konstrukce: https://static.wixstatic.com/media/21d294_3b6a5dc63cc94f41a2a7fcd831cea0f9~mv2_d_3805_2113_s_2.jpeg
- Servis klimatizace: https://static.wixstatic.com/media/21d294_44c79c60d9e04deebc1424333069d741~mv2.jpg

**Reference**

| Reference | URL |
|---|---|
| ZŠ Ležáků Hlinsko | https://static.wixstatic.com/media/845dab_4923fabe89a442bd88f60ad8cbb50524~mv2.jpg |
| ČNB | https://static.wixstatic.com/media/845dab_7e3233a82a0a4da2a8e2eff7ccf38a64~mv2.jpg |
| FN Motol | https://static.wixstatic.com/media/845dab_34476605aa474433b80d3df05d74ab19~mv2.jpg |
| Nemocnice Rakovník | https://static.wixstatic.com/media/845dab_16dcf8ebd1e54f86b7a751519faa6438~mv2.jpg |
| Thomayerova nemocnice | https://static.wixstatic.com/media/845dab_6eff3617515842b19db14368ec5853c1~mv2.jpg |
| Bazén Kralupy | https://static.wixstatic.com/media/845dab_2b692e4ab80a4ef1a8c6580d43fc1772~mv2.jpg |
| Bazén Slaný | https://static.wixstatic.com/media/845dab_9974b8a875db4051963ad44f0632a776~mv2.jpg |
| IKEM | https://static.wixstatic.com/media/845dab_297fcc1ac1bd46da975f4b4ec873b0c7~mv2.jpg |
| Planetárium | https://static.wixstatic.com/media/845dab_6bc31df0155a46cea58e186a52ae1ff0~mv2.jpg |
| NTM | https://static.wixstatic.com/media/845dab_fa70ca8b31aa46c78def41885a9b95c1~mv2.jpg |
| ZŠ Slaný | https://static.wixstatic.com/media/845dab_56caf9be55224558a24b13c6b2ffde42~mv2.jpg |
| Letiště Praha | https://static.wixstatic.com/media/845dab_d686ac6d5f37490f95f0bd51e4c199e8~mv2.jpg |
| Dětská skupina Trubín | https://static.wixstatic.com/media/845dab_1050b4ac5b7a4a3b8719dae8c8ea7c6a~mv2.jpg |
| Nemocnice Královské Vinohrady | https://static.wixstatic.com/media/845dab_43af088f61694d03a6e0719d208278b9~mv2.jpg |
| Zimní stadion Slaný | https://static.wixstatic.com/media/845dab_67b0d711d7334f0fb7d5554d50f4975a~mv2.jpg |

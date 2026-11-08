"""Institution pages (S2 schools / S3 FTS partners). Static, no forms, no scripts, no trackers.

Called from build.py:  kurumsal.build_pages(ctx)
ctx = dict(page=page, write=write, e=e, SITE=SITE, BRAND=BRAND, CONTACT=CONTACT)
"""
from urllib.parse import quote

NANO_STORE = "https://apps.apple.com/app/id6800853916?pt=128529947&ct=site-nano-kurum&mt=8"
NANO_PRIVACY_EN = "https://maliandro.github.io/profnano-site/privacy.html"
NANO_PRIVACY_TR = "https://maliandro.github.io/profnano-site/gizlilik.html"
FTS_STORE = "https://apps.apple.com/app/id6804052429?pt=128529947&ct=partners&mt=8"
FTS_PLAY = ("https://play.google.com/store/apps/details?id=com.maliandro.ayaktenisi"
            "&referrer=utm_source%3Dmeyade-site%26utm_medium%3Dpartners")

TODO_EN = "<!-- TODO S1: when the studio e-mail address exists, replace every mailto on this page (set CONTACT in build.py) -->\n"
TODO_TR = "<!-- TODO S1: stüdyo e-posta adresi belli olunca bu sayfadaki mailto'lar değişecek (build.py içinde CONTACT) -->\n"


def mailto(addr, subject, body):
    return f"mailto:{addr}?subject={quote(subject)}&body={quote(body)}"


def facts(items):
    return '<ul class="facts">' + "".join(
        f"<li><strong>{h}</strong><span>{t}</span></li>" for h, t in items) + "</ul>"


def shell(lang, hero_icon, hero_alt, h1, lead, sections, switch):
    sw_label, sw_href = switch
    other = "tr" if lang == "en" else "en"
    return f"""<main id="main" class="wrap section page-top org">
  <header class="page-head org-head">
    <img class="org-icon" src="{hero_icon}" alt="{hero_alt}" width="96" height="96" decoding="async" fetchpriority="high">
    <h1>{h1}</h1>
    <p class="lead-left">{lead}</p>
    <p class="langswitch"><a href="{sw_href}" hreflang="{other}" lang="{other}">{sw_label}</a></p>
  </header>
{sections}
</main>"""


def build_pages(ctx):
    page, write, e, SITE, BRAND, C = (ctx[k] for k in ("page", "write", "e", "SITE", "BRAND", "CONTACT"))

    def alt_links(en, tr):
        return (f'<link rel="alternate" hreflang="en" href="{SITE}{en}">\n'
                f'<link rel="alternate" hreflang="tr" href="{SITE}{tr}">\n'
                f'<link rel="alternate" hreflang="x-default" href="{SITE}{en}">\n')

    def webpage(name, path, lang):
        return [{"@context": "https://schema.org", "@type": "WebPage", "name": name, "url": SITE + path,
                 "inLanguage": lang, "publisher": {"@id": SITE + "/#org"}}]

    # ---------------------------------------------------------------- S2 Prof. Nano, English
    m_en = mailto(C, "Prof. Nano: free review code request",
                  "Hello,\n\nWe would like a free Full Version review code for Prof. Nano.\n\n"
                  "Name and role:\nSchool / library / institution:\nCountry:\n\nThank you.")
    sec_en = f"""  <section class="org-sec" aria-labelledby="what-h">
    <h2 id="what-h">What Prof. Nano is</h2>
    <p>Prof. Nano is a hands-on science game for children aged 7 to 10. A friendly professor explains out loud while children experiment and see what happens on screen. Eight regions hold 48 short mini games, from atoms to stars and from the heart to robots.</p>
    {facts([("Ages 7–10", "Short activities, read-aloud explanations"),
            ("48 mini games", "Across 8 regions, all hands-on"),
            ("Works offline", "No internet needed after the download"),
            ("No ads", "Nothing to tap by accident"),
            ("No data collection", "No accounts, no tracking"),
            ("Parent gate", "Purchases sit behind a parent gate")])}
  </section>
  <section class="org-sec" aria-labelledby="try-h">
    <h2 id="try-h">Free to try, one-time Full Version</h2>
    <p>The first region, <strong>Lighthouse Point</strong>, is free to play with no time limit, so a class, a family or a librarian can see exactly what children will do. The <strong>Full Version</strong> opens all 8 regions and every game. It is a single one-time purchase with no subscription, and it sits behind a parent gate.</p>
    <p>The game runs in Turkish and English. Prof. Nano is on the App Store for iPhone and iPad. <strong>Android is coming soon.</strong></p>
    <p class="btn-row"><a class="btn primary" href="{NANO_STORE}" target="_blank" rel="noopener">Prof. Nano on the App Store</a>
    <a class="btn" href="{NANO_PRIVACY_EN}" target="_blank" rel="noopener">Privacy policy</a></p>
  </section>
  <section class="org-sec" aria-labelledby="inst-h">
    <h2 id="inst-h">For institutions and educators</h2>
    <p>Teachers, school librarians, public libraries and home-education groups are welcome to review Prof. Nano before deciding anything. <strong>Write to us and we will send free Full Version review codes on request.</strong> Please tell us who you are and where you teach or work, so we can send the right number of codes.</p>
    <p>We do not offer bulk licences at this time. If that changes, this page will say so.</p>
    <p class="btn-row"><a class="btn primary" href="{e(m_en)}">Request a review code</a></p>
    <p class="note-line">Or write to <a href="mailto:{C}">{C}</a>. This page has no forms and no analytics, and sets no cookies.</p>
  </section>
  <section class="org-sec" aria-labelledby="who-h">
    <h2 id="who-h">Who makes it</h2>
    <p>{BRAND} is a small independent studio in Turkey. See <a href="/">all our games</a> or read <a href="/blog/prof-nano/">why we built Prof. Nano</a>.</p>
  </section>"""
    write("for-schools/index.html", page(
        path="/for-schools/", title="Prof. Nano for Schools and Home Education",
        desc="Prof. Nano: offline science game for ages 7 to 10. 48 hands-on mini games, no ads, no data collection. Free review codes for schools and libraries.",
        body=shell("en", "/img/prof-nano.jpg", "Prof. Nano science game icon",
                   "Prof. Nano for schools, libraries and home education",
                   "A calm, offline science game for ages 7 to 10. No ads, no data collection. Review it free.",
                   sec_en, ("Türkçe sürüm", "/tr/okullar/")),
        active="", image="/img/prof-nano.jpg",
        ld=webpage("Prof. Nano for schools, libraries and home education", "/for-schools/", "en"),
        head_extra=TODO_EN + alt_links("/for-schools/", "/tr/okullar/"), lang="en"))

    # ---------------------------------------------------------------- S2 Prof. Nano, Turkish
    m_tr = mailto(C, "Prof. Nano: ücretsiz inceleme kodu isteği",
                  "Merhaba,\n\nProf. Nano için ücretsiz Tam Sürüm inceleme kodu rica ediyoruz.\n\n"
                  "Ad ve görev:\nOkul / kütüphane / kurum:\nŞehir:\n\nTeşekkürler.")
    sec_tr = f"""  <section class="org-sec" aria-labelledby="what-h">
    <h2 id="what-h">Prof. Nano nedir?</h2>
    <p>Prof. Nano, 7-10 yaş çocuklar için uygulamalı bir bilim oyunu. Çocuk dener, ekranda olanı görür, Prof. Nano sesli anlatır. Sekiz bölgede, atomdan yıldızlara, kalpten robotlara 48 küçük oyun var.</p>
    {facts([("7-10 yaş", "Kısa etkinlikler, sesli anlatım"),
            ("48 küçük oyun", "8 bölgede, hepsi uygulamalı"),
            ("Çevrimdışı çalışır", "İndirdikten sonra internet gerekmez"),
            ("Reklam yok", "Yanlışlıkla dokunulacak reklam yok"),
            ("Veri toplamaz", "Hesap yok, izleme yok"),
            ("Veli kapısı", "Satın alma veli kapısının arkasında")])}
  </section>
  <section class="org-sec" aria-labelledby="try-h">
    <h2 id="try-h">Önce ücretsiz dene, sonra tek seferlik Tam Sürüm</h2>
    <p>İlk bölge <strong>Lighthouse Point</strong> süresiz ve ücretsiz. Sınıf, aile ya da kütüphaneci çocukların tam olarak ne yapacağını görebilir. <strong>Tam Sürüm</strong> 8 bölgenin ve bütün oyunların kilidini açar. Tek seferlik ödemedir, abonelik yoktur ve veli kapısının arkasındadır.</p>
    <p>Oyun Türkçe ve İngilizce çalışır. Prof. Nano şu an iPhone ve iPad için App Store'da. <strong>Android sürümü yakında.</strong></p>
    <p class="btn-row"><a class="btn primary" href="{NANO_STORE}" target="_blank" rel="noopener">Prof. Nano App Store'da</a>
    <a class="btn" href="{NANO_PRIVACY_TR}" target="_blank" rel="noopener">Gizlilik politikası</a></p>
  </section>
  <section class="org-sec" aria-labelledby="inst-h">
    <h2 id="inst-h">Kurumlar ve eğitimciler için</h2>
    <p>Öğretmenler, okul kütüphaneleri, halk kütüphaneleri ve evde eğitim grupları, karar vermeden önce Prof. Nano'yu inceleyebilir. <strong>Bize yazın, istek üzerine ücretsiz Tam Sürüm inceleme kodu gönderelim.</strong> Kim olduğunuzu ve nerede görev yaptığınızı yazmanız, doğru sayıda kod göndermemize yardımcı olur.</p>
    <p>Şu an toplu lisans sunmuyoruz. Bu değişirse bu sayfada yazar.</p>
    <p class="btn-row"><a class="btn primary" href="{e(m_tr)}">İnceleme kodu iste</a></p>
    <p class="note-line">Ya da doğrudan <a href="mailto:{C}">{C}</a> adresine yazın. Bu sayfada form, analiz aracı ve çerez yoktur.</p>
  </section>
  <section class="org-sec" aria-labelledby="who-h">
    <h2 id="who-h">Kim yapıyor?</h2>
    <p>{BRAND}, Türkiye'de küçük bağımsız bir stüdyo. <a href="/">Bütün oyunlarımıza</a> bakabilir ya da <a href="/blog/prof-nano/">Prof. Nano'yu neden yaptığımızı</a> (İngilizce) okuyabilirsiniz.</p>
  </section>"""
    write("tr/okullar/index.html", page(
        path="/tr/okullar/", title="Okullar İçin Prof. Nano: Çocuk Bilim Oyunu",
        desc="Prof. Nano: 7-10 yaş için çevrimdışı bilim oyunu. 48 uygulamalı küçük oyun, reklam yok, veri toplanmaz. Okullara ve kütüphanelere ücretsiz inceleme kodu.",
        body=shell("tr", "/img/prof-nano.jpg", "Prof. Nano bilim oyunu simgesi",
                   "Okullar, kütüphaneler ve evde eğitim için Prof. Nano",
                   "7-10 yaş için sakin, çevrimdışı bir bilim oyunu. Reklam yok, veri toplanmaz. Ücretsiz inceleyin.",
                   sec_tr, ("English version", "/for-schools/")),
        active="", image="/img/prof-nano.jpg",
        ld=webpage("Okullar, kütüphaneler ve evde eğitim için Prof. Nano", "/tr/okullar/", "tr"),
        head_extra=TODO_TR + alt_links("/for-schools/", "/tr/okullar/"), lang="tr"))

    # ---------------------------------------------------------------- S3 FTS partners, English
    p_en = mailto(C, "Foot Tennis Stars: partnership enquiry",
                  "Hello,\n\nWe are writing about a partnership or a stadium board in Foot Tennis Stars.\n\n"
                  "Name and organisation:\nWhat you have in mind:\n\nThank you.")
    stores = (f'<a class="btn primary" href="{FTS_STORE}" target="_blank" rel="noopener">App Store</a> '
              f'<a class="btn" href="{FTS_PLAY}" target="_blank" rel="noopener">Google Play</a>')
    sec_fts_en = f"""  <section class="org-sec" aria-labelledby="what-h">
    <h2 id="what-h">The game</h2>
    <p>Foot Tennis Stars brings foot tennis to the phone: real foot tennis rules, a net, smash shots and rallies you can read. Players on iPhone and Android meet in the same online matches. The store page is available in 39 languages.</p>
    {facts([("Real foot tennis", "Rules, net, smashes and rallies"),
            ("Online play", "iPhone and Android players in the same match"),
            ("Your own club", "Turn your winnings into a clubhouse, stands and floodlights"),
            ("Celebrations", "Fist pumps, trophy lifts, a Nations Cup walk-out"),
            ("Nine arenas", "From an indoor hall to a rooftop and a beach"),
            ("Players in Thailand", "The game already has players abroad")])}
    <p class="btn-row">{stores}</p>
  </section>
  <section class="org-sec" aria-labelledby="fed-h">
    <h2 id="fed-h">Federation</h2>
    <p>The game is made with respect for the sport. The name and emblem of the Turkish Foot Tennis Federation already appear inside the game. We would like to work with the federation and with clubs, leagues and events: a shared announcement, an official event or cup name inside the game, or a QR poster for a hall or a broadcast. We ask for nothing in return, and we only use a name or an emblem with written permission.</p>
    <!-- Reviewer note: no emblem image is used on this page on purpose. Written permission is needed before the federation's emblem appears in sponsor material. -->
  </section>
  <section class="org-sec" aria-labelledby="board-h">
    <h2 id="board-h">Stadium boards for sponsors</h2>
    <p>Every arena has advertising boards along the side and back of the pitch, the way a real match does. They are seen in every rally, every replay and in the Nations Cup final. A brand, a club or an event can have its own board in the game, together with a venue or cup name.</p>
    <p>Partnership options are flexible: stadium boards, a named cup or a special in-game event. <strong>Get in touch and tell us what you have in mind</strong>; we will reply with a clear proposal that fits your goals. We do not publish prices on this page.</p>
    <p>We do not count impressions inside the game. Any figure we give you about reach would be an estimate, and we will say so.</p>
  </section>
  <section class="org-sec" aria-labelledby="contact-h">
    <h2 id="contact-h">Contact</h2>
    <p class="btn-row"><a class="btn primary" href="{e(p_en)}">Write to us</a></p>
    <p class="note-line">Or write to <a href="mailto:{C}">{C}</a>. This page has no forms and no analytics, and sets no cookies.</p>
  </section>"""
    write("foot-tennis-stars/partners/index.html", page(
        path="/foot-tennis-stars/partners/", title="Foot Tennis Stars: Partners and Sponsors",
        desc="Foot Tennis Stars is a mobile foot tennis game with online play and its own club system. Partnership, federation and stadium board sponsor enquiries are welcome.",
        body=shell("en", "/img/foot-tennis-stars-2.jpg", "Foot Tennis Stars foot tennis game icon",
                   "Foot Tennis Stars: partners, sponsors and federations",
                   "A mobile foot tennis game with online play. Work with us on events, cups and stadium boards.",
                   sec_fts_en, ("Türkçe sürüm", "/tr/ayak-tenisi/")),
        active="", image="/img/foot-tennis-stars-2.jpg",
        ld=webpage("Foot Tennis Stars: partners, sponsors and federations", "/foot-tennis-stars/partners/", "en"),
        head_extra=TODO_EN + alt_links("/foot-tennis-stars/partners/", "/tr/ayak-tenisi/"), lang="en"))

    # ---------------------------------------------------------------- S3 FTS partners, Turkish
    p_tr = mailto(C, "Ayak Tenisi Yıldızları: iş birliği",
                  "Merhaba,\n\nAyak Tenisi Yıldızları'nda iş birliği ya da saha panosu için yazıyoruz.\n\n"
                  "Ad ve kurum:\nAklınızdaki fikir:\n\nTeşekkürler.")
    sec_fts_tr = f"""  <section class="org-sec" aria-labelledby="what-h">
    <h2 id="what-h">Oyun</h2>
    <p>Ayak Tenisi Yıldızları (Foot Tennis Stars), ayak tenisini telefona taşır: gerçek ayak tenisi kuralları, file, smaç vuruşları ve okunabilir toplar. iPhone ve Android oyuncuları aynı online maçlarda buluşur. Mağaza sayfası 39 dilde.</p>
    {facts([("Gerçek ayak tenisi", "Kurallar, file, smaçlar ve uzun toplar"),
            ("Online oyun", "iPhone ve Android oyuncuları aynı maçta"),
            ("Kendi kulübün", "Kazandığın altınla kulüp evi, tribün ve ışıklar kur"),
            ("Kutlamalar", "Yumruk sıkma, kupa kaldırma, Nations Cup çıkışı"),
            ("Dokuz saha", "Kapalı salondan çatıya ve plaja"),
            ("Tayland'da oyuncular", "Oyunun yurt dışında da oyuncuları var")])}
    <p class="btn-row">{stores}</p>
  </section>
  <section class="org-sec" aria-labelledby="fed-h">
    <h2 id="fed-h">Federasyon</h2>
    <p>Oyun, spora saygıyla yapıldı. Türkiye Ayak Tenisi Federasyonu'nun adı ve amblemi oyunun içinde zaten yer alıyor. Federasyonla, kulüplerle, liglerle ve etkinliklerle çalışmak isteriz: ortak duyuru, oyun içinde resmî bir etkinlik ya da kupa adı, salon ya da yayın için QR afişi. Karşılığında bir bedel beklemiyoruz; bir ad ya da amblemi yalnızca yazılı izinle kullanırız.</p>
    <!-- Not: federasyon amblemi için yazılı izin gelene kadar bu sayfada amblem görseli bilerek kullanılmadı. -->
  </section>
  <section class="org-sec" aria-labelledby="board-h">
    <h2 id="board-h">Sponsorlar için stadyum panoları</h2>
    <p>Her sahada, gerçek bir maçtaki gibi, sahanın yanında ve arkasında reklam panoları var. Her ralide, her tekrarda ve Nations Cup finalinde görünürler. Bir marka, kulüp ya da etkinlik, oyunda kendi panosuna ve isterse bir saha ya da kupa adına sahip olabilir.</p>
    <p>Ortaklık seçenekleri esnek: stadyum panoları, adınızı taşıyan bir kupa ya da oyun içi özel bir etkinlik. <strong>Bizimle iletişime geçin, aklınızdaki fikri yazın</strong>; hedeflerinize uyan net bir teklifle dönelim. Bu sayfada fiyat yayımlamıyoruz.</p>
    <p>Oyun içinde gösterim saymıyoruz. Erişim hakkında verdiğimiz her rakam bir tahmin olur ve öyle söyleriz.</p>
  </section>
  <section class="org-sec" aria-labelledby="contact-h">
    <h2 id="contact-h">İletişim</h2>
    <p class="btn-row"><a class="btn primary" href="{e(p_tr)}">Bize yazın</a></p>
    <p class="note-line">Ya da doğrudan <a href="mailto:{C}">{C}</a> adresine yazın. Bu sayfada form, analiz aracı ve çerez yoktur.</p>
  </section>"""
    write("tr/ayak-tenisi/index.html", page(
        path="/tr/ayak-tenisi/", title="Ayak Tenisi Yıldızları: Ortaklar ve Sponsorlar",
        desc="Ayak Tenisi Yıldızları, online oyunu ve kulüp sistemi olan bir mobil ayak tenisi oyunu. Federasyon, kulüp, lig ve sponsor iş birliği için yazabilirsiniz.",
        body=shell("tr", "/img/foot-tennis-stars-2.jpg", "Ayak Tenisi Yıldızları oyun simgesi",
                   "Ayak Tenisi Yıldızları: ortaklar, sponsorlar ve federasyonlar",
                   "Online oynanan mobil bir ayak tenisi oyunu. Etkinlik, kupa ve stadyum panosu için bizimle çalışın.",
                   sec_fts_tr, ("English version", "/foot-tennis-stars/partners/")),
        active="", image="/img/foot-tennis-stars-2.jpg",
        ld=webpage("Ayak Tenisi Yıldızları: ortaklar, sponsorlar ve federasyonlar", "/tr/ayak-tenisi/", "tr"),
        head_extra=TODO_TR + alt_links("/foot-tennis-stars/partners/", "/tr/ayak-tenisi/"), lang="tr"))

    return ["/for-schools/", "/tr/okullar/", "/foot-tennis-stars/partners/", "/tr/ayak-tenisi/"]

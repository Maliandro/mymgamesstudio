"""Bing / Yandex / Seznam / Naver'a sitemap'teki adresleri bildirir (IndexNow). Yayından sonra çalıştır:
    python indexnow.py
"""
import glob, json, os, re, urllib.request
SITE = "https://meyadegamesstudio.vercel.app"
KOK = os.path.dirname(os.path.abspath(__file__))
key = [os.path.basename(f)[:-4] for f in glob.glob(os.path.join(KOK, "*.txt")) if re.fullmatch(r"[0-9a-f]{32}\.txt", os.path.basename(f))][0]
urls = re.findall(r"<loc>(.*?)</loc>", open(os.path.join(KOK, "sitemap.xml"), encoding="utf-8").read())
body = json.dumps({"host": "meyadegamesstudio.vercel.app", "key": key, "keyLocation": f"{SITE}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
try:
    r = urllib.request.urlopen(req, timeout=30); print("IndexNow:", r.status, len(urls), "adres")
except urllib.error.HTTPError as e:
    print("IndexNow HATA:", e.code, e.read()[:200])

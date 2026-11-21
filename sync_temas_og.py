import os, re, json, html, urllib.request

with open("index.html", "r", encoding="utf-8") as f:
    src = f.read()

url_m = re.search(r'https://[a-zA-Z0-9-]+\.supabase\.co', src)
key_m = re.search(r'eyJ[a-zA-Z0-9._-]+', src)

if not url_m or not key_m:
    print("ERROR: No se encontro SUPABASE_URL o ANON_KEY en index.html")
    raise SystemExit(1)

sb_url = url_m.group(0).rstrip("/")
sb_key = key_m.group(0)
base_url = "https://meygey.github.io/Sistema-z"
default_img = f"{base_url}/portada-sistema-z.jpg?v=2"

req = urllib.request.Request(
    f"{sb_url}/rest/v1/temas_z?select=id,artist,title,genre,cover_url,copyright",
    headers={"apikey": sb_key, "Authorization": f"Bearer {sb_key}"}
)

with urllib.request.urlopen(req, timeout=20) as resp:
    temas = json.loads(resp.read().decode("utf-8"))

os.makedirs("t", exist_ok=True)
count = 0

for item in temas:
    tid = str(item.get("id", "")).strip()
    if not tid:
        continue
    artist = html.escape(str(item.get("artist") or "Artista Independiente"))
    title = html.escape(str(item.get("title") or "Tema sin titulo"))
    genre = html.escape(str(item.get("genre") or "Urbano"))
    cpr = html.escape(str(item.get("copyright") or "Copyright Z"))
    raw_cover = str(item.get("cover_url") or "").strip()
    cover = html.escape(raw_cover if raw_cover.startswith("http") else default_img)

    og_title = f"{title} — {artist} | Sistema Z"
    og_desc = f"Genero: {genre} | {cpr} | Escucha en Sistema Z"
    page_url = f"{base_url}/t/{tid}.html"
    target_url = f"{base_url}/?tema={tid}"

    page_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{og_title}</title>
  <meta property="og:type" content="music.song">
  <meta property="og:site_name" content="Sistema Z">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:image" content="{cover}">
  <meta property="og:url" content="{page_url}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{og_desc}">
  <meta name="twitter:image" content="{cover}">
  <meta http-equiv="refresh" content="0;url={target_url}">
  <script>window.location.replace("{target_url}");</script>
</head>
<body style="background:#080808;color:#fff;font-family:sans-serif;text-align:center;padding:40px;">
  <p>Cargando <strong>{title}</strong> de <strong>{artist}</strong> en Sistema Z...</p>
  <p><a href="{target_url}" style="color:#ef4444;">Abrir tema ahora</a></p>
</body>
</html>
"""
    with open(f"t/{tid}.html", "w", encoding="utf-8") as out:
        out.write(page_html)
    count += 1

print(f"TEMAS_OG_GENERADOS:{count}")

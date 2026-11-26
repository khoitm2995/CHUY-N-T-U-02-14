import base64, os, json

assets_dir = "assets"
embedded = {}

for filename in os.listdir(assets_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        key = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1].lower().replace(".", "")
        mime = "jpeg" if ext in ("jpg", "jpeg") else "png"
        with open(os.path.join(assets_dir, filename), "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            embedded[key] = f"data:image/{mime};base64,{b64}"

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Chèn biến toàn cục chứa toàn bộ ảnh Base64 vào trước thẻ </head>
inject_script = f"<script>window.EMBEDDED_ASSETS = {json.dumps(embedded)};</script>\n</head>"
bundled_html = html.replace("</head>", inject_script, 1)

with open("chuyen_tau_0214_offline.html", "w", encoding="utf-8") as f:
    f.write(bundled_html)

print(f"Đã đóng gói thành công {len(embedded)} ảnh vào chuyen_tau_0214_offline.html!")
# VAM 分享地圖

用 [Visual Agent Map](https://github.com/kevcltsai/visual-agent-map) 匯出的心智圖分享檔。每個 `.html` 都是單一檔案，不需要網路也能瀏覽。

## 目前的地圖

全部地圖列在首頁：<https://kevcltsai.github.io/vam-shared-maps/>

首頁（`index.html`）由 GitHub Action 自動產生，不要手動修改。

## 怎麼新增一張地圖

1. 在 Obsidian 打開地圖，按右上角的分享圖示（或命令面板「分享這張地圖」），再按「儲存…」。
2. 把存好的 `.html` 放進 `maps/`，檔名用英文或數字，例如 `cooking-science.html`。
3. （選填）在 `maps.json` 幫它加分類和一句說明；沒加的話會出現在首頁的「其他」，標題取自 HTML 的 `<title>`。
4. commit 並 push。Action 會重建 `index.html`，約一兩分鐘後首頁更新，地圖網址是 `https://kevcltsai.github.io/vam-shared-maps/maps/<檔名>.html`。

本地預覽首頁：`python3 scripts/build_index.py`

## 注意

這個 repo 是公開的：放進來的地圖，任何人都能看到完整筆記內容。放之前先確認內容可以公開。

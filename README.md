# VAM 分享地圖

用 [Visual Agent Map](https://github.com/kevcltsai/visual-agent-map) 匯出的心智圖分享檔。每個 `.html` 都是單一檔案，不需要網路也能瀏覽。

## 目前的地圖

也可以在首頁瀏覽：<https://kevcltsai.github.io/vam-shared-maps/>

<!-- MAPS:START — 以下由 scripts/build_index.py 自動產生，請勿手動修改 -->

### 料理與食物

| 地圖 | 說明 |
|---|---|
| [料理的科學](https://kevcltsai.github.io/vam-shared-maps/maps/cooking-science.html) | 第一次煎牛排要知道的事 |
| [料理的科學（繁／簡／英）](https://kevcltsai.github.io/vam-shared-maps/maps/steak_ch_eng.html) | 同一張牛排地圖的多語版本 |
| [料理的科學（繁／簡／英，另一版）](https://kevcltsai.github.io/vam-shared-maps/maps/cooking_steak_ch_eng.html) | 多語版本的另一份翻譯 |
| [牛肉各部位熱量](https://kevcltsai.github.io/vam-shared-maps/maps/beef_parts.html) | 紐約客、牛肋條等部位的熱量比較 |

### 知識與思考

| 地圖 | 說明 |
|---|---|
| [數學在幹嘛](https://kevcltsai.github.io/vam-shared-maps/maps/math.html) | 數學到底在做什麼 |
| [哲學在追問什麼](https://kevcltsai.github.io/vam-shared-maps/maps/philosophy.html) | 從「我怎麼知道什麼是真的？」等根問題出發 |
| [思考框架圖文書](https://kevcltsai.github.io/vam-shared-maps/maps/thinking_frameworks.html) | 為什麼需要框架、有哪些框架 |
| [金錢是什麼圖文書](https://kevcltsai.github.io/vam-shared-maps/maps/whats_money.html) | 從「沒有錢的世界」談金錢到底是什麼 |
| [英文文法](https://kevcltsai.github.io/vam-shared-maps/maps/english_grammar.html) | 文法的本質與理論基礎 |
| [看懂一幅畫：世界名畫背後的故事](https://kevcltsai.github.io/vam-shared-maps/maps/art_appreciation.html) | 怎麼看一幅畫，以及名畫背後的故事 |

### 示範

| 地圖 | 說明 |
|---|---|
| [假設驅動示範](https://kevcltsai.github.io/vam-shared-maps/maps/hypothesis_demo.html) | 以「美國年輕人失業率高，主因是 AI 嗎？」示範假設式拆解 |

### 其他

| 地圖 | 說明 |
|---|---|
| [財富的法則](https://kevcltsai.github.io/vam-shared-maps/maps/about_wealth.html) |  |
| [42歲女性的瘦身與美容](https://kevcltsai.github.io/vam-shared-maps/maps/for_her.html) |  |
| [背部伸展](https://kevcltsai.github.io/vam-shared-maps/maps/muscle_stretches.html) |  |
| [心理學圖文書](https://kevcltsai.github.io/vam-shared-maps/maps/psychology.html) |  |
| [不想讓你知道的世界真相](https://kevcltsai.github.io/vam-shared-maps/maps/untold_truth.html) |  |

<!-- MAPS:END -->

## 怎麼新增一張地圖

1. 在 Obsidian 打開地圖，按右上角的分享圖示（或命令面板「分享這張地圖」），再按「儲存…」。
2. 把存好的 `.html` 放進 `maps/`，檔名用英文或數字，例如 `cooking-science.html`。
3. （選填）在 `maps.json` 幫它加分類和一句說明；沒加的話會出現在首頁的「其他」，標題取自 HTML 的 `<title>`。
4. commit 並 push。Action 會重建 `index.html` 和 README 的地圖清單，約一兩分鐘後首頁更新，地圖網址是 `https://kevcltsai.github.io/vam-shared-maps/maps/<檔名>.html`。

本地預覽首頁：`python3 scripts/build_index.py`

## 注意

這個 repo 是公開的：放進來的地圖，任何人都能看到完整筆記內容。放之前先確認內容可以公開。

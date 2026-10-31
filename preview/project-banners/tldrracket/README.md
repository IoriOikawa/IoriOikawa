# TLDrRacket 项目横幅

沿用 Tenpai Prism 的双版本样板，保留左侧人物、右侧简短介绍的结构。
横幅已接入个人主页的 Projects 区域；此目录保留独立预览和复用写法。

打开同目录 `index.html` 查看自动选图。视口不超过 600 像素使用手机紧凑版，
超过时使用电脑横版。整张横幅链接到项目仓库。

<a href="https://github.com/IoriOikawa/TLDrRacket">
  <picture>
    <source media="(max-width: 600px)" srcset="../../../assets/projects/tldrracket/banner-mobile.png">
    <img src="../../../assets/projects/tldrracket/banner-desktop.png"
         alt="TLDrRacket: An RAG reading companion for Racket learners. View project."
         width="1200">
  </picture>
</a>

## 图片和源文件

- 电脑横版：`assets/projects/tldrracket/banner-desktop.png`，1200 × 400。
- 手机紧凑版：`assets/projects/tldrracket/banner-mobile.png`，750 × 450。
- 可编辑排版：`assets/projects/tldrracket/banner-source.html`。
- 原始人物：`asset_input/tldrracket_sicp.png`，与提供的 `sicp.png` 内容完全相同。

人物、电脑和 SICP 书完整保留，未重新绘制或裁切主体。配色沿用原图的靛蓝、
灰紫和暖金。两版说明相同，手机版单独增大相对字号并压缩留白。

横幅文字根据[项目最新 README](https://github.com/IoriOikawa/TLDrRacket#readme)
采用指定英文说明 “An RAG reading companion for Racket learners.”，不再另加第二句，
并标明 CS4400 / CS5400；入口文字为 “View project”。

修改排版源文件后，需要重新导出两张 PNG。源文件可使用 `?layout=desktop`
和 `?layout=mobile` 分别查看两种固定画布。

## 加入主 README 时的写法

```html
<a href="https://github.com/IoriOikawa/TLDrRacket">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/projects/tldrracket/banner-mobile.png">
    <img src="assets/projects/tldrracket/banner-desktop.png"
         alt="TLDrRacket: An RAG reading companion for Racket learners. View project."
         width="1200">
  </picture>
</a>
```

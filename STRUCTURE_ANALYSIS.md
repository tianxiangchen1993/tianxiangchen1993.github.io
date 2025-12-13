# 个人主页项目结构分析

## 📋 项目概览

**项目名称**: AcadHomepage（学术个人主页）  
**技术栈**: Jekyll + GitHub Pages  
**用途**: 学术研究人员个人学术主页  
**部署地址**: https://github.com/tianxiangchen1993/tianxiangchen1993.github.io  
**作者**: 陈天翔（Tianxiang Chen）  
**职位**: 香港理工大学应用生物及化学技术系 研究助理教授

---

## 🏗️ 核心项目结构

```
tianxiangchen1993.github.io/
├── 📄 配置文件层
│   ├── _config.yml                 # Jekyll 主配置文件（站点元数据、作者信息、插件等）
│   ├── Gemfile                     # Ruby 依赖管理（Jekyll、插件声明）
│   ├── Gemfile.lock                # 依赖版本锁定文件
│   └── .gitignore                  # Git 忽略规则
│
├── 📄 站点文件层
│   ├── README.md                   # 项目说明文档
│   ├── LICENSE                     # 许可证
│   ├── run_server.sh               # 本地运行脚本
│   └── STRUCTURE_ANALYSIS.md       # 本文件
│
├── 📁 内容层（Jekyll 源文件）
│   ├── _pages/                     # 页面内容（Markdown）
│   │   └── about.md                # 主页内容（学历、工作经验、研究方向）
│   │
│   ├── _layouts/                   # 页面布局模板
│   │   └── default.html            # 默认布局（HTML 结构、头尾等）
│   │
│   ├── _includes/                  # 可复用的 HTML 片段
│   │   ├── author-profile.html     # 作者个人信息卡片（头像、社交链接等）
│   │   ├── masthead.html           # 网站头部导航栏
│   │   ├── sidebar.html            # 侧边栏
│   │   ├── head.html               # HTML <head> 部分
│   │   ├── scripts.html            # 脚本加载
│   │   ├── seo.html                # SEO 元标签
│   │   ├── analytics.html          # Google Analytics 代码
│   │   ├── fetch_google_scholar_stats.html  # Google Scholar 引用统计
│   │   └── head/                   # 自定义 head 片段
│   │       └── custom.html         # 用户自定义 head
│   │
│   ├── _data/                      # 数据文件
│   │   └── navigation.yml          # 导航菜单配置
│   │
│   └── _sass/                      # SCSS 样式源文件
│       ├── _variables.scss         # CSS 变量（颜色、字体等）
│       ├── _base.scss              # 基础样式
│       ├── _masthead.scss          # 头部样式
│       ├── _sidebar.scss           # 侧边栏样式
│       ├── _page.scss              # 页面样式
│       ├── _archive.scss           # 归档样式
│       ├── _navigation.scss        # 导航样式
│       ├── _buttons.scss           # 按钮样式
│       ├── _forms.scss             # 表单样式
│       ├── _tables.scss            # 表格样式
│       ├── _notices.scss           # 提示框样式
│       ├── _utilities.scss         # 工具类样式
│       ├── _reset.scss             # 重置样式
│       ├── _footer.scss            # 页脚样式
│       ├── _animations.scss        # 动画样式
│       ├── _print.scss             # 打印样式
│       ├── _mixins.scss            # SCSS Mixin 混入
│       └── vendor/                 # 第三方 SCSS 库
│           ├── breakpoint/         # 响应式设计库
│           ├── font-awesome/       # FontAwesome 图标库
│           ├── magnific-popup/     # 弹出窗口库
│           └── susy/               # 栅格系统库
│
├── 📁 静态资源层
│   ├── assets/
│   │   ├── css/                    # 编译后的 CSS 文件
│   │   │   ├── main.scss           # 主样式表（编译后 main.css）
│   │   │   ├── academicons.css     # 学术图标库
│   │   │   └── collapse.css        # 折叠动画
│   │   │
│   │   ├── js/                     # JavaScript 文件
│   │   │   ├── _main.js            # 主 JS 逻辑
│   │   │   ├── main.min.js         # 压缩版本
│   │   │   ├── collapse.js         # 折叠功能
│   │   │   ├── plugins/            # jQuery 插件
│   │   │   │   ├── jquery.fitvids.js              # 响应式视频
│   │   │   │   ├── jquery.greedy-navigation.js    # 响应式导航
│   │   │   │   ├── jquery.magnific-popup.js       # 弹出图库
│   │   │   │   └── jquery.smooth-scroll.min.js    # 平滑滚动
│   │   │   └── vendor/             # 第三方库
│   │   │       └── jquery/         # jQuery 库
│   │   │
│   │   └── fonts/                  # 字体文件（FontAwesome 等）
│   │
│   └── images/                     # 图像资源
│       ├── android-chrome-192x192.png    # 应用图标（192px）
│       ├── android-chrome-512x512.png    # 应用图标（512px）
│       ├── apple-touch-icon.png         # iOS 收藏夹图标
│       ├── favicon-16x16.png            # 浏览器标签图标（16px）
│       ├── favicon-32x32.png            # 浏览器标签图标（32px）
│       ├── favicon.ico                  # 传统 favicon
│       └── site.webmanifest             # PWA 应用清单
│
├── 📁 自动化层
│   ├── .github/
│   │   ├── workflows/              # GitHub Actions 工作流
│   │   │   └── [GitHub Actions 配置] # 自动更新 Google Scholar 统计
│   │   └── FUNDING.yml             # 赞助配置
│   │
│   └── google_scholar_crawler/     # Google Scholar 爬虫
│       ├── main.py                 # Python 爬虫脚本
│       └── requirements.txt        # Python 依赖
│
└── 📁 文档和辅助
    └── docs/
        └── README-zh.md            # 中文文档
```

---

## 🔧 关键配置文件详解

### 1. `_config.yml` - 主配置文件

**站点元数据**:
- `title`: "Tianxiang Chen" - 网站标题
- `description`: "Chem is Try" - 网站描述
- `repository`: "tianxiangchen1993/tianxiangchen1993.github.io" - 仓库信息

**作者信息** (`author` 部分):
- `name`: "Tianxiang Chen（陈天翔）"
- `avatar`: "images/android-chrome-512x512.png" - 头像
- `location`: "Hong Kong, China"
- `email`: "tianxiangchen1993@gmail.com"
- 社交链接:
  - Google Scholar: https://scholar.google.com/citations?user=_Gdrw7UAAAAJ
  - ORCID: https://orcid.org/0000-0002-1578-0957
  - ResearchGate: https://www.researchgate.net/profile/Tianxiang-Chen-9

**功能配置**:
- `google_scholar_stats_use_cdn`: true - 使用 CDN 加速 Google Scholar 统计
- SEO 相关配置（Google/Bing/Baidu 验证码）
- Google Analytics 配置位置

**文件包含/排除**:
- 包含: `.htaccess`, `_pages`, `files`
- 排除: `docs`, `google_scholar_crawler`, `node_modules` 等开发文件

---

## 📄 内容层解析

### 主页内容 (`_pages/about.md`)

**YAML Front Matter**（页面配置）:
```yaml
permalink: /           # 根路径（主页）
title: ""              # 页面标题（空）
author_profile: true   # 显示作者个人信息卡片
redirect_from:         # 重定向别名
  - /about/
  - /about.html
```

**页面内容**:
- **简介**: 研究助理教授职位、研究方向（金属簇、催化剂等）
- **引用统计**: 集成 Google Scholar 引用数（1100+）
- **教育背景**: PhD → M.E. → B.S.（4个教育经历）
- **工作经验**: 5个职位记录（从研究助理 → 助理教授）

---

## 🎨 样式系统

### SCSS 架构

**分层设计**:
1. **基础层** (`_variables.scss`, `_reset.scss`): 全局变量、重置默认样式
2. **组件层** (`_buttons.scss`, `_forms.scss`, `_tables.scss`): UI 组件样式
3. **布局层** (`_page.scss`, `_sidebar.scss`, `_masthead.scss`): 页面布局
4. **响应式** (`breakpoint` 库): 不同屏幕尺寸适配
5. **第三方** (`font-awesome/`, `magnific-popup/`, `susy/`): 外部库集成

### 技术栈
- **格栅系统**: Susy（响应式栅格）
- **响应式**: Breakpoint（媒体查询）
- **图标**: FontAwesome（4000+ 图标）
- **弹窗**: Magnific Popup（图片库）

---

## 🌐 交互功能

### JavaScript 模块

| 文件 | 功能 |
|------|------|
| `jquery.smooth-scroll.min.js` | 锚点平滑滚动 |
| `jquery.greedy-navigation.js` | 响应式导航菜单 |
| `jquery.fitvids.js` | 响应式视频 |
| `jquery.magnific-popup.js` | 图片弹窗/灯箱效果 |
| `stickyfill.min.js` | CSS Sticky 兼容性补丁 |
| `collapse.js` | 折叠/展开交互 |

---

## 🔄 自动化工作流

### GitHub Actions 集成

**目的**: 自动更新 Google Scholar 引用统计

**流程**:
1. 触发条件: 代码推送 + 每天 UTC 08:00
2. 执行: `google_scholar_crawler/main.py`（爬取 Google Scholar 数据）
3. 输出: `gs_data.json` 到 `google-scholar-stats` 分支
4. 部署: CDN 加速访问统计数据

**配置位置**: `.github/workflows/` 目录

---

## 📱 响应式设计特点

**断点**（使用 Breakpoint 库）:
- 移动端: < 600px
- 平板: 600px ~ 1024px  
- 桌面: > 1024px

**自适应元素**:
- 导航菜单（汉堡菜单）
- 侧边栏（隐藏/显示）
- 文章布局（单栏/双栏）

---

## 🔍 SEO 优化

**配置项**:
1. **元标签**: `seo.html`（OG、Twitter Card 等）
2. **搜索验证**: Google/Bing/Baidu 站点验证
3. **网站地图**: `jekyll-sitemap` 插件自动生成
4. **RSS**: `jekyll-feed` 插件

**关键数据**:
- 标题、描述、作者信息
- 学术成就数据（论文、引用等）

---

## 🚀 部署和运行

### 本地开发

```bash
# 依赖安装
bundle install

# 本地预览（带自动刷新）
./run_server.sh
# 或
bundle exec jekyll serve -l

# 访问地址
http://localhost:4000
```

### 生产部署

- **部署方式**: GitHub Pages（自动）
- **编译**: Jekyll 自动编译 SCSS → CSS
- **CDN**: jsDelivr（Google Scholar 统计数据）

---

## 📊 关键数据流

```
编辑 about.md (Markdown)
        ↓
Jekyll 编译
        ↓
Liquid 模板渲染（_layouts, _includes）
        ↓
SCSS 编译为 CSS
        ↓
静态 HTML 生成
        ↓
GitHub Pages 部署
        ↓
访问者浏览网站
        ↓
JavaScript 增强交互
```

---

## 📦 依赖管理

### Ruby Gems（Gemfile）
- `github-pages`: GitHub Pages 官方 Jekyll 环境
- `jekyll-feed`: RSS Feed 生成
- `jekyll-sitemap`: 网站地图生成
- `hawkins`: 本地开发 LiveReload
- `wdm`: Windows 文件监听（Windows 专用）

### JavaScript 库
- jQuery 1.12.4
- Magnific Popup（灯箱效果）
- Breakpoint（响应式库）
- Susy（栅格系统）

### 图标库
- FontAwesome（社交、学术图标）
- Academicons（学术指标图标）

---

## 🎯 优化建议

### 现状优势
✅ 自动更新 Google Scholar 统计  
✅ 完整的学术信息展示  
✅ 响应式设计适配所有设备  
✅ SEO 优化完善  
✅ GitHub Pages 零成本部署  

### 可优化方向
1. **性能**: 考虑压缩图片（现有图标可优化）
2. **功能**: 可添加发布日期、分类标签
3. **设计**: 可加入动画效果（已有基础）
4. **内容**: 定期更新发布信息

---

## 📞 核心联系方式

| 渠道 | 链接/信息 |
|------|---------|
| 📧 Email | tianxiangchen1993@gmail.com |
| 🎓 Google Scholar | https://scholar.google.com/citations?user=_Gdrw7UAAAAJ |
| 🔗 ORCID | https://orcid.org/0000-0002-1578-0957 |
| 📱 ResearchGate | https://www.researchgate.net/profile/Tianxiang-Chen-9 |

---

**生成时间**: 2025年12月13日  
**分析类型**: 完整项目架构分析

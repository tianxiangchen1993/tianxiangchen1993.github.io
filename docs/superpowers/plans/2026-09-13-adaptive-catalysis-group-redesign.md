# Adaptive Catalysis Group Website Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the current single-page personal site into a seven-page Adaptive Catalysis Group website and update the publication list to the 50 records supplied in `citations(2).csv`.

**Architecture:** Keep the current Jekyll/Academic Pages framework. Reuse `_pages/about.md` as the home page, create six focused pages, update `_data/navigation.yml` and `_config.yml`, and keep Markdown as the primary content source. Publications are reorganized into a dedicated page while the home page shows only selected recent work.

**Tech Stack:** Jekyll, Kramdown/GFM Markdown, Academic Pages theme, YAML configuration, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-09-13-adaptive-catalysis-group-redesign.md`

## Global Constraints

- Group name: **Adaptive Catalysis Group**.
- Tagline: **Revealing and controlling dynamic catalyst evolution through atomically precise design and operando structural characterization.**
- Primary audiences: academic peers, collaborators, grant reviewers, hiring/promotion committees, while supporting prospective students and researchers.
- Dynamic catalyst restructuring and catalyst evolution are the scientific identity. Synchrotron methods are enabling tools, not the brand itself.
- Preserve verified biographical, team, funding, and publication information.
- Keep the first release compatible with the existing Jekyll theme and avoid unnecessary CSS/layout changes.
- Keep English scientific prose concise and avoid semicolons.

---

### Task 1: Site identity and navigation

**Files:**
- Modify: `_config.yml`
- Modify: `_data/navigation.yml`

**Produces:** Seven top-level routes: Home, Research, People, Publications, Funding, PI, Join Us.

- [ ] Replace the generic site title/description with Adaptive Catalysis Group branding.
- [ ] Populate useful author-profile fields such as employer, GitHub username, and a concise research bio without changing verified external profile URLs.
- [ ] Replace anchor-based CV navigation with page-based navigation.
- [ ] Verify all navigation URLs correspond to real permalinks.

### Task 2: Home page

**Files:**
- Modify: `_pages/about.md`

**Produces:** `/`

- [ ] Replace the long CV-style page with a group landing page.
- [ ] Include group identity, tagline, mission, three research themes, selected recent publications, team snapshot, funding snapshot, news, and recruitment call-to-action.
- [ ] Keep personal career history off the home page.
- [ ] Keep the existing redirect aliases `/about/` and `/about.html`.

### Task 3: Research and People pages

**Files:**
- Create: `_pages/research.md`
- Create: `_pages/people.md`

**Produces:** `/research/`, `/people/`

- [ ] Research page: explain adaptive catalysis, dynamic restructuring, atomically precise multinuclear sites, and operando/multimodal structural characterization.
- [ ] People page: list PI, postdoctoral researchers, PhD students, research assistants, co-supervision, and DYBRI bases where supplied.
- [ ] Record Dr. Jiawei Zhao as an alumnus/former short-term research fellow now at Northwestern Polytechnical University.

### Task 4: Publications page from the supplied CSV

**Files:**
- Create: `_pages/publications.md`

**Produces:** `/publications/`

- [ ] Use the 50 CSV records as the publication source of truth for titles, authors, journals, years, volumes, issues, and pages/article numbers.
- [ ] Retain known first/co-first/corresponding-author markers from the existing homepage where the CSV does not encode contribution roles.
- [ ] Keep the verified count of 19 first/co-first/corresponding-author papers unless evidence in supplied material supports a change.
- [ ] Organize publications into `First, Co-first & Corresponding Author Papers` and `Collaborative Publications`, then sort newest to oldest within each section.
- [ ] Update the total publication count to 50.

### Task 5: Funding and PI pages

**Files:**
- Create: `_pages/funding.md`
- Create: `_pages/pi.md`

**Produces:** `/funding/`, `/pi/`

- [ ] Funding page: show NSFC Young Scientists Fund (Category C), Presidential Global Impact Postdoctoral Fellowship Scheme, and PolyU Start-up Fund using proper Markdown list syntax.
- [ ] PI page: migrate current work experience, education, awards, invited talks, academic meetings, research achievements, and expertise from the old home page.
- [ ] Remove outdated CV wording such as `Post-doc Research Fellow ... present` from public-facing page content.

### Task 6: Join Us page

**Files:**
- Create: `_pages/join-us.md`

**Produces:** `/join-us/`

- [ ] State the research themes and profiles of prospective PhD students, postdocs, RAs, and collaborators who would fit the group.
- [ ] Give a concise application instruction using the public contact details already configured for the site.
- [ ] Avoid promising currently unverified funded vacancies.

### Task 7: Validation

**Files:** all changed pages and configuration files.

- [ ] Confirm every page has valid YAML front matter and a unique permalink.
- [ ] Confirm every navigation URL resolves to a created page.
- [ ] Confirm the home page no longer contains the full 50-paper list.
- [ ] Confirm Publications contains 50 unique records from the CSV.
- [ ] Confirm `Our Team` data matches the requested Zeng Binwen, Lei Xie, Feixuan Li, Wan Zhang, and current postdocs.
- [ ] Confirm Zheng Zhou is absent from News.
- [ ] Confirm Dr. Jiawei Zhao's departure is acknowledged and his current Northwestern Polytechnical University position is stated.
- [ ] Confirm Funding uses standard Markdown bullets and includes NSFC Category C, RMB 300,000.
- [ ] Compare the redesign branch with `main` and review all changed files before opening a pull request.

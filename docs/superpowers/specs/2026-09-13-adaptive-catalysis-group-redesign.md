# Adaptive Catalysis Group Website Redesign Specification

Date: 2026-09-13

## Goal

Transform the current single-page personal academic profile into a multi-page research-group website for the **Adaptive Catalysis Group**, led by Tianxiang Chen at The Hong Kong Polytechnic University.

Primary research identity:

> **Revealing and controlling dynamic catalyst evolution through atomically precise design and operando structural characterization.**

Primary audiences are academic peers, potential collaborators, grant reviewers, hiring and promotion committees, while still supporting prospective PhD students, postdoctoral researchers, and research assistants.

## Design Principles

1. Present the site as an independent PI research-group website rather than a long-form CV.
2. Put scientific identity and current research questions before career history.
3. Emphasize dynamic catalyst restructuring, active-site evolution, nuclearity changes, migration, coordination changes, host–guest response, and operando structural characterization.
4. Present synchrotron XRD, PDF, XAS, EPR, Raman, and related methods as tools for answering scientific questions rather than as the group identity itself.
5. Keep the current Jekyll and Academic Pages framework for the first release to minimize deployment risk.
6. Preserve existing verified publication, funding, award, education, and employment information unless explicitly updated.
7. Separate group-level information from PI-level biography.
8. Keep content easy to maintain directly in Markdown.

## Information Architecture

### 1. Home

Path: `/`

Purpose: concise landing page that immediately communicates group identity, research focus, current team, selected outputs, funding, and recruitment.

Sections:

- Adaptive Catalysis Group title
- Core tagline
- Short group mission statement
- Three research themes
- Selected recent publications
- Current team snapshot
- Selected funding
- Latest news
- Join Us call to action

The homepage will no longer contain the full PI education, work history, conference list, invited talks, or complete publication list.

### 2. Research

Path: `/research/`

Purpose: explain the scientific questions that define the group.

Initial research themes:

1. **Dynamic Active-Site Reconstruction**
   - Reaction-condition-dependent restructuring
   - Nuclearity evolution
   - Metal migration and aggregation
   - Reversible and irreversible structural changes

2. **Atomically Precise Catalytic Architectures**
   - Single and multinuclear metal sites
   - Zeolite-confined clusters and ensembles
   - Ligand-mediated and modular assembly strategies
   - Control of geometric and electronic structure

3. **Operando Structure–Function Relationships**
   - Operando and in situ XRD
   - Pair distribution function analysis
   - XAS
   - EPR and vibrational spectroscopy where relevant
   - Correlation of structural dynamics with catalytic function

Research text should distinguish scientific goals from characterization methods.

### 3. People

Path: `/people/`

Purpose: provide a stable group roster independent of News.

Initial categories:

- Principal Investigator
- Postdoctoral Research Fellows
- PhD Students
- Research Assistants
- Alumni

Current members to include:

- Dr. Tianxiang Chen, Principal Investigator
- Dr. Liu Biyuan, Postdoctoral Research Fellow
- Dr. Lingfeng Jia, Postdoctoral Research Fellow
- Dr. Xuezhen Feng, Postdoctoral Research Fellow
- Mr. Binwen Zeng, PhD Student, co-supervised with Prof. Tsz Woon Benedict Lo
- Ms. Lei Xie, first-year PhD Student, co-supervised with Prof. Ka-fu Joseph Yung
- Ms. Wan Zhang, Research Assistant, based at DYBRI
- Mr. Feixuan Li, Research Assistant, based at DYBRI

Alumni:

- Dr. Jiawei Zhao, former short-term Research Fellow, now Professor at Northwestern Polytechnical University

The alumni entry should acknowledge his contribution to the group in a concise professional form.

### 4. Publications

Path: `/publications/`

Purpose: move the complete publication record away from the homepage while preserving it as a durable scholarly record.

Structure:

- Selected publications
- First, co-first, and corresponding-author papers
- Collaborative publications

The current publication data in `_pages/about.md` will be preserved unless a bibliographic correction is explicitly required.

### 5. Funding

Path: `/funding/`

Purpose: present independent and collaborative funding clearly.

Current entries:

- National Natural Science Foundation of China Young Scientists Fund, Category C, PI, 2027–2030, RMB 300,000
- Presidential Global Impact Postdoctoral Fellowship Scheme, Co-PI, 2027–2030, HKD 1,580,000
- PolyU Start-up Fund, PI, 2025–2027, HKD 300,000

Formatting will use standard Markdown lists or a compact table rather than `--` prefixes.

Beamtime may remain on the same page initially under a separate subsection only if current content is available and useful. Otherwise, the navigation label will be `Funding` rather than `Funding and Beamtime`.

### 6. PI

Path: `/pi/`

Purpose: contain Tianxiang Chen's individual academic profile without dominating the group homepage.

Content:

- Short biography
- Research focus
- Work experience
- Education
- Honors and awards
- Invited talks
- Selected academic meetings if still useful
- Links to Google Scholar, ORCID, ResearchGate, and email

The outdated `CV.md` should either be updated to match the current RAP position and publication record or removed from public navigation until updated.

### 7. Join Us

Path: `/join-us/`

Purpose: provide a professional recruitment page for prospective PhD students, postdoctoral researchers, research assistants, and collaborators.

Initial content:

- Scientific interests sought
- Expected researcher qualities
- Typical project areas
- Application materials
- Contact route

The first release should avoid promising open funded positions unless explicitly confirmed.

## Navigation

Replace the current CV-style anchor navigation with:

- Home
- Research
- People
- Publications
- Funding
- PI
- Join Us

Remove the following from the top-level navigation:

- Work Experience
- Education
- Research Achievements
- Invited Talks
- Academic Meetings
- Honors and Awards
- Expertise

These remain available within the PI or Research pages where appropriate.

## Site Identity and Configuration

Update `_config.yml`:

- Site title: `Adaptive Catalysis Group`
- Description: concise group research identity rather than `Chem is Try`
- Author remains Tianxiang Chen
- Add employer: `The Hong Kong Polytechnic University`
- Add GitHub username if useful
- Preserve Google Scholar, ORCID, ResearchGate, and email links

Recommended description:

> Revealing and controlling dynamic catalyst evolution through atomically precise design and operando structural characterization.

## News

Keep a News section on the homepage, but use it for genuinely time-sensitive group developments rather than as a substitute for the People page.

Current September 2026 updates should include:

- Binwen Zeng joining as a PhD student
- Lei Xie joining as a first-year PhD student
- Feixuan Li joining as a Research Assistant based at DYBRI
- Jiawei Zhao moving to Northwestern Polytechnical University as a Professor, with a brief acknowledgement of his contribution

Keep Wan Zhang's June 2026 entry with DYBRI base.

Do not restore the removed Zheng Zhou news entry.

## Technical Scope for First Release

Files expected to change:

- `_data/navigation.yml`
- `_config.yml`
- `_pages/about.md`
- new `_pages/research.md`
- new `_pages/people.md`
- new `_pages/publications.md`
- new `_pages/funding.md`
- new `_pages/pi.md`
- new `_pages/join-us.md`
- `CV.md`, if retained

The first release will not redesign the Jekyll layout engine or theme CSS. Visual styling can be handled as a second phase after the information architecture is stable.

## Known Issues to Fix

1. The current navigation points to `/#invited-talks` while the existing page anchor uses `Invited-Talks`. This mismatch becomes irrelevant once Invited Talks moves to the PI page, but no broken anchor should remain.
2. `Our Team` currently exists on the homepage but is absent from the old top navigation. The new People page supersedes this issue.
3. Research grant entries currently use `--` prefixes. Replace with valid Markdown list or table syntax.
4. `CV.md` contains outdated employment status and publication counts. It must not contradict the current PI page.
5. `_config.yml` currently uses `Chem is Try` as the site description and leaves employer and bio blank. These should be updated.
6. The Google Scholar crawler workflow uses an old `actions/checkout@v2`. Workflow modernization can be handled as a separate maintenance task after the content redesign.

## Validation Criteria

The redesign is successful when:

1. Every top navigation item resolves to a valid page.
2. The homepage communicates group identity within the first screen of content.
3. Full CV-style material no longer dominates the homepage.
4. Current team members appear on a dedicated People page.
5. Publications and funding each have dedicated pages.
6. PI biography and career history are separated from group-level content.
7. No outdated `Post-doc Research Fellow, Oct. 2022 - present` statement remains in publicly linked content.
8. The group name and tagline are consistent across the homepage, navigation, and site configuration.
9. The existing GitHub Pages/Jekyll build structure remains intact.
10. Changes are implemented on the `adaptive-catalysis-group-redesign` branch before any merge to `main`.

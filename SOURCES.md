# Bronnen en selectie

Deze bundel bestaat uit eigen, compacte instructies **geïnspireerd** op de volgende repositories. Het is geen kopie van hun volledige plugins, tooling, templates, licenties of hooks. Voor uitgebreide audits en CLI-functionaliteit gebruik je de originele projecten.

| Bron | Relevante principes | HBS |
|---|---|---|
| [Ponytail](https://github.com/DietrichGebert/ponytail) | AGENTS.md, SKILL.md, YAGNI, hergebruik | lean-code, AGENTS |
| [Impeccable](https://github.com/pbakaus/impeccable) | Visuele hiërarchie, UI-audits en polish | beautiful-html |
| [Addy Osmani Skills](https://github.com/addyosmani/agent-skills) | Frontend, security, CI/CD en review | beautiful-html, security-first, clean-deployment |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | diagnosing-bugs, testfeedback | debug-verify |
| [Cloudflare security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Trust boundaries, geverifieerde securitybevindingen | security-first |
| [Superpowers](https://github.com/obra/superpowers) | Spec, tests, review, gefaseerde uitvoering | debug-verify |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | Rustige hoogwaardige HTML/SVG-schema's | visual-diagrams |
| [I Have ADHD](https://github.com/ayghri/i-have-adhd) | Actiegericht en compact communiceren | AGENTS |
| [Humanizer](https://github.com/blader/humanizer) | Natuurlijke teksten en minder filler | AGENTS |
| [Justinmind: dashboard design](https://www.justinmind.com/ui-design/dashboard-design-best-practices-ux) | Layout, F/Z-hiërarchie, relevantie, dataweergave, filters | dashboard-storytelling |
| [NN/g: chart types](https://www.nngroup.com/articles/choosing-chart-types/) | Context, contrast, beperken van ruis | dashboard-storytelling |
| [NN/g: data tables](https://www.nngroup.com/articles/data-tables/) | Filterbaarheid, vergelijkbaarheid, exacte waarden | dashboard-storytelling |

[Graphify](https://github.com/Graphify-Labs/graphify) bewust niet standaard: nuttig bij grote codebases, maar extra Python-tooling zou het systeem voor kleine projecten onnodig verzwaren.

Controleer upstream-documentatie bij integratie van code, extra dependencies of daadwerkelijke plugins. Markdown-instructies alléén installeren geen runtime-tools.

## Aanvullende bronnen: selectieve integratie

| Bron | Relevante principes | HBS |
|---|---|---|
| [Claude Vibe Skills](https://github.com/darthrater78/claude-vibe-skills) | DESIGN_REFERENCE, SECURITY_WINDOWS, SECURITY_ANDROID, SECURITY_GATE, QUALITY_REFERENCE en releasecontrole | beautiful-html, security-first, debug-verify, clean-deployment |
| [Google Labs DESIGN.md](https://github.com/google-labs-code/design.md) | Productgebonden design-tokens (alpha-formaat) | templates/DESIGN.template.md |

Niet overgenomen: verplichte zes-gates-procedure voor elke commit, automatische uitvoerbare Python-hooks, verplichte certificate pinning of generieke platformrestrictions. De controles zijn proportioneel naar project en risico.

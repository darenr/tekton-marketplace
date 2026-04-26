---
name: company-evaluator
description:  >-
    Produces an early-stage VC investment memo with founder diligence, investor signal analysis, market research, and competitive positioning. Use when a user asks to evaluate a startup, prepare an investment memo, assess founder-market fit, compare startup competitors, or diligence a company from a URL/pitch deck. Do not use for public-market stock analysis, personal financial advice, or legal counsel.
metadata:
    author: Tekton
    version: 1.1.6
    category: venture-capital
---

# Company Evaluator Skill

## What this skill produces

An Investor Memo — a comprehensive document that synthesizes research on the founders, investors, market, and competitive landscape to provide a clear recommendation on whether to pursue an investment opportunity.

## Trigger conditions

Use this skill when users ask for company evaluation or diligence, including phrasing like:
- "evaluate this company"
- "write an investment memo"
- "analyze this startup"
- "how strong is this founding team"
- "compare this startup to competitors"

Do not use this skill for:
- Public equity or options analysis
- Personal investing advice
- Legal advice or contract interpretation as legal counsel

## Operating principles

- Request from the user as much context as possible, including URLs, pitch decks, and specific questions they want answered, they should provide a pitch deck, website, or other materials to review. If they do not provide sufficient information, ask follow-up questions to gather more context before proceeding.
- Be specific and evidence-driven. Every external claim must include a source.
- State uncertainty explicitly. If data is missing, add it to Due Diligence Items.
- Prefer clear, plain language for partners who may be new to the market.
- Use progressive disclosure: keep core instructions here, and put deep references in `references/` as this skill evolves.
- When evaluating a company's ability to win, systematically assess technology, incumbents vs. new entrants, and positioning/focus, as well as the founding team and the fundability or financial strength of its competitors.
- The output format should be a Microsoft Word document structured as an investor memo, with sections for each area of analysis and a final recommendation. 


---
name: company-evaluator-plugin
description:  >-
    Produces an early-stage VC investment memo with founder diligence, investor signal analysis, market research, and competitive positioning. Use when a user asks to evaluate a startup, prepare an investment memo, assess founder-market fit, compare startup competitors, or diligence a company from a URL/pitch deck. 
metadata:
    author: Tekton
    version: 1.1.0
    category: venture-capital
---

# Company Evaluator Skill

## What this skill produces

An Investor Memo — a comprehensive document that synthesizes research on the founders, investors, market, and competitive landscape to provide a clear recommendation on whether to pursue an investment opportunity.

## Trigger conditions

Use this skill when users ask for company evaluation or diligence, including phrasing like:
- "evaluate this company"
- "write an investment memo"
- "analyze this startup"
- "how strong is this founding team"
- "compare this startup to competitors"


## Operating principles

- Be specific and evidence-driven. Every external claim must include a source.
- State uncertainty explicitly. If data is missing, add it to Due Diligence Items.
- Prefer clear, plain language for partners who may be new to the market.
- Use progressive disclosure: keep core instructions here, and put deep references in `references/` as this skill evolves.

## Workflow phases

### Phase 1: Information Gathering

When the user triggers this skill with a company name and URL, you must:

1. Acknowledge the company and URL.
2. Request inputs:
    - Pitch deck or slide deck (if available)
    - Written call notes or meeting transcripts
    - Other relevant materials (financials, cap tables, term sheets)
    - Specific deep-dive priority (for example: technical moat, founder-market fit, competition)
    - Whether the deal is in-thesis or an adjacent/new market for the fund

If the user has no files, proceed with URL-only research and explicitly mark confidence as lower.

### Phase 2: Founder and Team Deep Dive

Research each founder and key executive individually. Use web search

For each founder (explicitly including the CEO, Co-Founders, and CTO), include:

1. Career arc: roles, companies, scope of responsibility
2. Prior outcomes: IPO/acquisition/shutdown/still operating
3. Exit context: acquirer, timing, reported value if public
4. Domain tenure: years in this market
5. Technical/functional edge: patents, papers, OSS, specialist credentials
6. Network/reputation: board roles, advisor roles, relevant visibility
7. Team composition: key hires, critical gaps for current stage

Use these sources for founder research:  Use web search

| Objective | Target Sources |
| :--- | :--- |
| Career and exits | LinkedIn, Crunchbase (People), PitchBook, press archives |
| Patents and research | Google Patents, USPTO, Google Scholar, arXiv |
| Reputation and network | Conference talks, podcasts, The Org, Twitter/X |

### Phase 3: Investor and Backing Signal Analysis

Assess who invested in the current startup and in founders' prior companies. Use web search

1. Current cap table snapshot (if available): lead, co-investors, angels
2. Prior investor overlap: identify repeat backers
3. Investor quality scoring:
    - Tier (top-tier, mid-tier, emerging, angels)
    - Domain relevance
    - Notable portfolio outcomes
    - Value-add reputation
4. Signal stacking:
    - Strong signal
    - Moderate signal
    - Mixed signal
    - Weak signal

Use these sources for investor research:

| Objective | Target Sources |
| :--- | :--- |
| Funding rounds and cap table | PitchBook, Crunchbase, Dealroom, SEC EDGAR (Form D) |
| Investor track record | PitchBook profiles, Crunchbase, Midas/Forbes VC rankings |
| Repeat backers | Cross-reference founder prior ventures vs. current cap table |

### Phase 4: Market and Competitive Landscape

This section should educate generalist partners quickly.

- Market primer: problem, buyer, existing alternatives, identify other companies in this space and provide a comparison
- Market sizing: TAM/SAM/SOM with transparent methodology
- Timing/tailwinds: regulatory, technical, behavioral catalysts
- Competitive matrix: startup vs. top competitors, including segmentation by type, incumbents vs.    startups, and funding history
- Synthetic Comparison: Differentiate between incumbents (slower, resource-heavy) and startup peers (faster, agile).
- Moat Assessment: Rate IP, network effects, switching costs, and regulatory barriers.
- Bear Case Analysis: Identify the existential risks (regulatory, technical, or market-timing).


Use these sources for market research:

| Objective | Target Sources |
| :--- | :--- |
| Market size | Statista, Gartner, Grand View Research, sector reports |
| Competition | G2, Capterra, Crunchbase competitors, CB Insights |
| Product sentiment | G2, Capterra, Product Hunt, Reddit, Hacker News |
| Traction proxies | SimilarWeb, LinkedIn headcount trends, app-store rank |

### Phase 5: Document Review and Synthesis

1. Compare pitch claims against independent research
2. Label each major claim: confirmed, partially supported, contradicted
3. Build a first-draft memo framework
4. Claim Mapping: Tag major pitch claims as [Confirmed], [Partially Supported], or [Contradicted].
5. DD Prioritization: Move critical missing data points to the top of the memo.

### Phase 6: Guidance and Weighting

Before finalizing, ask:

- Which sections should be weighted most heavily?
- Which sections are lower priority for this deal?
- Which red flags should be explicitly stress-tested?
- Are there any specific competitive companies to consider

### Phase 7: Final Memo

Produce the final memo using the output format below as a Word document.

## Examples

Example 1: URL-only diligence

- User says: "Evaluate https://example.com for a seed investment"
- Actions:
    1. Run web research across founders, investors, market, and competitors
    2. Build memo with explicit low-confidence flags where private data is unavailable
    3. Provide recommendation plus Due Diligence Items

Example 2: Deck plus call notes

- User says: "Use this deck and notes to draft an investment memo"
- Actions:
    1. Extract claims from provided materials
    2. Validate claims externally
    3. Produce memo with claim-vs-evidence and recommendation

## Troubleshooting

### Skill appears under-triggered

Cause: User phrasing does not match trigger language.
Fix: Ask one clarifying question and map intent to this workflow if they want diligence or an investment memo.

### Missing hard metrics (revenue, valuation, retention)

Cause: Early-stage private data is not public.
Fix: Do not guess. Add a Due Diligence Item and continue with available signal-based assessment.

### Conflicting sources

Cause: Databases and press may disagree.
Fix: Note discrepancy, prioritize primary/most recent source, and include confidence notes.

## Output format

```
# [Company Name] — Investment Memo
**Date:** [Date]
**Stage:** [Pre-Seed / Seed / Series A]
**Sector:** [Category]
**Prepared by:** AI Research Assistant
## Executive Summary
[BLUF: 3–5 sentence summary of the company, the opportunity, and the recommendation.
Include the Signal Strength rating here: Strong / Moderate / Weak / Mixed.]

## Founders & Team
### Founder Profiles
[For each founder, explicitly including the CEO, Co-Founders, and CTO: career arc, prior exits (with outcomes), domain tenure, technical edge, network.]
### Team Assessment
[Key hires, gaps, overall team strength for this stage.]
### Founder Signal
[Repeat founder? Favorable exits? Domain expert or new to sector?]

## Investor & Backing Signal
### Current Investors
[Known investors, lead, round size, valuation if known.]
### Prior Backing of Founders
[Who invested in the founders' previous companies? Are any re-investing?]
### Investor Reputation Assessment
[Tier and domain relevance of key investors. Notable hits from their portfolios.]
### Signal Stacking Summary
[Composite: Strong / Moderate / Weak / Mixed — with rationale.]

## Market Opportunity
### Market Primer
[Plain-language explanation of the space for non-domain-experts.]
### Market Size
[TAM / SAM / SOM with sources and methodology.]
### Tailwinds & Timing
[Why now? Specific catalysts.]

## Competitive Landscape
### Positioning Matrix
[Detailed competitive matrix: include segmentation by type, compare incumbents vs. startups, and list funding/capitalization for competitors.]
### Moat Assessment
[IP, network effects, switching costs, data advantage, regulatory moat. Overall rating.]

## Technology & Product
[What they build and how it works. Do not focus on stack details. Instead, answer: Is it hard to build? Is it differentiated and defensible? Does the technical approach make sense?]

## Traction & Business Model
[Revenue model, pricing, key metrics, evidence of product-market fit.]

## Financials & Metrics
[Extract summary financial plan and known financial metrics. If unavailable, flag as DD Item.]

## Risks & Mitigations
[Honest assessment. For each risk, note severity (High/Medium/Low) and any known mitigation.]

## Due Diligence Items
[Consolidated list of all unanswered questions and missing data to raise with founders.]

## Recommendation
[`Strong Fit`, `Possible Fit`, or `Not a Fit` with a 3–5 sentence rationale.
Include 2–3 specific questions for the partnership to discuss.]
```

If information is missing, state assumptions clearly and add the gap to the Due Diligence Items section.

## Quality Checklist

Before finalizing the memo, ensure:
- All claims are supported by evidence with sources cited.
- Uncertainties and data gaps are clearly noted.
- The memo is structured logically with clear sections.
- Language is clear and accessible to non-experts.
- The recommendation is clearly stated and justified by the analysis.


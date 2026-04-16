---
name: company-evaluator-plugin
description:  >-
    Produces an early-stage VC investment memo with founder diligence, investor signal analysis, market research, and competitive positioning. Use when a user asks to evaluate a startup, prepare an investment memo, assess founder-market fit, compare startup competitors, or diligence a company from a URL/pitch deck. Do not use for public-market stock analysis, personal financial advice, or legal counsel.
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

Do not use this skill for:
- Public equity or options analysis
- Personal investing advice
- Legal advice or contract interpretation as legal counsel

## Operating principles

- Be specific and evidence-driven. Every external claim must include a source.
- State uncertainty explicitly. If data is missing, add it to Due Diligence Items.
- Prefer clear, plain language for partners who may be new to the market.
- Use progressive disclosure: keep core instructions here, and put deep references in `references/` as this skill evolves.

## Comprehensive Diligence Framework

When evaluating a company's ability to win, systematically assess the following areas, focusing on technology, incumbents vs. new entrants, and positioning/focus:

### 1) Technology & Product Competition
**Core Technical Advantage**
- What is technically unique about this product vs. competitors?
- Is the differentiation real (architecture-level) or surface-level (UX, packaging)?
- Could a strong engineering team replicate this in 6–12 months?
- What parts of the system are hardest to copy?

**Architecture & Stack**
- How does the company’s architecture differ from competitors?
- Are competitors using fundamentally different approaches (e.g., rules-based vs. AI-native)?
- Is the technology proprietary in any way? Is it protected or protectable via patents?
- Is the product dependent on third-party platforms (e.g., OpenAI, AWS, Google, etc.)?
- Does reliance on third parties create vulnerability or speed advantage?

**Team Advantage**
- Does the company’s technical team have unique experience, expertise or combination of expertise that gives it a competitive advantage?
- Does the company’s founding team have unique experience, or domain knowledge that provides them with superior insights to drive the market winning product or solution?

**Data Advantage**
- Does the company have proprietary data competitors do not?
- How is data collected, cleaned, and enriched vs. competitors?
- Does the product improve with scale (data flywheel)?
- Are competitors able to access similar datasets?

**Performance & Scalability**
- How does performance (speed, accuracy, reliability) compare?
- What happens at enterprise scale vs. competitors?
- Are there bottlenecks (i.e. latency, cost, compute)?

**Cost Structure (Tech-Driven)**
- Is the product structurally cheaper to operate than competitors?
- Are competitors subsidizing pricing due to inefficiencies?
- Does cost advantage improve with scale?

**Product Velocity**
- How fast can the company ship vs. competitors?
- Are incumbents slower due to legacy systems?
- Are startups faster but less stable?

### 2) Incumbents (Large / Established Players)
**Identification**
- Who are the dominant incumbents in this space?
- Are they horizontal platforms or vertical specialists?

**Strengths**
- What advantages do incumbents have? (Distribution? Brand trust? Existing customer base? Bundled offerings?)

**Weaknesses**
- Where do incumbents fail customers today?
- Are they constrained by: Legacy architecture? Organizational inertia? Pricing rigidity?

**Likelihood of Response**
- Will incumbents build, buy, or ignore this category?
- What is their historical behavior in similar disruptions?
- How quickly could they respond if this startup gains traction?

**Switching Dynamics**
- How hard is it for customers to switch away from incumbents?
- What integrations or workflows create lock-in?
- Is there a wedge that avoids direct displacement?

**Pricing Power**
- Are incumbents overpriced relative to value?
- Are they cross-subsidizing this product?

### 3) New Entrants / Startups
**Competitive Set**
- Who are the top startup competitors?
- How crowded is the category?
- Are competitors well-funded?

**Differentiation vs. Peers**
- How does this company compare to other startups?
- Are competitors converging toward similar features?
- Is there real differentiation or feature parity?

**Speed & Execution**
- Which competitors are shipping fastest?
- Who is winning early customers?
- Are competitors iterating based on user feedback effectively?

**Fundraising & Resources**
- How much capital have competitors raised?
- Are there "overfunded" players who can outspend?
- Are there undercapitalized but strong technical teams?

**Strategic Positioning**
- Are competitors attacking the same ICP or different segments?
- Are some going upmarket vs. downmarket?

### 4) Market Positioning
**Value Proposition**
- What is the company’s core positioning? Is it: Faster? Cheaper? Better UX? More accurate? More integrated?

**Target Customer**
- Who is the primary ICP?
- How does that differ from competitors’ ICPs?
- Is the company focused or trying to serve too many segments?

**Use Case Focus**
- Is the company solving a narrow wedge problem or broad platform?
- Are competitors more specialized or generalized?
- Is there risk of being a "feature" vs. a "platform"?

**Messaging & Branding**
- Is the positioning clear and compelling?
- Do customers understand why it is different?
- Does messaging resonate vs. competitors?

**Pricing Strategy**
- Is pricing aligned with positioning (premium vs. budget)?
- How does pricing compare to competitors?
- Is pricing a competitive advantage or liability?

### 5) Strategic Focus & Expansion
**Beachhead Strategy**
- What initial wedge is the company using?
- Why is this wedge defensible?

**Expansion Path**
- How does the company plan to expand from initial use case?
- Is expansion logical or forced?

**Platform Potential**
- Can this evolve into a platform?
- Are competitors already platforms?

**Risk of Feature Encroachment**
- Could incumbents easily replicate this as a feature?
- Is the company building something standalone or complementary?

### 6) Competitive Moats & Durability
**Defensibility**
- What prevents competitors from winning long-term?
- Is the moat: Technology? Data? Network effects? Distribution?

**Network Effects**
- Does the product get better with more users?
- Are there two-sided or data network effects?

**Switching Costs**
- How painful is it to switch away?
- Are workflows deeply embedded?
- Is this replacing an incumbent or sitting alongside it?
- Is this a "budget line item" or a "new spend category"?

**Ecosystem & Integrations**
- Is the company part of a broader ecosystem?
- Are integrations a strength or dependency?

### 7) Competitive Risks
- What is the most dangerous competitor and why?
- What happens if a major incumbent prioritizes this space?
- Is this market trending toward winner-take-all or fragmentation?
- Are we underwriting true differentiation or temporary advantage?
- Could this company be out-executed rather than out-innovated?

### Synthesis Questions
These are the decision-driving questions that must be addressed in the final memo:
- Why does this company win vs. incumbents?
- Why does it win vs. other startups?
- Does the team have market-leading, world class technical or domain expertise that provides it with competitive advantage?
- What is the one thing competitors cannot easily replicate?
- What is the biggest competitive threat faced by the company?
- Is this a category-defining company, a category disruptor, or a fast follower?
- In 3–5 years, who controls this market?

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

Research each founder and key executive individually.

For each founder, include:
1. Career arc: roles, companies, scope of responsibility
2. Prior outcomes: IPO/acquisition/shutdown/still operating
3. Exit context: acquirer, timing, reported value if public
4. Domain tenure: years in this market
5. Technical/functional edge: patents, papers, OSS, specialist credentials
6. Network/reputation: board roles, advisor roles, relevant visibility
7. Team composition: key hires, critical gaps for current stage

Use these sources for founder research:

| Objective | Target Sources |
| :--- | :--- |
| Career and exits | LinkedIn, Crunchbase (People), PitchBook, press archives |
| Patents and research | Google Patents, USPTO, Google Scholar, arXiv |
| Reputation and network | Conference talks, podcasts, The Org, Twitter/X |

### Phase 3: Investor and Backing Signal Analysis

Assess who invested in the current startup and in founders' prior companies.

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

1. Market primer: problem, buyer, existing alternatives
2. Market sizing: TAM/SAM/SOM with transparent methodology
3. Timing/tailwinds: regulatory, technical, behavioral catalysts
4. Competitive matrix: startup vs. top 3-5 competitors
5. Moat assessment:
- IP/patents
- Network effects
- Switching costs
- Data advantage
- Regulatory barriers

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

### Phase 6: Guidance and Weighting

Before finalizing, ask:
- Which sections should be weighted most heavily?
- Which sections are lower priority for this deal?
- Which red flags should be explicitly stress-tested?

### Phase 7: Final Memo

Produce the final memo using the output format below.

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
[For each founder: career arc, prior exits (with outcomes), domain tenure, technical edge, network.]
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
[Comparison table: company vs. top 3–5 competitors.]
### Moat Assessment
[IP, network effects, switching costs, data advantage, regulatory moat. Overall rating.]

## Product & Differentiation
[What they build, how it works, what makes it meaningfully different.]

## Traction & Business Model
[Revenue model, pricing, key metrics, evidence of product-market fit.]

## Financials & Metrics
[Known financial data. If unavailable, flag as DD Item.]

## Risks & Mitigations
[Honest assessment. For each risk, note severity (High/Medium/Low) and any known mitigation.]

## Due Diligence Items
[Consolidated list of all unanswered questions and missing data to raise with founders.]

## Recommendation
[`Strong Fit`, `Possible Fit`, or `Not a Fit` with a 3–5 sentence rationale.
Include 2–3 specific questions for the partnership to discuss.]
```

If information is missing, state assumptions clearly and add the gap to the Due Diligence Items section.

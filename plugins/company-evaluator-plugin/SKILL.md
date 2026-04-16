---
name: company-evaluator-plugin
description:  >-
    Produces an early-stage VC investment memo with founder diligence, investor signal analysis, market research, and competitive positioning. Use when a user asks to evaluate a startup, prepare an investment memo, assess founder-market fit, compare startup competitors, or diligence a company from a URL/pitch deck. Do not use for public-market stock analysis, personal financial advice, or legal counsel.
metadata:
    author: Tekton
    version: 1.1.1
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
- When evaluating a company's ability to win, systematically assess the following areas, focusing on technology, incumbents vs. new entrants, and positioning/focus:
- The evaluation should focus on: technology, incumbents vs. new entrants, and positioning/focus. It should also assess the company’s ability to win from the standpoint of its founding team, as well as in the context of the fundability and/or financial strength of its competitors.

## Comprehensive Diligence Framework



 

**1) Technology & Product Competition**

**Core Technical Advantage**

-   What is technically unique about this product vs. competitors?
-   Is the differentiation **real (architecture-level)** or **surface-level (UX, packaging)**?
-   Could a strong engineering team replicate this in 6--12 months?
-   What parts of the system are hardest to copy?

**Architecture & Stack**

-   How does the company's architecture differ from competitors?
-   Are competitors using fundamentally different approaches (e.g., rules-based vs. AI-native)?
-   Is the technology proprietary in any way? Is it protected or protectable via patents?
-   Is the product dependent on third-party platforms (e.g., OpenAI, AWS, Google, etc.)?
-   Does reliance on third parties create vulnerability or speed advantage?

**Team Advantage**

-   Does the company's technical team have unique experience, expertise or combination of expertise that gives it a competitive advantage?
-   Does the company's founding team have unique experience, or domain knowledge that provides them with superior insights to drive the market winning product or solution?

**Data Advantage**

-   Does the company have proprietary data competitors do not?
-   How is data collected, cleaned, and enriched vs. competitors?
-   Does the product improve with scale (data flywheel)?
-   Are competitors able to access similar datasets?

**Performance & Scalability**

-   How does performance (speed, accuracy, reliability) compare?
-   What happens at enterprise scale vs. competitors?
-   Are there bottlenecks (i.e. latency, cost, compute)?

**Cost Structure (Tech-Driven)**

-   Is the product structurally cheaper to operate than competitors?
-   Are competitors subsidizing pricing due to inefficiencies?
-   Does cost advantage improve with scale?

**Product Velocity**

-   How fast can the company ship vs. competitors?
-   Are incumbents slower due to legacy systems?
-   Are startups faster but less stable?

**2) Incumbents (Large / Established Players)**

**Identification**

-   Who are the dominant incumbents in this space?
-   Are they horizontal platforms or vertical specialists?

**Strengths**

-   What advantages do incumbents have?

-   Distribution?
-   Brand trust?
-   Existing customer base?
-   Bundled offerings?

**Weaknesses**

-   Where do incumbents fail customers today?
-   Are they constrained by:

-   Legacy architecture?
-   Organizational inertia?
-   Pricing rigidity?

**Likelihood of Response**

-   Will incumbents build, buy, or ignore this category?
-   What is their historical behavior in similar disruptions?
-   How quickly could they respond if this startup gains traction?

**Switching Dynamics**

-   How hard is it for customers to switch away from incumbents?
-   What integrations or workflows create lock-in?
-   Is there a wedge that avoids direct displacement?

**Pricing Power**

-   Are incumbents overpriced relative to value?
-   Are they cross-subsidizing this product?

**3) New Entrants / Startups**

**Competitive Set**

-   Who are the top startup competitors?
-   How crowded is the category?
-   Are competitors well-funded?

**Differentiation vs. Peers**

-   How does this company compare to other startups?
-   Are competitors converging toward similar features?
-   Is there real differentiation or feature parity?

**Speed & Execution**

-   Which competitors are shipping fastest?
-   Who is winning early customers?
-   Are competitors iterating based on user feedback effectively?

**Fundraising & Resources**

-   How much capital have competitors raised?
-   Are there "overfunded" players who can outspend?
-   Are there undercapitalized but strong technical teams?

**Strategic Positioning**

-   Are competitors attacking the same ICP or different segments?
-   Are some going upmarket vs. downmarket?

**4) Market Positioning**

**Value Proposition**

-   What is the company's core positioning?
-   Is it:

-   Faster?
-   Cheaper?
-   Better UX?
-   More accurate?
-   More integrated?

**Target Customer**

-   Who is the primary ICP?
-   How does that differ from competitors' ICPs?
-   Is the company focused or trying to serve too many segments?

**Use Case Focus**

-   Is the company solving a narrow wedge problem or broad platform?
-   Are competitors more specialized or generalized?
-   Is there risk of being a "feature" vs. a "platform"?

**Messaging & Branding**

-   Is the positioning clear and compelling?
-   Do customers understand why it is different?
-   Does messaging resonate vs. competitors?

**Pricing Strategy**

-   Is pricing aligned with positioning (premium vs. budget)?
-   How does pricing compare to competitors?
-   Is pricing a competitive advantage or liability?

**5) Strategic Focus & Expansion**

**Beachhead Strategy**

-   What initial wedge is the company using?
-   Why is this wedge defensible?

**Expansion Path**

-   How does the company plan to expand from initial use case?
-   Is expansion logical or forced?

**Platform Potential**

-   Can this evolve into a platform?
-   Are competitors already platforms?

**Risk of Feature Encroachment**

-   Could incumbents easily replicate this as a feature?
-   Is the company building something standalone or complementary?

**6) Competitive Moats & Durability**

**Defensibility**

-   What prevents competitors from winning long-term?
-   Is the moat:

-   Technology?
-   Data?
-   Network effects?
-   Distribution?

**Network Effects**

-   Does the product get better with more users?
-   Are there two-sided or data network effects?

**Switching Costs**

-   How painful is it to switch away?
-   Are workflows deeply embedded?
-   Is this replacing an incumbent or sitting alongside it?
-   Is this a "budget line item" or a "new spend category"?

**Ecosystem & Integrations**

-   Is the company part of a broader ecosystem?
-   Are integrations a strength or dependency?

**7) Competitive Risks**

-   What is the **most dangerous competitor** and why?
-   What happens if a major incumbent prioritizes this space?
-   Is this market trending toward **winner-take-all or fragmentation**?
-   Are we underwriting **true differentiation or temporary advantage**?
-   Could this company be **out-executed rather than out-innovated**?

**Synthesis Questions**

These are the *decision-driving* questions:

-   Why does this company win vs. incumbents?
-   Why does it win vs. other startups?
-   Does the team have market-leading, world class technical or domain expertise that provides it with competitive advantage?
-   What is the one thing competitors cannot easily replicate?
-   What is the biggest competitive threat faced by the company?
-   Is this a category-defining company, a category disruptor, or a fast follower?
-   In 3--5 years, who controls this market?
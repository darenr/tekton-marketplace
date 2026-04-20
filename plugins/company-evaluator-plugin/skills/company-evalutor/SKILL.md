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
- The output format should be a Microsoft Word document structured as an investor memo, with sections for each area of analysis and a final recommendation. 


See references/due-diligence.md for details of company evaluation framework, including technology/product, competitive landscape, market positioning, and founding team analysis.

## Quality Checklist

Before finalizing the memo, ensure:
- All claims are supported by evidence with sources cited.
- Uncertainties and data gaps are clearly noted.
- The memo is structured logically with clear sections.
- Language is clear and accessible to non-experts.
- The recommendation is clearly stated and justified by the analysis.


---
name: company-evaluator
description:  >-
    Produces an early-stage VC investment memo with founder diligence, investor signal analysis, market research, and competitive positioning. Use when a user asks to evaluate a startup, prepare an investment memo, assess founder-market fit, compare startup competitors, or diligence a company from a URL/pitch deck. 
metadata:
    author: Tekton
    version: 1.1.2
    category: venture-capital
---

# Company Evaluator Skill

## What this skill produces

An Investor Memo — a comprehensive document that synthesizes research on the founders, investors, market, and competitive landscape to provide a clear recommendation on whether to pursue an investment opportunity. The final output is a Microsoft Word document with appropriate formatting and structure for an investor memo.

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
- When evaluating a company's ability to win, systematically assess technology, incumbents vs. new entrants, and positioning/focus, differentiation, as well as the founding team and the fundability or financial strength of its competitors.
- Determine why the company is well-positioned to win in its market, and what risks it faces. Consider the company's technology/product, competitive landscape, market positioning, and founding team.
- The output format should be a Microsoft Word document structured as an investor memo, with sections for each area of analysis and a final recommendation. 


See references/due-diligence.md for details of company evaluation framework.

## Quality Checklist

Before finalizing the memo, ensure:
- All claims are supported by evidence with sources cited.
- Uncertainties and data gaps are clearly noted.
- The memo is structured logically with clear sections.
- Language is clear and accessible to non-experts.
- The recommendation is clearly stated and justified by the analysis.
- The final output is a Microsoft Word document with appropriate formatting and structure for an investor memo.
# tekton-company-evaluator

Evaluator skill and tools for Tekton's company evaluator, packaged for use as an
Anthropic Claude skill.

## Anthropic Claude skill

This repository provides the `SKILL.md` definition for a reusable company
evaluation skill.

## File Structure

```bash
your-skill-name/
├── SKILL.md # Required - main skill file
├── scripts/ # Optional - executable code
│ ├── process_data.py # Example
│ └── validate.sh # Example
├── references/ # Optional - documentation
│ ├── api-guide.md # Example
│ └── examples/ # Example
└── assets/ # Optional - templates, etc.
 └── report-template.md # Example
 ```
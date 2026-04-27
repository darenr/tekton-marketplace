import json
import yaml
from pathlib import Path
from typing import Any, Dict

# This will create the marketplace.json, and a .claude-plugin/plugin.json for each plugin, the source of
# truth is considered the plugins/<plugin-folder>/skills/SKILL.md file metadata.
# The format is defined here https://code.claude.com/docs/en/plugins


def process_skill_md(plugin_dir: Path) -> Dict[str, Any]:
    skill_file = plugin_dir / "skills" / plugin_dir.name / "SKILL.md"
    if not skill_file.exists():
        raise FileNotFoundError(f"SKILL.md not found at {skill_file}")

    content = skill_file.read_text()
    parts = content.split("---", 2)
    if len(parts) >= 3:
        return yaml.safe_load(parts[1]) or {}
    return {}


def create_plugin_json(
    plugin_folder_name: str, skill_metadata: Dict[str, Any]
) -> Dict[str, Any]:
    metadata = skill_metadata.get("metadata", {})
    return {
        "name": plugin_folder_name,
        "description": skill_metadata.get("description", ""),
        "version": metadata.get("version", "1.0.0"),
        "author": {
            "name": metadata.get("author", "Unknown"),
        },
    }


def write_plugin_json_file(plugin_dir: Path, plugin_json: Dict[str, Any]) -> None:
    plugin_config_dir = plugin_dir / ".claude-plugin"
    plugin_config_dir.mkdir(parents=True, exist_ok=True)

    plugin_file = plugin_config_dir / "plugin.json"
    plugin_file.write_text(json.dumps(plugin_json, indent=2) + "\n")


def write_marketplace_json(marketplace: Dict[str, Any]) -> None:
    marketplace_dir = Path(".claude-plugin")
    marketplace_dir.mkdir(parents=True, exist_ok=True)

    marketplace_file = marketplace_dir / "marketplace.json"
    marketplace_file.write_text(json.dumps(marketplace, indent=2) + "\n")


def main() -> None:
    marketplace = {
        "name": "tekton-marketplace",
        "owner": {"name": "Tekton"},
        "metadata": {
            "description": "Tekton Claude plugin marketplace",
            "version": "1.0.0",
        },
        "plugins": [],
    }

    plugins_dir = Path("plugins")
    if not plugins_dir.exists():
        print("No 'plugins' directory found.")
        return

    for plugin_dir in plugins_dir.iterdir():
        if not plugin_dir.is_dir():
            continue

        plugin_folder_name = plugin_dir.name
        print(f"Processing {plugin_folder_name}...")

        try:
            plugin = process_skill_md(plugin_dir)
        except FileNotFoundError as e:
            print(f"Skipping {plugin_folder_name}: {e}")
            continue

        if not plugin:
            print(f"Skipping {plugin_folder_name}: No YAML frontmatter found in SKILL.md.")
            continue

        # Validation
        missing_keys = [k for k in ("name", "description", "metadata") if k not in plugin]
        if missing_keys:
            print(f"Skipping {plugin_folder_name}: Missing required keys {missing_keys}")
            continue

        metadata = plugin["metadata"]
        if "version" not in metadata:
            print(f"Skipping {plugin_folder_name}: Missing 'version' in metadata")
            continue

        marketplace["plugins"].append(
            {
                "name": plugin["name"],
                "description": plugin["description"],
                "source": f"./plugins/{plugin_folder_name}",
                "version": metadata["version"],
                "author": {"name": metadata.get("author", "Unknown")},
                "license": metadata.get("license", "MIT"),
            }
        )
        print(f"Added {plugin['name']} to marketplace.json")

        plugin_json = create_plugin_json(plugin_folder_name, plugin)
        write_plugin_json_file(plugin_dir, plugin_json)

    if marketplace["plugins"]:
        write_marketplace_json(marketplace)
        print("marketplace.json created successfully.")
    else:
        print("No valid plugins found. marketplace.json not created.")


if __name__ == "__main__":
    main()

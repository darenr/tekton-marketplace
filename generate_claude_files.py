import json
import yaml
import glob
import os

# This will create the marketplace.json, and a .claude-plugn/plugin.json for each plugin, the source of
# truth is considered the plugins/<plugin-folder>/skills/SKILL.md file metadata.
# The format is defined here https://code.claude.com/docs/en/plugins


def process_skill_md(plugin_folder_name: str):
    with open(f"plugins/{plugin_folder_name}/skills/{plugin_folder_name}/SKILL.md", "r") as f:
        return yaml.safe_load(f.read().split("---")[1])


def create_plugin_json(plugin_folder_name: str, skill_metadata: dict):
    # example:
    # {
    #   "name": "my-first-plugin",
    #   "description": "A greeting plugin to learn the basics",
    #   "version": "1.0.0",
    #   "author": {
    #     "name": "Your Name"
    #   }
    # }

    return {
        "name": plugin_folder_name,
        "description": skill_metadata.get("description", ""),
        "version": skill_metadata.get("metadata", {}).get("version", "1.0.0"),
        "author": {
            "name": skill_metadata.get("metadata", {}).get("author", "Unknown"),
        },
    }


def write_plugin_json_file(plugin_folder_name: str, plugin_json: dict):
    if not os.path.exists(f"plugins/{plugin_folder_name}/.claude-plugin"):
        os.makedirs(f"plugins/{plugin_folder_name}/.claude-plugin")

    with open(f"plugins/{plugin_folder_name}/.claude-plugin/plugin.json", "w") as f:
        json.dump(plugin_json, f, indent=2)


def write_marketplace_json(marketplace: dict):
    with open(".claude-plugin/marketplace.json", "w") as f:
        json.dump(marketplace, f, indent=2)


if __name__ == "__main__":
    # Create marketplace.json
    marketplace = {
        "name": "tekton-marketplace",
        "owner": {"name": "Tekton"},
        "plugins": [],
    }

    for plugin_folder in glob.glob("plugins/*/"):
        plugin_folder_name = plugin_folder.split("/")[1]

        print(f"Processing {plugin_folder_name}...")
        plugin = process_skill_md(plugin_folder_name)

        assert "name" in plugin, f"Name not found in metadata for {plugin_folder_name}"
        assert "description" in plugin, (
            f"Description not found in metadata for {plugin_folder_name}"
        )
        assert "metadata" in plugin, f"Metadata not found in metadata for {plugin_folder_name}"
        assert "version" in plugin["metadata"], (
            f"Version not found in metadata for {plugin_folder_name}"
        )

        marketplace["plugins"].append(
            {
                "name": plugin["name"],
                "description": plugin["description"],
                "source": f"./{plugin_folder_name}",
                "version": plugin["metadata"]["version"],
                "author": {"name": plugin["metadata"].get("author", "Unknown")},
                "license": plugin["metadata"].get("license", "MIT"),
            }
        )
        print(f"Added {plugin['name']} to marketplace.json")
        write_plugin_json_file(
            plugin_folder_name, create_plugin_json(plugin_folder_name, plugin)
        )

    if marketplace["plugins"]:
        write_marketplace_json(marketplace)
        print("marketplace.json created successfully.")
    else:
        print("No plugins found. marketplace.json not created.")

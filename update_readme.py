import os
import random
from github import Github
from datetime import datetime, timezone

USERNAME = os.environ["GH_USERNAME"]
TOKEN = os.environ["GH_TOKEN"]

g = Github(TOKEN)
user = g.get_user(USERNAME)

# Only public, non-fork repos with the "featured" topic
repos = [
    repo
    for repo in user.get_repos()
    if not repo.fork
    and not repo.private
    and "featured" in repo.get_topics()
]

if not repos:
    raise RuntimeError("No repositories found with the 'featured' topic.")

chosen = random.choice(repos)
desc = chosen.description or "No description provided."

# Format the featured block
featured_block = f"""> **[{chosen.name}]({chosen.html_url})**  
{desc}

_Last updated: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}_"""

# Read the template
with open("README.template.md", "r", encoding="utf-8") as f:
    template = f.read()

# Replace placeholder
output = template.replace("<!-- FEATURED_REPO -->", featured_block)

# Write updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(output)

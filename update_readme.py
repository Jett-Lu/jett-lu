import os
import random
from github import Github
from datetime import datetime

USERNAME = os.environ["GH_USERNAME"]
TOKEN = os.environ["GH_TOKEN"]

g = Github(TOKEN)
user = g.get_user(USERNAME)
repos = [repo for repo in user.get_repos() if not repo.fork and not repo.private]

chosen = random.choice(repos)
desc = chosen.description or "No description provided."

```text
{chosen.name}
{desc}
→ {chosen.html_url}
```

_Last updated: {datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")}_

"""

# Read template
with open("README.template.md", "r") as f:
    template = f.read()

# Replace placeholder
output = template.replace("<!-- FEATURED_REPO -->", featured_block)

# Write updated README
with open("README.md", "w") as f:
    f.write(output)

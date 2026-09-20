#!/usr/bin/env python3
"""Refresh the 'Recent activity' block in README.md from the public events API."""
import json, os, re, urllib.request
from collections import OrderedDict

USER = "kavonrtep"
MAX_LINES = 8
START, END = "<!--START_SECTION:activity-->", "<!--END_SECTION:activity-->"

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/events/public?per_page=100",
    headers={"Accept": "application/vnd.github+json",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})})
events = sorted(json.load(urllib.request.urlopen(req)), key=lambda e: e["created_at"], reverse=True)

lines = OrderedDict()   # key -> line; pushes to same repo on same day are merged
for e in events:
    repo = e["repo"]["name"]
    if repo == f"{USER}/{USER}":
        continue                      # ignore the automated README commits
    day = e["created_at"][:10]
    url = f"https://github.com/{repo}"
    p = e["payload"]
    t = e["type"]
    if t == "PushEvent":
        key = ("push", repo, day)
        n = p.get("distinct_size", p.get("size", len(p.get("commits", [])) or None))
        msg = p["commits"][-1]["message"].splitlines()[0] if p.get("commits") else ""
        if key in lines:
            if n and lines[key]["n"] is not None:
                lines[key]["n"] += n
        else:
            lines[key] = {"n": n, "msg": msg, "repo": repo, "url": url, "day": day}
    elif t == "ReleaseEvent" and p.get("action") == "published":
        r = p["release"]
        lines[("rel", repo, r["tag_name"])] = {"text": f"🏷️ Released [{r['tag_name']}]({r['html_url']}) of [{repo}]({url})", "day": day}
    elif t == "IssuesEvent":
        i = p["issue"]
        lines[("iss", i["html_url"], p["action"])] = {"text": f"🐛 {p['action'].capitalize()} issue [#{i['number']}]({i['html_url']}) in [{repo}]({url})", "day": day}
    elif t == "PullRequestEvent":
        pr = p["pull_request"]
        act = "merged" if p["action"] == "closed" and pr.get("merged") else p["action"]
        lines[("pr", pr["html_url"], act)] = {"text": f"🔀 {act.capitalize()} PR [#{pr['number']}]({pr['html_url']}) in [{repo}]({url})", "day": day}
    elif t == "CreateEvent" and p.get("ref_type") == "repository":
        lines[("new", repo)] = {"text": f"✨ Created repository [{repo}]({url})", "day": day}

out = []
for v in lines.values():
    if "text" not in v:
        count = "" if not v["n"] else f" {v['n']} commit" + ("" if v["n"] == 1 else "s")
        msg = f" — *{v['msg'][:70]}*" if v["msg"] else ""
        v["text"] = f"⬆️ Pushed{count} to [{v['repo']}]({v['url']}){msg}"
    out.append(f"- {v['day']} · {v['text']}")
    if len(out) >= MAX_LINES:
        break

block = START + "\n" + "\n".join(out) + "\n" + END
readme = open("README.md", encoding="utf-8").read()
new = re.sub(re.escape(START) + r".*?" + re.escape(END), block, readme, flags=re.S)
if new != readme:
    open("README.md", "w", encoding="utf-8").write(new)
    print("README updated")
else:
    print("No change")

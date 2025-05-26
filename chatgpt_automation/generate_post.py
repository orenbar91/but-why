import subprocess
import datetime
import os
import pyperclip

# Run AppleScript
subprocess.run(["osascript", "chatgpt_post_chrome.scpt"])

# Get clipboard contents
content = pyperclip.paste()

# Create folder if not exists
output_dir = "content/posts"
os.makedirs(output_dir, exist_ok=True)

# Save content to markdown file
today = datetime.date.today().isoformat()
filename = os.path.join(output_dir, f"auto_post_{today}.md")

with open(filename, "w") as f:
    f.write(content)

print(f"Saved blog post to {filename}")
import re

log_path = r"C:\Users\admin\.gemini\antigravity\brain\ca4fa98f-056d-4c0f-b0a4-a68c56c252a5\.system_generated\logs\overview.txt"
with open(log_path, 'r', encoding='utf-8') as f:
    text = f.read()

# The prompt was: "modify the UI to this: <!-- Design System -->..."
# We will search for "modify the UI to this:" and capture everything until the next model response.
start_idx = text.find("modify the UI to this:")
if start_idx != -1:
    start_idx += len("modify the UI to this:")
    end_idx = text.find(">", start_idx) # Actually the HTML ends somewhere. Let's just find "</html>"
    end_idx = text.rfind("</html>", start_idx)
    if end_idx != -1:
        html = text[start_idx:end_idx + 7]
        with open("scratch_design.html", "w", encoding="utf-8") as out:
            out.write(html.strip())
        print("Successfully extracted HTML to scratch_design.html")
    else:
        print("Could not find </html>")
else:
    print("Could not find prompt text")

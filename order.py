import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Define the HTML blocks directly from what's currently in about.md
# I will extract each block by looking for "<!-- =========================(...)-->" blocks.
splitter = "<!-- ========================================================================================================================== -->\n"
parts = text.split(splitter)

header_part = parts[0]
paper_blocks = parts[1:]

paper_dict = {}
for p in paper_blocks:
    if "MVP:" in p:
        paper_dict["MVP"] = p.strip()
    elif "MacTok:" in p:
        paper_dict["MacTok"] = p.strip()
    elif "IVQ" in p:
        paper_dict["IVQ"] = p.strip()
    elif "OrderMind" in p or "Manipulation Ordering" in p:
        paper_dict["OrderMind"] = p.strip()
    elif "ARTDECO:" in p:
        paper_dict["ARTDECO"] = p.strip()
    elif "GOOD:" in p:
        paper_dict["GOOD"] = p.strip()
    elif "Dark-ISP:" in p:
        paper_dict["Dark-ISP"] = p.strip()
    elif "Loong:" in p:
        paper_dict["Loong"] = p.strip()

desired_order = ["MVP", "MacTok", "GOOD", "OrderMind", "IVQ", "Dark-ISP", "ARTDECO", "Loong"]

# Construct the new publications section without sub-headers
new_text_blocks = []
for title in desired_order:
    if title in paper_dict:
        new_text_blocks.append(splitter + "\n" + paper_dict[title] + "\n")

new_papers_content = "\n".join(new_text_blocks)

# I need to clean up the `header_part` which contains the old section headers
# Strip out "## Multimodal Structured Reasoning" and "## Other Explorations" from the text
# Find the start of publications
pub_start = header_part.find("# 📝 Selected Publications")
if pub_start != -1:
    # Just keep everything up to the intro of publications
    # Let's see what's in header_part currently.
    pass


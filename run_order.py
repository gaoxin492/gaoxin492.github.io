import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    text = f.read()

splitter = "<!-- ========================================================================================================================== -->\n"
parts = text.split(splitter)

header_part = parts[0]
paper_blocks = parts[1:]

paper_dict = {}
for p in paper_blocks:
    if "MVP:" in p: paper_dict["MVP"] = p.strip()
    elif "MacTok:" in p: paper_dict["MacTok"] = p.strip()
    elif "IVQ" in p: paper_dict["IVQ"] = p.strip()
    elif "OrderMind" in p or "Manipulation Ordering" in p: paper_dict["OrderMind"] = p.strip()
    elif "ARTDECO:" in p: paper_dict["ARTDECO"] = p.strip()
    elif "GOOD:" in p: paper_dict["GOOD"] = p.strip()
    elif "Dark-ISP:" in p: paper_dict["Dark-ISP"] = p.strip()
    elif "Loong:" in p: paper_dict["Loong"] = p.strip()

desired_order = ["MVP", "MacTok", "GOOD", "OrderMind", "IVQ", "Dark-ISP", "ARTDECO", "Loong"]

new_text_blocks = []
for title in desired_order:
    if title in paper_dict:
        new_text_blocks.append(splitter + "\n" + paper_dict[title] + "\n\n")

new_papers_content = "".join(new_text_blocks)

# Clean up header part by removing the subheaders
# Find where "# 📝 Selected Publications" starts
pub_start = header_part.find("# 📝 Selected Publications")

new_header_part = header_part[:pub_start] + """# 📝 Selected Publications

My research primarily focuses on **Multimodal Structured Reasoning**, along with other exploratory works in distribution modeling and vision foundation models.

"""

# Retain anything after the last paper block.
# Wait, paper_blocks[-1] contains the rest of the file after the last paper block!
# Let's extract the "rest_of_file" from paper_blocks[-1]
# Actually, the last element of paper_blocks has the last paper AND the subsequent sections
# We need to gracefully separate the last paper from the rest of the file.
last_paper_chunk = paper_blocks[-1]
# Assume paper ends at the last </div></div> matching structure, but safely we can find "<!-- # Why PhD?" or "\n# 🎖 Honors and Awards"
end_idx = last_paper_chunk.find("\n# 🎖 Honors and Awards")
if end_idx == -1: end_idx = last_paper_chunk.find("<!-- # Why PhD?")

if end_idx != -1:
    rest_of_file = last_paper_chunk[end_idx:]
    # remove the rest_of_file from the paper_dict string
    for k in paper_dict:
        if paper_dict[k].endswith(rest_of_file.strip()):
            paper_dict[k] = paper_dict[k].replace(rest_of_file.strip(), "").strip()
            
    # Then rebuild list identically
    new_text_blocks = []
    for title in desired_order:
        if title in paper_dict:
            new_text_blocks.append(splitter + "\n" + paper_dict[title] + "\n\n")
    new_papers_content = "".join(new_text_blocks)
    
    final_text = new_header_part + new_papers_content + "\n" + rest_of_file
else:
    # fallback
    print("Could not find end marker")
    final_text = text

with open('_pages/about.md', 'w', encoding='utf-8') as f:
    f.write(final_text)

print("Done")

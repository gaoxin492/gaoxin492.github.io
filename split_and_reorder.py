import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    text = f.read()

# I will find the bounds of the papers text.
pre_marker = "## Multimodal Structured Reasoning\n"
post_marker = "\n<!-- # Why PhD?"

start_idx = text.find(pre_marker)
end_idx = text.find(post_marker)

if start_idx != -1 and end_idx != -1:
    papers_area = text[start_idx + len(pre_marker):end_idx]
    
    # Split by the comment bar
    splitter = "<!-- ========================================================================================================================== -->\n"
    chunks = papers_area.split(splitter)
    
    # chunks might have empty elements or the "## Other Explorations" header
    # Let's filter and identify each chunk
    structured_reasoning_papers = []
    other_papers = []
    
    for c in chunks:
        c_stripped = c.strip()
        if not c_stripped: continue
        
        # If the chunk has the header, remove it for a clean paper block
        if "## Other Explorations" in c:
            c = c.replace("## Other Explorations", "").strip()
            if not c: continue

        # Identify where this paper belongs
        if "Loong:" in c or "OrderMind:" in c or "ARTDECO:" in c or "MacTok:" in c or "IVQ:" in c or "Manipulation Ordering" in c or "Visual Concept Learning" in c or "Synthesize Long" in c:
            structured_reasoning_papers.append(c)
        else:
            # MVP, GOOD, Dark-ISP
            other_papers.append(c)
            
    # Reassemble
    new_papers_area = "\n\n"
    
    # Join structured reasoning
    for p in structured_reasoning_papers:
        new_papers_area += splitter + "\n" + p + "\n\n"
        
    new_papers_area += "\n## Other Explorations\n\n"
    
    for p in other_papers:
        new_papers_area += splitter + "\n" + p + "\n\n"
        
    # Inject back
    new_text = text[:start_idx + len(pre_marker)] + new_papers_area + text[end_idx:]
    
    with open('_pages/about.md', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Reordered successfully!")
else:
    print("Markers not found!")


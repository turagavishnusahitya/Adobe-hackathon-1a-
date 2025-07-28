import fitz  # PyMuPDF
import os
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title", "") or os.path.basename(pdf_path)
    
    outline = []
    # heuristics: we will scan pages and find text blocks with font size and font style to decide headings
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b['type'] != 0:
                continue
            for line in b["lines"]:
                for span in line["spans"]:
                    size = span["size"]
                    text = span["text"].strip()
                    # Skip empty or very short text
                    if len(text) < 3:
                        continue
                    # Determine heading level by font size (heuristic thresholds)
                    if size > 15:
                        level = "H1"
                    elif 12 < size <= 15:
                        level = "H2"
                    elif 9 < size <= 12:
                        level = "H3"
                    else:
                        continue
                    
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })
    return title, outline


def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    # process all PDFs in input_dir
    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(".pdf"):
            continue
        
        pdf_path = os.path.join(input_dir, filename)
        print(f"Processing {pdf_path} ...")
        
        title, outline = extract_outline(pdf_path)
        
        output_data = {
            "title": title,
            "outline": outline
        }
        
        output_filename = filename.rsplit(".", 1)[0] + ".json"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"Output saved to {output_path}")

if __name__ == "__main__":
    main()

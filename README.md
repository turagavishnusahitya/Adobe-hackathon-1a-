# 📄 PDF Outline Extractor

![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python)
![License](https://img.shields.io/github/license/turagavishnusahitya/pdf-outline-extractor)
![Issues](https://img.shields.io/github/issues/turagavishnusahitya/pdf-outline-extractor)

**PDF Outline Extractor** is a lightweight and fast tool to extract structured outlines (like H1, H2, H3 headings) from PDF documents such as books, manuals, and reports. The tool uses rule-based logic (no ML models) and runs within Docker in under 10 seconds.

---

## 🚀 Features

- 📘 Extracts headings like Title, H1, H2, H3 with page numbers
- ⚡ Fast (under 10 seconds for 50-page PDFs)
- 🧠 Rule-based, no machine learning required
- 📦 Outputs structured `outline.json`
- 🐳 Dockerized for easy setup and use
- 💻 Offline-capable and completely CPU-based

---

## 📂 Project Structure

```
📁 project-root/
├── Dockerfile
├── input/           # Place PDF files here
├── output/          # Extracted JSON files appear here
├── app/
│   └── main.py      # Main Python script for extraction
```

---

## 🛠️ Technologies Used

| Tool / Library     | Purpose                                 |
|--------------------|------------------------------------------|
| **Python 3.10+**    | Programming language                     |
| **PyMuPDF (fitz)**  | PDF parsing and style extraction         |
| **Regex (re)**      | Heading text cleanup                     |
| **os / json**       | File handling and JSON generation        |
| **Docker**          | Containerization for consistent runtime  |

---

## 🐳 Docker Usage

### 🔧 Step 1: Build the Docker Image

```bash
docker build -t pdf-outline-app .
```

### ▶️ Step 2: Run the Docker Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  pdf-outline-app
```

✅ Place your PDF files in the `input/` folder  
✅ After processing, check the `output/` folder for `outline.json`

---

## 📤 Sample Output (`outline.json`)

```json
[
  {
    "level": "H1",
    "heading": "Chapter 1: Getting Started",
    "page_number": 1
  },
  {
    "level": "H2",
    "heading": "Installation",
    "page_number": 2
  },
  {
    "level": "H3",
    "heading": "Requirements",
    "page_number": 2
  }
]
```

---

## ⚠️ Limitations

- Only supports PDFs up to **50 pages**
- Does not handle scanned/image PDFs
- Depends on **font size/style** for heading detection
- English-language support only (for now)

---

## 📌 Use Cases

- 📚 Summarizing e-books or manuals
- 🧾 Creating table of contents for documents
- 🧠 Preprocessing for NLP or document analysis
- 🗂️ Document indexing and search

---

## 🤝 Contributing

We welcome contributions!

### To contribute:

1. Fork this repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Create a pull request

Please make sure to update tests as appropriate.

---

## 🧑‍💻 Author

**Turaga Vishnu Sahitya**  
📫 [turagavishnusahitya@gmail.com](mailto:turagavishnusahitya@gmail.com)  
🔗 [GitHub Profile](https://github.com/turagavishnusahitya)


# PDF Outline Extractor

## Overview
This tool extracts the title and outline headings (H1, H2, H3) from PDF files and outputs a JSON file with the extracted structure.

## How to Build and Run

### Build Docker image
```bash
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .

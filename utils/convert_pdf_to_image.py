from pdf2image import convert_from_path


SIMPLE_DOCUMENT_NAME = "original-simple-doc.pdf"
SIMPLE_DOCUMENT_PATH = f"data/original/{SIMPLE_DOCUMENT_NAME}"

pages = convert_from_path(SIMPLE_DOCUMENT_PATH)

tess_cfg = "--psm 6"
for idx, page in enumerate(pages):
    print("Page", idx + 1)
    direct = f"data/images/{SIMPLE_DOCUMENT_NAME.rstrip('.pdf')}_{idx+1}.jpg"
    page.save(direct, "JPEG")

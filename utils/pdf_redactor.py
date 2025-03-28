from PyPDF2 import PdfReader, PdfWriter

class PDFRedactor:
    @staticmethod
    def redact_sections(pdf_path, sensitive_sections, output_path=None):
        if output_path is None:
            output_path = "redacted_" + pdf_path.split("/")[-1]
        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()

            for section in sensitive_sections:
                if section['text'] in text:
                    # Ersetze den sensiblen Text mit █████
                    text = text.replace(section['text'], "█████")

            writer.add_page(page)

        with open(output_path, "wb") as output_file:
            writer.write(output_file)

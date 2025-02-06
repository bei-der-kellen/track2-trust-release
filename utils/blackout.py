import fitz  # PyMuPDF

class Blackout:

    @staticmethod
def redact_sentences(text_array, file_input_path, file_output_path):
    """
    Schw�rzt alle W�rter aus text_array in einem PDF.
    
    :param text_array: Liste mit S�tzen/W�rtern, die geschw�rzt werden sollen.
    :param file_input_path: Pfad zur Eingabe-PDF.
    :param file_output_path: Pfad zur Ausgabe-PDF.
    """
    # PDF �ffnen
    doc = fitz.open(file_input_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        words = page.get_text("words")  # Alle W�rter mit Positionen
        blocks = page.get_text("blocks")  # Alle Textbl�cke mit Positionen
        full_text = page.get_text("text")  # Gesamter Text der Seite

        for sentence in text_array:
            if sentence in full_text:
                print(f"Satz gefunden: '{sentence}' auf Seite {page_num+1}")

                # Satz in W�rter zerlegen
                sentence_words = sentence.split()

                # Suche den passenden Textblock
                for block in blocks:
                    x0, y0, x1, y1, block_text, _, _ = block

                    if sentence in block_text:
                        print(f"Textblock gefunden f�r '{sentence}' auf Seite {page_num+1}")

                        # Schw�rze jedes Wort im Block, wenn es zum Satz geh�rt
                        for word in words:
                            wx0, wy0, wx1, wy1, text, _, _, _ = word

                            # Pr�fen, ob das Wort in diesem Satz enthalten ist und im Block liegt
                            if text in sentence_words and (x0 <= wx0 <= x1 and y0 <= wy0 <= y1):
                                print(f"Schw�rze Wort: {text} auf Seite {page_num+1}")
                                word_rect = fitz.Rect(wx0, wy0, wx1, wy1)
                                page.add_redact_annot(word_rect, fill=(0, 0, 0))  # Schwarzer Hintergrund
                                page.apply_redactions()  # Anwenden der Schw�rzung

    # Ge�ndertes PDF speichern
    doc.save(file_output_path)
    doc.close()


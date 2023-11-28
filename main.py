import pyttsx3
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extrai texto de um arquivo PDF.

    Parameters:
    - pdf_path (str): Caminho do arquivo PDF.

    Returns:
    - str: Texto extraído do PDF.
    """
    try:
        with fitz.open(pdf_path) as pdf_document:
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text += page.get_text()

        return text.strip()
    except Exception as e:
        print(f"Não foi possível extrair texto do PDF. Erro: {str(e)}")
        return None

def convert_text_to_audio(text, output_path='output.mp3'):
    """
    Converte texto para áudio e salva em um arquivo MP3.

    Parameters:
    - text (str): Texto a ser convertido.
    - output_path (str): Caminho do arquivo de saída MP3.

    Returns:
    - None
    """
    try:
        speaker = pyttsx3.init()
        speaker.save_to_file(text, output_path)
        speaker.runAndWait()
        speaker.stop()
        print(f"Áudio gerado com sucesso em: {output_path}")
    except Exception as e:
        print(f"Erro ao gerar áudio. Erro: {str(e)}")

def main():
    # Substitua pelo caminho do seu PDF
    pdf_path = 'CV Lázaro Rafael Xavier. (1).pdf'
    
    # Extraia texto do PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    if extracted_text:
        # Converta texto para áudio
        convert_text_to_audio(extracted_text)
    else:
        print("Falha ao extrair texto do PDF.")

if __name__ == "__main__":
    main()

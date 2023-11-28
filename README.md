# PDF-converter-to-audio

Projeto: Extração de texto de PDF e conversão para áudio

# Descrição:

Este projeto consiste em extrair texto de um arquivo PDF e converter esse texto para áudio. O texto extraído pode ser de qualquer tipo, como um currículo, um documento legal ou um livro.

# Requisitos:

Python 3
PyMuPDF
pyttsx3
Instalação:

# Para instalar os requisitos, execute os seguintes comandos:

pip install PyMuPDF
pip install pyttsx3
Uso:

# Para usar o projeto, siga estas etapas:

Substitua o caminho do arquivo PDF no arquivo main.py.
Execute o arquivo main.py.
Saída:

Se o texto for extraído com sucesso, ele será convertido para áudio e salvo no arquivo especificado no parâmetro output_path.

# Exemplo:

O seguinte exemplo extrai texto do meu currículo e converte esse texto para áudio:

Python
pdf_path = 'CV Lázaro Rafael Xavier. (1).pdf'

extracted_text = extract_text_from_pdf(pdf_path)

if extracted_text:
    convert_text_to_audio(extracted_text)
else:
    print("Falha ao extrair texto do PDF.")
Use o código com cuidado. Saiba mais
Neste caso, o arquivo de áudio será salvo no arquivo output.mp3.

# Observações:

O projeto pode não funcionar corretamente com arquivos PDF que contenham imagens ou outros elementos não textuais.
Obrigado por usar o meu projeto!

import os
import PyPDF2

## O código não está funcionando

def search_word_in_pdfs(folder_path, search_word):
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    found_files = []

    for pdf_file in pdf_files:
        file_path = os.path.join(folder_path, pdf_file)

        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(pdf_reader.len(pdf_reader.pages)):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()
                if search_word.lower() in text.lower():
                    found_files.append(pdf_file)
                    break

    return found_files

if __name__ == "__main__":
    folder_path = input("Digite o caminho da pasta contendo os arquivos PDF: ")
    search_word = input("Digite a palavra que deseja procurar nos arquivos PDF: ")

    result = search_word_in_pdfs(folder_path, search_word)

    if result:
        print(f"A palavra '{search_word}' foi encontrada nos seguintes arquivos:")
        for file in result:
            print(file)
    else:
        print(f"A palavra '{search_word}' não foi encontrada em nenhum arquivo PDF da pasta.")




import os
import PyPDF3
import PyPDF2
from googletrans import Translator
from googletrans import LANGUAGES

# Define the folder containing the documents
document_folder = "documents"

# List available documents
document_list = os.listdir(document_folder)

# Function to select a document
def select_document():
    print("Available documents:")
    for i, doc in enumerate(document_list):
        print(f"{i + 1}. {doc}")    
    document_index = int(input("Enter the document number you want to choose: ")) - 1
    selected_document = document_list[document_index]
    return os.path.join(document_folder, selected_document)

# Function to select a language
def select_language():
    print("Available languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

    while True:
        choice = input("Enter the language code you want to select: ")
        if choice in LANGUAGES:
            return choice
        else:
            print("Invalid choice. Please select a valid language code.")
select_language()

# Function to extract text from a PDF document
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    def translate_text(text, target_lang):
        translator = Translator()
        translated = translator.translate(text, dest=target_lang)
        
    return translate_text

# Main chatbot loop
while True:
    document_path = select_document()
    if document_path.endswith(".pdf"):
        document_content = extract_text_from_pdf(document_path)
    else:
        with open(document_path, 'r', encoding='utf-8') as file:
            document_content = file.read()
    
    target_language = select_language()
    
    print("Document content:")
    print(document_content)
    
    while True:
        user_input = input("Ask a question or type 'end' to close the session: ")
        if user_input.lower() == 'end':
            break
        
        # Implement logic to check if the question is relevant to the document
        # If relevant, provide an answer in the selected language
        # If not relevant, initiate connection to a human assistant
        
        # For now, let's assume all questions are relevant, and translate the answer
        answer = "This is the answer to your question."
        translated_answer = translate_text(answer, target_language)
        print("Chatbot:", translated_answer)
    
    end_session = input("Type 'end' to close the session or press Enter to ask another question: ")
    if end_session.lower() == 'end':
        break

print("Session ended.")

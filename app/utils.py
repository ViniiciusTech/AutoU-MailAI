import sqlite3
import PyPDF2
import io
from werkzeug.utils import secure_filename

""""Lê arquivos .txt e .pdf """

def process_file(file) :
    """" Processsa arquivos enviado e extrai o texto"""
    filename = secure_filename(file.filename) # garantir que o nome do arquivo seja seguro

    if filename.endswith('.txt') :
        content = file.read().decode('utf-8')
        return content
    
    elif filename.endswith('.pdf') :
      # Processar arquivo PDF
      try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
        text = ""
        for page in pdf_reader.pages:
           text +=  page.extract_text()
           return text
      except Exception as e :
         return f"Erro ao processar PDf: {str(e)}"
      
      else :
         return "Formato de arqivo não suportado. Use .txt ou pdf"
 
    def get_stats(database_path):
        """Calcula estatísticas dos emails processados"""
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Total de emails
        cursor.execute("SELECT COUNT(*) FROM emails")
        total_emails = cursor.fetchone()[0]

        # Emails produtivos
        cursor.execute("SELECT COUNT(*) FROM emails WHERE category = 'Produtivo'")
        productive = cursor.fetchone()[0]

        # Emails improdutivos
        cursor.execute("SELECT COUNT(*) FROM emails WHERE category = 'Improdutivo'")
        unproductive = cursor.fetchone()[0]

        # Calcular precisão (simulada)
        if total_emails > 0:
           accuracy = ((productive + unproductive) / total_emails) * 85 + 10 # Simulação de precião
        else :
           accuracy = 0


        conn.close()
        return {
           'total_emails': total_emails,
           'productive': productive,
           'unproductive': unproductive,
           'accuracy': min(accuracy, 95) # Máximo 95%
        }
    
    def clean_text(text):
       """"Limpa e normaliza texto"""
       import re

       # Remover caracteres especiais 
       text = re.sub(r'[^\w\s]', ' ', text)

       # Remover espaços extras
       text = re.sub(r'\s+', ' ', text)

       # Converter para minúsculo
       text = text.lower().strip()

       return text
    

    import re

def extract_email_metadados(email_text):
    """Extrai metadados do email (remetente, assunto, data)"""
    metadata = {
        'sender': None,
        'subject': None,
        'date': None
    }

    # Extrair remetente
    sender_match = re.search(r'from\s*:\s*(.+)', email_text, re.IGNORECASE)
    if sender_match:
        metadata['sender'] = sender_match.group(1).strip()

    # Extrair assunto
    subject_match = re.search(r'subject\s*:\s*(.+)', email_text, re.IGNORECASE)
    if subject_match:
        metadata['subject'] = subject_match.group(1).strip()

    # Extrair data
    date_match = re.search(r'date\s*:\s*(.+)', email_text, re.IGNORECASE)
    if date_match:
        metadata['date'] = date_match.group(1).strip()

    return metadata

 # “Qualquer um pode escrever um código que o computador entenda. Bons programadores escrevem códigos que os humanos entendam.” – Martin Fowler
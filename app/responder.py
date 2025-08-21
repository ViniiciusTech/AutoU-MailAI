import random


class ResponseGenerator:
    def __init__(self):
        self.productive_responses  = [
          "Obrigado pelo seu email. Analisarei as informações e retornarei em breve com uma resposta detalhada.",
            "Recebi sua mensagem e vou revisar os pontos mencionados. Entrarei em contato assim que possível.",
            "Agradecemos o contato. Sua solicitação está sendo analisada e responderemos dentro do prazo estabelecido.",
            "Muito obrigado pela mensagem. Vou verificar os detalhes e dar um retorno adequado em breve.",
            "Recebi seu email e vou dar a devida atenção aos pontos levantados. Aguarde meu retorno."
    ]
        
        # Improdutivos 
        self.unproductive_responses = [
            "Agradecemos seu contato. Sua mensagem foi recebida e será processada conforme nossa política interna.",
            "Obrigado pela mensagem. Caso seja relevante para nossos serviços, entraremos em contato.",
            "Recebemos seu email. Mensagens promocionais são direcionadas para análise da equipe comercial.",
            "Agradecemos o interesse. Sua mensagem foi registrada em nosso sistema.",
            "Obrigado pelo contato. Avaliaremos a relevância da mensagem para nossos processos."
        ]

        # Contexto 
        self.context_responses = {
            'reunião': "Obrigado pelo convite. Vou verificar minha agenda e confirmar a participação na reunião.",
            'projeto': "Recebi as informações sobre o projeto. Vou analisar os requisitos e dar um retorno detalhado.",
            'prazo': "Entendi a urgência do prazo. Vou priorizar esta demanda e responder o mais breve possível.",
            'orçamento': "Obrigado pela solicitação de orçamento. Vou preparar uma proposta detalhada para análise.",
            'contrato': "Recebi os documentos contratuais. Vou revisar os termos e dar um retorno adequado.",
            'problema': "Lamento pelo inconveniente relatado. Vou investigar a situação e buscar uma solução rápida.",
            'reclamação': "Agradecemos o feedback. Sua reclamação será analisada pela equipe responsável."
        }

    def  generate_responses(self, email_text, classification) :
        """"Gera a resposta"""
        email_lower = email_text.lower()

        #Contexto 
        for context, response in self.context_responses.items():
            if context in email_lower:
                return response
            
        # RESP baseado na categoria
        if classification['category'] == 'Produtivo' :
        # Personalizar resposta baseada no sentimento
            if classification['sentiment'] == 'Positivo':
                responses = [
                    "Que ótima notícia! Obrigado por compartilhar. Vou analisar e dar um retorno positivo.",
                    "Excelente! Agradecemos a informação. Vou processar os dados e responder adequadamente."
                ]
                return random.choice(responses)
            elif classification['sentiment'] == 'Negativo':
                responses = [
                    "Lamento pela situação relatada. Vou investigar o problema e buscar uma solução eficaz.",
                    "Entendo sua preocupação. Vou dar atenção especial a esta questão e retornar em breve."
                ]
                return random.choice(responses)
            else:
                return random.choice(self.productive_responses)
        else:
            return random.choice(self.unproductive_responses)
    
    def customize_response(self, base_response, sender_name=None, company=None):
        """Personaliza a resposta com informações do remetente"""
        if sender_name:
            base_response = f"Olá {sender_name}, {base_response.lower()}"
        
        if company:
            base_response += f" Atenciosamente, Equipe {company}."
        else:
            base_response += " Atenciosamente, Equipe de Atendimento."
        
        return base_response

# “A genialidade é 1% inspiração e 99% transpiração.” – Thomas Edson


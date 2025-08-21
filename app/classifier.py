import re
import sqlite3
from collections import Counter
import random

class EmailClassifier:
    def __init__(self): # Palavras para a classsificação 
        self.productive_keywords = [
            'projeto', 'reunião', 'prazo', 'entrega', 'desenvolvimento',
            'implementação', 'análise', 'relatório', 'proposta', 'orçamento',
            'contrato', 'acordo', 'negociação', 'cliente', 'vendas',
            'marketing', 'estratégia', 'planejamento', 'meta', 'objetivo'
        ]

        self.unproductive_keywords = [
            'spam', 'promoção', 'desconto', 'oferta', 'grátis',
            'ganhe', 'prêmio', 'sorteio', 'clique', 'urgente',
            'limitado', 'exclusivo', 'oportunidade', 'dinheiro', 'renda'
        ]
        
        self.sentiment_positive = [
            'excelente', 'ótimo', 'bom', 'positivo', 'sucesso',
            'parabéns', 'feliz', 'satisfeito', 'aprovado', 'aceito'
        ]
        
        self.sentiment_negative = [
            'problema', 'erro', 'falha', 'negativo', 'ruim',
            'insatisfeito', 'reclamação', 'cancelar', 'rejeitado', 'atrasado'
        ]
    
    def preprocess_text(self, text):
        """Pré-processa o texto do email"""
        text = text.lower()
    
        text = re.sub(r'[^a-záàâãéèêíïóôõöúçñ\s]', '', text)
        

        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def extract_keywords(self, text):
        """Extrai palavras-chave relevantes do texto"""
        words = text.split()
        

        productive_found = [word for word in words if word in self.productive_keywords]
        

        unproductive_found = [word for word in words if word in self.unproductive_keywords]
        
        all_keywords = productive_found + unproductive_found
        
        if not all_keywords:
            word_freq = Counter(words)
            stop_words = ['de', 'da', 'do', 'para', 'com', 'em', 'no', 'na', 'um', 'uma', 'o', 'a', 'e', 'que', 'se', 'por']
            filtered_words = [word for word, freq in word_freq.most_common(10) 
                            if len(word) > 3 and word not in stop_words]
            all_keywords = filtered_words[:5]
        
        return list(set(all_keywords))[:5]  
    
    def analyze_sentiment(self, text):
        """Analisa o sentimento do email"""
        positive_count = sum(1 for word in text.split() if word in self.sentiment_positive)
        negative_count = sum(1 for word in text.split() if word in self.sentiment_negative)
        
        if positive_count > negative_count:
            return "Positivo"
        elif negative_count > positive_count:
            return "Negativo"
        else:
            return "Neutro"
    
    def classify(self, email_text):
        """Classifica o email como Produtivo ou Improdutivo"""
        processed_text = self.preprocess_text(email_text)
        
        keywords = self.extract_keywords(processed_text)
        
        sentiment = self.analyze_sentiment(processed_text)
        
        productive_score = 0
        unproductive_score = 0
        
        words = processed_text.split()
        
        for word in words:
            if word in self.productive_keywords:
                productive_score += 2
        
        for word in words:
            if word in self.unproductive_keywords:
                unproductive_score += 3
        
        if len(words) > 50:
            productive_score += 1
    
        uppercase_ratio = sum(1 for char in email_text if char.isupper()) / len(email_text)
        if uppercase_ratio > 0.3:
            unproductive_score += 2
        
        if productive_score > unproductive_score:
            category = "Produtivo"
            confidence = min(95, 60 + (productive_score - unproductive_score) * 5)
        elif unproductive_score > productive_score:
            category = "Improdutivo"
            confidence = min(95, 60 + (unproductive_score - productive_score) * 5)
        else:
            if any(keyword in processed_text for keyword in ['reunião', 'projeto', 'trabalho', 'empresa']):
                category = "Produtivo"
                confidence = 65
            else:
                category = "Improdutivo"
                confidence = 60
        
        return {
            'category': category,
            'confidence': confidence,
            'sentiment': sentiment,
            'keywords': keywords
        }
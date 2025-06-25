# 🍕 AI-Powered Pizza Restaurant Assistant

Questo progetto implementa un assistente AI specializzato in una pizzeria, capace di rispondere alle domande dei clienti basandosi su recensioni reali archiviate in un database vettoriale.

## Caratteristiche Principali
- Recupero di recensioni pertinenti usando embedding vettoriali
- Generazione di risposte contestuali con modelli LLM (Mistral via Ollama)
- Interfaccia conversazionale in tempo reale
- Persistenza del database vettoriale per performance ottimizzate

## Tecnologie Utilizzate
- **Ollama** - Per l'esecuzione locale di modelli LLM
- **LangChain** - Framework per applicazioni basate su LLM
- **ChromaDB** - Database vettoriale open-source
- **Pandas** - Elaborazione del dataset delle recensioni

## Prerequisiti

1. **Ollama installato**: [Download Ollama](https://ollama.ai/)
2. Modelli Ollama necessari:
```bash
ollama pull mistral
ollama pull mxbai-embed-large

local_restaurant_chatAI/
├── main.py                 # Script principale per l'interfaccia utente
├── vector.py               # Gestione del database vettoriale
├── realistic_restaurant_reviews.csv  # Dataset delle recensioni
├── requirements.txt        # Dipendenze Python
├── README.md               # Questo file
└── chrome_langchain_db/    # Cartella del database vettoriale (generata automaticamente)

Dataset delle Recensioni
Il progetto utilizza un file CSV con questo formato:

Title	Review | Rating	| Date
Ottima esperienza	La pizza era croccante e...	| 5	| 2024-05-15
Servizio lento	Buone pizze ma il servizio...	| 3	| 2024-04-22

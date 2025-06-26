# 🍕 AI-Powered Pizza Restaurant Assistant - Assistente PizzerIA

Questo progetto implementa un assistente AI specializzato in una pizzeria, capace di rispondere alle domande dei clienti basandosi su recensioni reali archiviate in un database vettoriale.

## Caratteristiche Principali
- Recupero di recensioni pertinenti usando embedding vettoriali
- Generazione di risposte contestuali con modelli LLM (Mistral via Ollama)
- Interfaccia grafica conversazionale in tempo reale
- Persistenza del database vettoriale per performance ottimizzate

## Tecnologie Utilizzate
- **Ollama** - Per l'esecuzione locale di modelli LLM
- **LangChain** - Framework per applicazioni basate su LLM
- **ChromaDB** - Database vettoriale open-source
- **Pandas** - Elaborazione del dataset delle recensioni
- **Streamlit** - Per l'interfaccia web

## Prerequisiti

1. **Ollama installato**: [Download Ollama](https://ollama.ai/)
2. Modelli Ollama necessari:
```
ollama pull mistral
ollama pull mxbai-embed-large
```
# Struttura del progetto

local_restaurant_chatAI/
├── main.py                 # Script principale con input-output da terminale
├── main.py                 # Script principale per l'interfaccia utente
├── vector.py               # Gestione del database vettoriale
├── realistic_restaurant_reviews.csv  # Dataset delle recensioni
├── requirements.txt        # Dipendenze Python
├── README.md               # Questo file
└── chrome_langchain_db/    # Cartella del database vettoriale (generata automaticamente)

# Dataset delle Recensioni
Il progetto utilizza un file CSV con questo formato:

| Title             | Review                          | Rating | Date       |
|-------------------|---------------------------------|--------|------------|
| Ottima esperienza | La pizza era croccante e...     | 5      | 2024-05-15 |
| Servizio lento    | Buone pizze ma il servizio...   | 3      | 2024-04-22 |

## Come avviare il progetto
avviare due terminali, uno dove far partire Ollama
```
ollama serve
```
e nell'altro avviare app.py se si vuole la versione con interfaccia grafica tramite streamlit
```
streamlit run app.py
```
altrimenti per la classica interfaccia da terminale
```
python main.py
```

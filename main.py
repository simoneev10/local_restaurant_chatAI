from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="mistral", temperature=0.1)

template = """
Sei un esperto nel rispondere a domande su una pizzeria.
 Rispondi alle domande dei clienti basandoti SOLO sulle recensioni qui sotto.
Se la domanda non riguarda la pizzeria o non ci sono recensioni pertinenti, rispondi educatamente che non puoi aiutare.

RECENSIONI PERTINENTI:
{reviews}

DOMANDA DEL CLIENTE: 
{question}

ISTRUZIONI:
- Rispondi in italiano, in modo cortese e professionale
- Se rilevante, menziona valutazioni e date delle recensioni
- Non inventare dettagli non presenti nelle recensioni
- Per domande su menu/prezzi, specifica che queste info non sono nelle recensioni
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("(q per uscire)\nFai la tua domanda: ")
    print("\n\n")
    if question == "q":
        break
    
    # Recupera i documenti
    documents = retriever.invoke(question)
    
    # Formatta le recensioni in modo leggibile
    formatted_reviews = []
    for doc in documents:
        review_text = (
            f"Recensione: {doc.page_content}\n"
            f"Voto: {doc.metadata['rating']}/5 - Data: {doc.metadata['date']}\n"
            "---"
        )
        formatted_reviews.append(review_text)
    
    reviews_text = "\n\n".join(formatted_reviews)
    
    result = chain.invoke({"reviews": reviews_text, "question": question})
    print(result)
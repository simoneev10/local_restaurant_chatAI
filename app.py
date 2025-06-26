import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Configurazione pagina
st.set_page_config(
    page_title="Assistente PizzerIA",
    page_icon="🍕",
    layout="centered"
)

@st.cache_resource
def load_model():
    return Ollama(model="mistral", temperature=0.1)

@st.cache_resource
def load_prompt_chain():
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
    return prompt | model

model = load_model()
chain = load_prompt_chain()

# Inizializzazione stato sessione
if "reviews_text" not in st.session_state:
    st.session_state.reviews_text = ""
if "last_question" not in st.session_state:
    st.session_state.last_question = ""

# Interfaccia
st.title("🍕 Assistente PizzerIA")
st.divider()

with st.container(border=True):
    question = st.text_input(
        "Fai la tua domanda sulla pizzeria:",
        placeholder="Es: Quali sono le pizze più apprezzate?",
        key="user_input"
    )
    submit_btn = st.button("Invia", type="primary")

if submit_btn or question:
    if not question.strip():
        st.warning("Per favore inserisci una domanda")
        st.stop()
    
    st.session_state.last_question = question
    
    with st.spinner("🔍 Cerco informazioni nelle recensioni..."):
        # Recupero documenti
        documents = retriever.invoke(question)
        formatted_reviews = []
        
        for doc in documents:
            review_text = (
                f"**Recensione:** {doc.page_content}\n\n"
                f"⭐ **Voto:** {doc.metadata['rating']}/5  \n"
                f"📅 **Data:** {doc.metadata['date']}\n"
                "---"
            )
            formatted_reviews.append(review_text)
        
        st.session_state.reviews_text = "\n\n".join(formatted_reviews)
    
    with st.status("🧠 Sto elaborando la risposta...", expanded=True) as status:
        result = chain.invoke({
            "reviews": st.session_state.reviews_text, 
            "question": question
        })
        status.update(label="Risposta pronta!", state="complete")
    
    st.subheader("Risposta:")
    st.markdown(result)

# Footer
st.divider()
st.caption("Assistente AI basato su recensioni della pizzeria - Powered by Ollama Mistral")
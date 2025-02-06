import streamlit as st
from utils.common import initialize_page

lang = initialize_page()

def main():
    # Translations dictionary
    translations = {
        "English": {
            "title": "Verified Documents",
            "list_title": "List of Verified Documents",
            "no_documents": "No verified document found.",
            "risk_low": "Low Sensitivity",
            "risk_medium": "Medium Sensitivity",
            "risk_high": "High Sensitivity",
            "document_name": "Document Name",
            "assessment": "Overall Assessment",
            "model": "Model"
        },
        "Deutsch": {
            "title": "Geprüfte Dokumente",
            "list_title": "Liste der geprüften Dokumente",
            "no_documents": "Keine geprüften Dokumente gefunden.",
            "risk_low": "Niedrige Sensitivität",
            "risk_medium": "Mittlere Sensitivität",
            "risk_high": "Hohe Sensitivität",
            "document_name": "Dokumentname",
            "assessment": "Gesamtbewertung",
            "model": "Modell"
        },
        "Français": {
            "title": "Documents vérifiés",
            "list_title": "Liste des documents vérifiés",
            "no_documents": "Aucun document vérifié trouvé.",
            "risk_low": "Sensibilité faible",
            "risk_medium": "Sensibilité moyenne",
            "risk_high": "Sensibilité élevée",
            "document_name": "Nom du document",
            "assessment": "Évaluation globale",
            "model": "Modèle"
        }
    }

    # Choose the appropriate translation based on the selected language
    t = translations[lang]

    st.title(t["title"])
    
    # Retrieve processed documents from session_state
    processed_docs = st.session_state.get("processed_docs", {})
    
    if processed_docs:
        doc_list = []
        for doc_name, doc_data in processed_docs.items():
            # Compute overall risk based on sensitive sections
            sensitive_sections = doc_data.get("sensitive_sections", [])
            overall = "low"  # default risk level
            
            if sensitive_sections:
                for section in sensitive_sections:
                    cat = section.get("category", "").lower()
                    if "secret" in cat or "security" in cat:
                        overall = "high"
                        break
                    elif "personal" in cat:
                        overall = "medium"
            
            # Map to a translated description with icon
            risk_dict = {
                "low": t["risk_low"],
                "medium": t["risk_medium"],
                "high": t["risk_high"]
            }
            icon_dict = {"low": "🟢", "medium": "🟠", "high": "🔴"}
            assessment = f"{icon_dict.get(overall, '')} {risk_dict.get(overall, overall)}"
            
            model_used = doc_data.get("model", "Unknown")
            doc_list.append({
                t["document_name"]: doc_name,
                t["assessment"]: assessment,
                t["model"]: model_used,
            })
        
        st.markdown(f"### {t['list_title']}")
        st.table(doc_list)
    else:
        st.info(t["no_documents"])

if __name__ == "__main__":
    main()
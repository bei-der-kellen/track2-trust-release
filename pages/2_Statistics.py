import streamlit as st
from utils.common import initialize_page
import plotly.express as px
import pandas as pd
from collections import Counter

def main():
    # Initialize page
    lang = initialize_page()
    
    # Translations
    translations = {
        "English": {
            "title": "Document Statistics",
            "no_data": "No documents processed yet.",
            "risk_distribution": "Risk Level Distribution",
            "sensitivity_types": "Types of Sensitive Information",
            "docs_by_model": "Documents Processed by Model",
            "total_docs": "Total Documents Processed",
            "avg_sensitive": "Average Sensitive Sections per Document",
        },
        "Deutsch": {
            "title": "Dokumentenstatistik",
            "no_data": "Noch keine Dokumente verarbeitet.",
            "risk_distribution": "Verteilung der Risikoniveaus",
            "sensitivity_types": "Arten sensibler Informationen",
            "docs_by_model": "Verarbeitete Dokumente nach Modell",
            "total_docs": "Insgesamt verarbeitete Dokumente",
            "avg_sensitive": "Durchschnittliche sensible Abschnitte pro Dokument",
        },
        "Français": {
            "title": "Statistiques des documents",
            "no_data": "Aucun document traité pour le moment.",
            "risk_distribution": "Distribution des niveaux de risque",
            "sensitivity_types": "Types d'informations sensibles",
            "docs_by_model": "Documents traités par modèle",
            "total_docs": "Total des documents traités",
            "avg_sensitive": "Sections sensibles moyennes par document",
        }
    }

    t = translations[lang]
    
    st.title(t["title"])

    # Get processed documents from session state
    docs = st.session_state.get("processed_docs", {})
    
    if not docs:
        st.info(t["no_data"])
        return

    # Calculate statistics
    total_docs = len(docs)
    
    # Risk level distribution
    risk_levels = []
    sensitivity_types = []
    models_used = []
    
    for doc_name, doc_data in docs.items():
        # Calculate risk level
        overall = "Low"
        if doc_data['sensitive_sections']:
            for section in doc_data['sensitive_sections']:
                cat = section['category'].lower()
                if "secret" in cat or "security" in cat:
                    overall = "High"
                    break
                elif "personal" in cat:
                    overall = "Medium"
                    
        risk_levels.append(overall)
        
        # Collect sensitivity types
        for section in doc_data['sensitive_sections']:
            sensitivity_types.append(section['category'])
            
        # Collect models used
        models_used.append(doc_data.get('model', 'Unknown'))

    # Create visualizations with two columns
    col1, col2 = st.columns(2)  # Changed to 2 columns
    
    with col1:
        # Risk level distribution
        risk_df = pd.DataFrame(Counter(risk_levels).items(), 
                             columns=['Sensitivity Level', 'Count'])
        fig1 = px.pie(
            risk_df,
            values='Count',
            names='Sensitivity Level',
            title=t["risk_distribution"],
            color='Sensitivity Level',  # Added color parameter
            color_discrete_map={"High": "red", "Medium": "orange", "Low": "green"}  # Define the custom color mapping
        )
        # Adjust figure size and margins
        fig1.update_layout(
            height=300,
            width=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        # Sensitivity types distribution
        if sensitivity_types:
            sensitivity_df = pd.DataFrame(Counter(sensitivity_types).items(), 
                                       columns=['Type', 'Count'])
            fig2 = px.bar(sensitivity_df, x='Type', y='Count', 
                         title=t["sensitivity_types"])
            # Adjust figure size and margins
            fig2.update_layout(
                height=300,
                width=300,
                margin=dict(l=20, r=20, t=40, b=20),
                xaxis_tickangle=-45  # Angle the x-axis labels for better readability
            )
            st.plotly_chart(fig2, use_container_width=True)

    # Summary metrics in their own row
    st.markdown("---")  # Add a separator
    col1, col2 = st.columns(2)
    with col1:
        st.metric(t["total_docs"], total_docs)
    with col2:
        avg_sensitive = sum(len(doc['sensitive_sections']) for doc in docs.values()) / total_docs
        st.metric(t["avg_sensitive"], f"{avg_sensitive:.1f}")

if __name__ == "__main__":
    main() 
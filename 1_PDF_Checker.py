import streamlit as st
from sidebar import render_sidebar_logo
# Other imports...

def main():
    render_sidebar_logo()
    
    # Added language selection widget with session state persistence
    languages = {"🇬🇧 English": "English", "🇩🇪 Deutsch": "Deutsch", "🇫🇷 Français": "Français"}
    default_index = 0
    if "lang" in st.session_state:
        lang_values = list(languages.values())
        try:
            default_index = lang_values.index(st.session_state.lang)
        except ValueError:
            default_index = 0
    lang_choice = st.sidebar.selectbox("Select Language", list(languages.keys()), index=default_index)
    st.session_state.lang = languages[lang_choice]
    lang = st.session_state.lang
    
    # Translations for PDF Checker page
    translations = {
         "English": {
             "checker_title": "PDF Checker",
             "upload_label": "Upload your PDF file",
             "instruction": "Select a PDF file to check for sensitive information.",
             "overall_assessment": "Overall Sensitivity",
             "sensitivity_low": "Low Sensitivity",
             "sensitivity_medium": "Medium Sensitivity",
             "sensitivity_high": "High Sensitivity"
         },
         "Deutsch": {
             "checker_title": "PDF-Prüfer",
             "upload_label": "Laden Sie Ihre PDF-Datei hoch",
             "instruction": "Wählen Sie eine PDF-Datei aus, um auf sensitive Informationen zu prüfen.",
             "overall_assessment": "Gesamtsensitivität",
             "sensitivity_low": "Niedrige Sensitivität",
             "sensitivity_medium": "Mittlere Sensitivität",
             "sensitivity_high": "Hohe Sensitivität"
         },
         "Français": {
             "checker_title": "Vérificateur de PDF",
             "upload_label": "Téléchargez votre PDF",
             "instruction": "Sélectionnez un fichier PDF pour vérifier la présence d'informations sensibles.",
             "overall_assessment": "Sensibilité globale",
             "sensitivity_low": "Sensibilité faible",
             "sensitivity_medium": "Sensibilité moyenne",
             "sensitivity_high": "Sensibilité élevée"
         }
    }
    t = translations.get(lang, translations["English"])

    st.title(t["checker_title"])
    st.write(t["instruction"])

    uploaded_file = st.file_uploader(t["upload_label"], type=["pdf"])
    if uploaded_file:
        # Here you would process the PDF and determine the sensitivity level
        # For now, let's assume we have a function that returns 'low', 'medium', or 'high'
        sensitivity_level = 'low'  # This should be replaced with actual logic
        
        # Map the sensitivity level to the translated text
        sensitivity_mapping = {
            'low': t["sensitivity_low"],
            'medium': t["sensitivity_medium"],
            'high': t["sensitivity_high"]
        }
        
        overall_sens = sensitivity_mapping.get(sensitivity_level, t["sensitivity_low"])
        st.subheader(t["overall_assessment"])
        st.write(overall_sens)

if __name__ == "__main__":
    main() 
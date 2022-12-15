import streamlit as st
from needleman_wunsch_bioinformatica import Needleman_Wunsch
from Swiss_prot import Swiss_prot
from io import StringIO

nav = st.sidebar.radio("Choose operation",
                       ["Needleman-Wunsch", "Swiss-prot"])

first, last = st.columns(2)

# ===============================================================================
if nav == "Needleman-Wunsch":
    side, beside = st.columns(2)
    with side:
        first.title("Needleman Wunsch")
    with beside:
        last.image("images/img2.png")

    sequence_1 = first.text_input('Enter sequence number 1', '').upper()
    sequence_2 = first.text_input('Enter sequence number 2', '').upper()

    if (first.button("Start The Process")):
        output = Needleman_Wunsch(sequence_1, sequence_2)
        first.write(output[0])
        first.write(output[1])

# ===============================================================================
elif nav == "Swiss-prot":
    side, beside = st.columns(2)
    with side:
        first.title("Swiss prot")
    with beside:
        last.image("images/img1.png")

    uploaded_file = first.file_uploader("Upload a Swiss prot file")
    string_file = ''
    if uploaded_file is not None:
        string_file = StringIO(uploaded_file.getvalue().decode("utf-8"))

    obj = Swiss_prot(string_file)

    options = ["Identification", "Accession number(s)", "Date", "Description", "Gene name(s)", "Organism species",
               "Organelle", "Organism classification", "Reference info", "Comments or notes attached",
               "Database cross-references", "Keywords", "Feature table data", "Sequence"]

    options_functions = {"Identification": obj.get_ID(), "Accession number(s)": obj.get_AC(), "Date": obj.get_DT(),
                         "Description": obj.get_DE(), "Gene name(s)": obj.get_GN(), "Organism species": obj.get_OS(),
                         "Organelle": obj.get_OG(), "Organism classification": obj.get_OC(),
                         "Reference info": obj.get_RN(), "Comments or notes attached": obj.get_CC(),
                         "Database cross-references": obj.get_DR(), "Keywords": obj.get_KW(),
                         "Feature table data": obj.get_FT(), "Sequence": obj.get_SQ()}

    choosed = first.selectbox("Choose which data you want to display", options, index=0)
    first.write(options_functions[choosed])

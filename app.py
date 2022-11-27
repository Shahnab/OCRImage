import sys # System-specific parameters and functions
import easyocr as ocr  # OCR
import streamlit as st  # web app
from streamlit import cli as stcli # cli web app
from PIL import Image  # opening images
import numpy as np  # for array conversions


st.set_page_config(
    page_title="Recognition",
    page_icon="",
    layout="wide",
    menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "# Text recognition in 83 languages"
    }
)


@st.cache
def load_model(lang):
    return ocr.Reader([lang], model_storage_directory=".")


def main():
    st.title("OCR Image Recognizer Engine")
    st.subheader("Recognizing text from an image")
    st.caption("For optical character recognition, you must select from the list on the left side the language corresponding to the language of the text")
    st.markdown("Demo files for uploading- [link](https://drive.google.com/drive/folders/1Ije6E3w2ygyXYHdxxDo32SlbLQ6AoM2p?usp=sharing)")

    image = st.file_uploader(
        label="Upload Image", type=["png", "jpg", "jpeg"]
        )

    st.sidebar.write("About:")
    st.sidebar.caption("Optical character recognition (OCR) or Text recognition extracts and repurposes data from scanned documents, camera images and image-only pdfs")
    st.sidebar.caption("OCR can single out letters on the image, puts them into words and then puts the words into sentences, thus enabling access to and editing of the original content")
    st.sidebar.caption("Eliminates the need for manual data entry")

    langs = {
        "Abaza": "abq",
        "Adyghe": "ady",
        "Afrikaans": "af",
        "Angina": "ang",
        "Arabic": "ar",
        "Assamese": "as",
        "Avarsky": "ava",
        "Azerbaijani": "az",
        "Belarusian": "be",
        "Bulgarian": "bg",
        "Bihari": "bh",
        "Bhojpuri": "bho",
        "Bengali": "bn",
        "Bosnian": "bs",
        "Simplified Chinese": "ch_sim",
        "Traditional Chinese": "ch_tra",
        "Chechen": "che",
        "Czech": "cs",
        "Welsh": "cy",
        "Danish": "da",
        "Dargwa": "dar",
        "German": "de",
        "English": "en",
        "Spanish": "es",
        "Estonian": "et",
        "Persian (Farsi)": "fa",
        "French": "fr",
        "Irish": "ga",
        "Goan Konkani": "gom",
        "Hindi": "hi",
        "Croatian": "hr",
        "Hungarian": "hu",
        "Indonesian": "id",
        "Ingush": "inh",
        "Icelandic": "is",
        "Italian": "it",
        "Japanese": "ja",
        "Kabardian": "kbd",
        "Kannada": "kn",
        "Korean": "ko",
        "Kurdish": "ku",
        "Latin": "la",
        "Lak": "lbe",
        "Lezghian": "lez",
        "Lithuanian": "lt",
        "Latvian": "lv",
        "Magahi": "mah",
        "Maithili": "mai",
        "Maori": "mi",
        "Mongolian": "mn",
        "Marathi": "mr",
        "Malay": "ms",
        "Maltese": "mt",
        "Nepali": "ne",
        "Newari": "new",
        "Dutch": "nl",
        "Norwegian": "no",
        "Occitan": "oc",
        "Pali": "pi",
        "Polish": "pl",
        "Portuguese": "pt",
        "Romanian": "ro",
        "Russian": "ru",
        "Serbian (cyrillic)": "rs_cyrillic",
        "Serbian (latin)": "rs_latin",
        "Nagpuri": "sck",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Albanian": "sq",
        "Swedish": "sv",
        "Swahili": "sw",
        "Tamil": "ta",
        "Tabassaran": "tab",
        "Telugu": "te",
        "Thai": "th",
        "Tajik": "tjk",
        "Tagalog": "tl",
        "Turkish": "tr",
        "Uyghur": "ug",
        "Ukranian": "uk",
        "Urdu": "ur",
        "Uzbek": "uz",
        "Vietnamese": "vi",
    }


    label_langs = st.sidebar.title('Language Selection Panel')
    feature_choice = st.sidebar.selectbox(
        "Specify the language of the text for recognition", list(langs.keys())
    )


    info_text = st.sidebar.text('83 languages available')
    if image is not None:
        input_image = Image.open(image)
        st.image(input_image)
        reader = load_model(lang=langs.get(feature_choice))
        with st.spinner("Recognizing..."):
            result = reader.readtext(
                np.array(input_image)
            )
            out_str = " "
            list_text = [ftext[1] for ftext in result]
            st.title("Loading result:")
            with open(".txt", 'w', encoding='utf-8', errors='ignore') as file:
                file.write(out_str.join(list_text))
            result_file = open(".txt", 'rb')
            st.download_button('Download recognized text', result_file)

            st.title("Recognized image as text:")

  
            futext = st.write(out_str.join(list_text))
            st.title("Recognized image in the list:")
            result_text = [text[1] for text in result]
            st.write(result_text)
    else:
        st.info(
            "Please select a language and upload an image for recognition..."
        )
    


if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

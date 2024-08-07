import streamlit as st
from streamlit_option_menu import option_menu
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib.parse

# Configuración de la página
st.set_page_config(page_title="Imanol Asolo portfolio", page_icon="🌟", layout="wide")

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url({'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzvgDLROm4JxrqhSyr-lE6whR4d5szAFJtZw&s'}) no-repeat center center fixed;
        background-size: contain;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Crear una barra de navegación superior
selected = option_menu(
    menu_title='Imanol Asolo',
    options=["Home", "About", "Contact", "Chat with Imanol"],  # Opciones del menú
    icons=["house", "info-circle", "envelope"],  # Iconos para las opciones
    menu_icon="cast",  # Icono del menú
    default_index=0,  # Opción seleccionada por defecto
    orientation="horizontal",  # Menú horizontal
)

# Mostrar contenido según la selección en la barra de navegación
if selected == "Home":
    st.title("Who is Imanol Asolo")
    col1, col2 = st.columns(2)
    with col1:
        st.success("A passionate full stack developer and Scrum Master at CodeCodix, where innovation meets excellence. With a unique focus on creating advanced technological solutions for the healthcare sector and beyond, Imanol leads projects with strategic vision and an unwavering commitment to quality. From implementing AI tools to managing public relations and social media, Imanol transforms ideas into impactful realities, ensuring that each project not only meets but exceeds expectations. Explore and discover how technology can change the world!")
    with col2:
        # URL de tu video en YouTube
        video_url = "https://youtu.be/4k81Pg-odLg?si=7KbGtk7TcVYb-6LN"

        # URL de la miniatura
        thumbnail_url = "image1.png"

        # Crear una función para mostrar el video
        def show_video():
            st.video(video_url)

        # Mostrar la miniatura como un botón
        if st.button("Watch Video", key="watch_video_button"):
            show_video()
        else:
            st.image(thumbnail_url, width=300, caption="Click the button to watch the video!")

elif selected == "About":
    st.title("Info about Imanol Asolo")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("Projects.")
        # Añadir un selector para los proyectos
        project_option = st.selectbox("Select a project to download the PDF:", ["Raptor_Eye", "Botarmy_hub", "AI_Medicare"])

        # Diccionario de PDFs
        pdfs = {
            "Raptor_Eye": "Raptor_Eye_pres.pdf",
            "Botarmy_hub": "Botarmy_pres.pdf",
            "AI_Medicare": "AI_medicare_pres.pdf",
            
        }

        # Descargar el PDF seleccionado
        if st.button("Download PDF", key="download_project_pdf_button"):
            pdf_path = pdfs[project_option]
            with open(pdf_path, "rb") as file:
                btn = st.download_button(
                    label="Download",
                    data=file,
                    file_name=pdf_path.split("/")[-1],
                    mime="application/pdf"
                )
    with col2:
        st.warning('Mostly used Stack')
        # Añadir un selector para los stacks
        stack_option = st.selectbox("Select a stack to learn more about:", ["PYTHON", "JAVASCRIPT", "STREAMLIT", "REACT", "MERN", "PERN", "DJANGO", "FLASK", "VUE", "NUXT"])

        # Diccionario de descripciones
        stack_descriptions = {
            "PYTHON": "Python is a versatile and powerful programming language used for web development, data analysis, artificial intelligence, scientific computing, and more. Imanol Asolo has extensive experience in Python, utilizing it to build robust and scalable applications.",
            "JAVASCRIPT": "JavaScript is a dynamic scripting language used to create interactive and dynamic web content. Imanol Asolo is proficient in JavaScript, enabling the creation of responsive and engaging user interfaces.",
            "STREAMLIT": "Streamlit is an open-source app framework for creating and sharing data applications. Imanol leverages Streamlit to build interactive web applications for data science and machine learning projects, enhancing user experience and accessibility.",
            "REACT": "React is a popular JavaScript library for building user interfaces, particularly single-page applications. Imanol uses React to develop fast and interactive front-end applications, ensuring a seamless user experience.",
            "MERN": "The MERN stack consists of MongoDB, Express.js, React, and Node.js. Imanol utilizes the MERN stack to create full-stack JavaScript applications, providing end-to-end development solutions.",
            "PERN": "The PERN stack includes PostgreSQL, Express.js, React, and Node.js. Imanol employs the PERN stack for developing scalable and robust web applications with efficient data management.",
            "DJANGO": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Imanol uses Django to build secure and maintainable web applications quickly and efficiently.",
            "FLASK": "Flask is a lightweight WSGI web application framework in Python. Imanol chooses Flask for its simplicity and flexibility when developing smaller web applications and APIs.",
            "VUE": "Vue.js is a progressive JavaScript framework for building user interfaces. Imanol uses Vue to create versatile and performant front-end applications with a smooth learning curve.",
            "NUXT": "Nuxt.js is a framework built on top of Vue.js that simplifies the development of server-side rendered applications. Imanol leverages Nuxt to build SEO-friendly and performant web applications."
        }

        # Mostrar la descripción del stack seleccionado
        st.warning(stack_descriptions[stack_option])
    
    with col3:
        st.info('Check my latest CV')
        pdfs = {
            "PDF_Imanol1": "CV_resume.pdf",
        }

        # Descargar el PDF seleccionado
        if st.button("Download CV", key="download_cv_button"):
            pdf_path = pdfs["PDF_Imanol1"]
            with open(pdf_path, "rb") as file:
                btn = st.download_button(
                    label="Download",
                    data=file,
                    file_name=pdf_path.split("/")[-1],
                    mime="application/pdf"
                )

elif selected == "Contact":
    st.title("Contact")
    st.write("This is the contact page.")
    
    with st.form(key='contact_form'):
        contact_reason = st.selectbox("Reason for contact:", ["Project Inquiry", "Employment", "Tutoring", "General Information"])
        contact_info = st.text_input("Your contact info (WhatsApp or email):")
        message = st.text_area("Your message:")
        
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            # Enviar el correo electrónico
            email_recipient = "jjusturi@gmail.com"
            email_subject = f"Contact Form Submission: {contact_reason}"
            email_body = f"Reason: {contact_reason}\nContact Info: {contact_info}\nMessage: {message}"
            
            msg = MIMEMultipart()
            msg['From'] = contact_info
            msg['To'] = email_recipient
            msg['Subject'] = email_subject
            msg.attach(MIMEText(email_body, 'plain'))
            
            try:
                # Configurar el servidor SMTP
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(st.secrets["smtp"]["username"], st.secrets["smtp"]["password"])
                text = msg.as_string()
                server.sendmail(contact_info, email_recipient, text)
                server.quit()
                st.success("Your message has been sent successfully!")
            except Exception as e:
                st.error(f"Error sending message: {e}")

            # Generar enlace de WhatsApp
            whatsapp_message = f"Reason: {contact_reason}\nContact Info: {contact_info}\nMessage: {message}"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_link = f"https://wa.me/593099351023?text={encoded_message}"
            
            st.markdown(f"Or contact me via WhatsApp: [Click here](https://wa.me/593099351023?text={encoded_message})")

elif selected == "Chat with Imanol":
    st.title('Chat with my AI')
    # Agregar el botón que abre el enlace en una nueva pestaña
    st.markdown(
        """
        <a href="https://aiprofilevcard.streamlit.app/" target="_blank">
            <button style="padding: 10px 20px; font-size: 16px; cursor: pointer; background-color: #007BFF; color: white; border: none; border-radius: 5px;">
                Chat with AI
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )


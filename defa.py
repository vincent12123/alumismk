import streamlit as st
import re
import os

def update_static_references(file_content, directory_name, new_directory_name):
    # Define the regex pattern with the directory name provided by the user
    pattern = rf'({re.escape(directory_name)})/([\w\-./]+)'

    # Replace the found paths with the Flask url_for syntax using the new directory name
    updated_content = re.sub(pattern, lambda x: "{{ url_for('static', filename='" + new_directory_name + "/" + x.group(2) + "') }}", file_content)
    return updated_content

def main():
    st.title("Static Reference Updater")

    # User input for directory names
    directory_name = st.text_input("Enter the original directory name for the paths:")
    new_directory_name = st.text_input("Enter the new path for the directory:")

    # File uploader
    uploaded_file = st.file_uploader("Choose a file", type=['html'])
    if uploaded_file is not None and directory_name and new_directory_name:
        file_content = uploaded_file.getvalue().decode("utf-8")
        updated_content = update_static_references(file_content, directory_name, new_directory_name)

        # Get the base name of the uploaded file
        base_name = os.path.splitext(uploaded_file.name)[0]

        # Display or download
        st.text_area("Updated File Content", updated_content, height=300)
        st.download_button("Download Updated File", updated_content, file_name=f"{base_name}_update.html")

if __name__ == "__main__":
    main()
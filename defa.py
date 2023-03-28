import pandas as pd
import streamlit as st

# Load data from CSV file
df = pd.read_csv("alumi.csv")
def intro():
    import streamlit as st
    st.write("# Data Alumi SMK Karya Bangsa")
    st.sidebar.success("Silahkan Pilih.")
    st.markdown(
        ###
        
    )
    
st.write(df)
# Count number of students who are already working
num_working = df[df["Apakah sudah bekerja"] == "Ya"]["Nama Siswa"].count()

# Display result in Streamlit app
st.write("Jumlah siswa yang sudah bekerja:", num_working)
# Count number of students in each department who answered "perhotelan", "tsm", or "rpl"
perhotelan_count = df[(df["Jurusan"] == "Perhotelan") & (df["Apakah sudah bekerja"] == "Ya")]["Nama Siswa"].count()
tsm_count = df[(df["Jurusan"] == "Teknik Sepeda Motor") & (df["Apakah sudah bekerja"] == "Ya")]["Nama Siswa"].count()
rpl_count = df[(df["Jurusan"] == "Rekayasa Perangkat Lunak") & (df["Apakah sudah bekerja"] == "Ya")]["Nama Siswa"].count()

# Display result in Streamlit app
st.write("Jumlah siswa yang sudah bekerja di jurusan perhotelan:", perhotelan_count)
st.write("Jumlah siswa yang sudah bekerja di jurusan tsm:", tsm_count)
st.write("Jumlah siswa yang sudah bekerja di jurusan rpl:", rpl_count)

# Count number of students who answered the questionnaire
num_respondents = df["Nama Siswa"].count()

# Display result in Streamlit app
st.write("Jumlah siswa yang menjawab kuesioner:", num_respondents)

# Group data by department and count number of students who answered the questionnaire
respondents_by_dept = df.groupby("Jurusan")["Nama Siswa"].count()

# Display result in Streamlit app
st.write("Jumlah siswa yang menjawab kuesioner per jurusan:")
st.write(respondents_by_dept)

# Filter data by students who haven't worked and want to continue studying
df_filtered = df[df["Apa Kuliah"] == "Ya"]

# Group filtered data by department and count number of students who want to continue studying
continue_studies_by_dept = df_filtered.groupby("Jurusan")["Nama Siswa"].count()

# Display result in Streamlit app
st.write("Jumlah siswa yang ingin melanjutkan kuliah per jurusan:")
st.write(continue_studies_by_dept)

# Group filtered data by department and get list of students who want to continue studying
continue_studies_by_dept = df_filtered.groupby("Jurusan")["Nama Siswa"].apply(list)

# Display result in Streamlit app
st.write("Daftar nama siswa yang ingin melanjutkan kuliah per jurusan:")
st.write(continue_studies_by_dept)

# Filter data by students who haven't worked and want to continue studying
df_filtered = df[df["Apa Kuliah"] == "Ya"]

# Group filtered data by department and get list of students who want to continue studying
continue_studies_by_dept = df_filtered.groupby("Jurusan")[["Nama Siswa", "Tempat Kuliah"]].apply(lambda x: x.values.tolist())

# Display result in Streamlit app
st.write("Daftar nama siswa yang ingin melanjutkan kuliah per jurusan:")
st.write(continue_studies_by_dept)

# Filter data by students who haven't worked
df_filtered = df[df["Apa Kuliah"] == "Tidak"]

# Select columns "Nama Siswa" and "Apa Kuliah" from filtered data
result = df_filtered[["Nama Siswa","Jurusan", "Berikan penjelasan / keterangan"]]

# Display result in Streamlit app
st.write("Daftar siswa yang tidak kuliah  dan Alasan:")
st.write(result)
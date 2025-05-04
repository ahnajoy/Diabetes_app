import streamlit as st
import pandas as pd

st.title('Diabetes Melitus')
teks1 =  "Diabetes melitus merupakan salah satu penyakit dengan tingkat kematian tinggi. Dikutip dari World Health Organization (WHO), Diabetes menduduki peringkat ke-8 sebagai penyakit paling berbahaya di dunia. Salah satu penyebab mengapa penyakit ini terus meningkat di tengah masyarakat adalah karena gejala penyakit diabetes yang cukup umum, seperti pengeluaran urine berlebihan, penglihatan mata kabur, serta penurun berat badan. Hal ini membuat masyarakat tidak terlalu memperhatikan bahaya yang ditimbulkan penyakit ini."
st.markdown(
    f"""
    <div style="text-align: justify; text-justify: inter-word;">
        {teks1}
    </div>
    """,
    unsafe_allow_html=True
)


st.write("\n")
st.subheader("Klasifikasi Diabetes", anchor=False)

teks2 = "Diabetes dibedakan menjadi dua tipe, yang pertama adalah diabetes tipe 1. Klasifikasi diabetes tipe 1 ini biasanya dikaitkan oleh kondisi autoimun. Di mana, sistem imun yang mulanya melindungi tubuh, justru malah menyerang tubuh, salah satunya adalah pankreas yang menjadi tempat produksi insulin yang berfungsi dalam mengatur kadar glukosa tubuh. Klasifikas selanjutnya disebut dengan diabetes tipe 2, penyebab dari tipe ini memang beragam, beberapa di antaranya adalah obesitas, penuaan, atau memiliki anggota keluarga dengan riwayat diabetes."
st.markdown(
    f"""
    <div style="text-align: justify; text-justify: inter-word;">
        {teks2}
    </div>
    """,
    unsafe_allow_html=True
)


st.write("\n")
st.subheader("Bahaya Diabetes", anchor=False)

teks3 = "Jika diabetes terlambat dideteksi, penderita dapat mengalami penyakit yang lebih serius, seperti penyakit jantung, gagal ginjal, hingga stroke. Selain itu, penderita diabetes melitus memiliki kemungkinan kerusakan anggota tubuh yang sangat tinggi dan sulit untuk sembuh kembali. Salah satu area yang sering mengalami kerusakan adalah kaki, lebih jauh, kerusakan ini dapat berakhir dengan amputasi."
st.markdown(
    f"""
    <div style="text-align: justify; text-justify: inter-word;">
        {teks3}
    </div>
    """,
    unsafe_allow_html=True
)


st.write("\n")
st.subheader("Pencegahan Diabetes", anchor=False)

st.write(f"""
* Menjaga pola hidup sehat, salah satunya dengan mencapai berat badan ideal
* Melakukan olahraga minimal 30 menit setiap harinya
* Mengkonsumsi makanan bergizi, serta menghindari memakan makanan yang mengandung gula tinggi, berikut nama-nama gula dalam kemasan makanan:
""")

df = pd.DataFrame({
    "Nama lain gula pada kemasan": ['Agave nectar', 'Dextrose', 'Maltose', 'Brown sugar',
        'Evaporated cane juice', 'Malt syrup', 'Cane crystals',
        'Fructose', 'Maple syrup', 'Cane sugar', 'Fruit juice concentrates',
        'Molasses', 'Coconut sugar', 'Glucose', 'Raw sugar',
        'Corn sweetener', 'High-fructose corn syrup', 'Sucrose',
        'Corn syrup', 'Honey', 'Syrup', 'Crystalline fructose', 'Invert sugar']
}, index=range(1, 24))

df.index.name = 'No'
st.dataframe(df)

st.write("""
- Tidak merokok
""")

st.write('\n')
st.markdown('<span>(Source)</span><span> https://www.who.int/</span>', unsafe_allow_html=True)




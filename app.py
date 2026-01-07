import streamlit as st

st.set_page_config(page_title="Multi Calculator PRO", layout="centered")

st.title("🧠 Multi Calculator App (PRO MODE)")
st.caption("Satu aplikasi, banyak kalkulator | Built with Python + Streamlit")


menu = st.sidebar.radio(
    "Pilih Kalkulator",
    [
        "🧮 Kalkulator Standar",
        "📐 Luas & Keliling",
        "⚖️ BMI Calculator",
        "🔢 Persentase"
    ]
)
if menu == "🧮 Kalkulator Standar":
    st.subheader("🧮 Kalkulator Standar")

    a = st.number_input("Angka pertama", value=0.0)
    b = st.number_input("Angka kedua", value=0.0)
    operasi = st.selectbox("Operasi", ["+", "-", "×", "÷"])

    if st.button("Hitung"):
        if operasi == "+":
            hasil = a + b
        elif operasi == "-":
            hasil = a - b
        elif operasi == "×":
            hasil = a * b
        elif operasi == "÷":
            if b == 0:
                st.error("Tidak bisa dibagi nol")
                hasil = None
            else:
                hasil = a / b

        if hasil is not None:
            st.success(f"Hasil: {hasil}")

elif menu == "📐 Luas & Keliling":
    st.subheader("📐 Kalkulator Luas & Keliling")

    bentuk = st.selectbox("Pilih Bentuk", ["Persegi", "Persegi Panjang"])

    if bentuk == "Persegi":
        sisi = st.number_input("Panjang sisi", min_value=0.0)
        if st.button("Hitung"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"Luas: {luas}")
            st.info(f"Keliling: {keliling}")

    else:
        panjang = st.number_input("Panjang", min_value=0.0)
        lebar = st.number_input("Lebar", min_value=0.0)
        if st.button("Hitung"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas: {luas}")
            st.info(f"Keliling: {keliling}")

elif menu == "⚖️ BMI Calculator":
    st.subheader("⚖️ BMI Calculator")

    berat = st.number_input("Berat badan (kg)", min_value=0.0)
    tinggi = st.number_input("Tinggi badan (cm)", min_value=0.0)

    if st.button("Hitung BMI"):
        if tinggi == 0:
            st.error("Tinggi tidak boleh 0")
        else:
            tinggi_m = tinggi / 100
            bmi = berat / (tinggi_m ** 2)

            st.success(f"BMI kamu: {bmi:.2f}")

            if bmi < 18.5:
                st.info("Status: Kurus")
            elif bmi < 25:
                st.success("Status: Normal")
            elif bmi < 30:
                st.warning("Status: Gemuk")
            else:
                st.error("Status: Obesitas")

elif menu == "🔢 Persentase":
    st.subheader("🔢 Kalkulator Persentase")

    nilai = st.number_input("Nilai awal", value=0.0)
    persen = st.number_input("Persentase (%)", value=0.0)

    if st.button("Hitung Persentase"):
        hasil = nilai * persen / 100
        st.success(f"Hasil: {hasil}")

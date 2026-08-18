## Projek Pendeteksi Emosi Wajah Manusia

### Alur Projek (CRISP-DM)

### 1. Pemahaman Bisnis (Business Understanding)
Tujuan utama dari proyek ini adalah membuat model AI yang dapat mengidentifikasi Ekspresi Wajah Manusia

### 2. Pemahaman Data (Data Understanding)
* **Sumber Data:** Kumpulan gambar wajah manusia yang dikumpulkan dari [Roboflow](https://universe.roboflow.com/emotions-dectection/human-face-emotions)
* **Anotasi:** Setiap gambar di dalam dataset sudah terdapat *bounding box*

### 3. Persiapan Data (Data Preparation)
Data akan diambil hanya anger, sad dan happy, lalu akan diproses dengan dilakukan splitting datanya

### 4. Pemodelan (Modeling)
* **Arsitektur Utama:** YOLOv8
* **Pelatihan:** Model akan melalui pelatihan awal yakni fine-tuning untuk mencari kombinasi terbaik dan hasil fine tuning akan digunakan pada training akhir

### 5. Evaluasi (Evaluation)
Setelah proses pelatihan selesai, model akan memasuki proses TTA untuk memaksimalkan validasi dari modelnya dan akan diperlihatkan juga hasil evaluasianya

### 6. Penyebaran (Deployment)
Model YOLOv8 yang sudah jadi akan dimasukkan ke dalam website

#### Kurva Hasil Training dan Confusion Matrix
<br>
<img width="2400" height="1200" alt="output" src="https://github.com/user-attachments/assets/0fcb8be0-18d9-483a-94f2-4047961245e8" />
<br>
<img width="495" height="555" alt="Screenshot 2026-08-18 135804" src="https://github.com/user-attachments/assets/59296e54-7c7b-4564-b5dd-dea27271564a" />


#### Flowchart dari cara kerja websitenya
<br>
<img width="541" height="792" alt="Untitled Diagram drawio (5)" src="https://github.com/user-attachments/assets/b7b4aeef-728c-4256-b194-0b6b5b274fad" />

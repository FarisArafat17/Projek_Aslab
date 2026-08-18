## Projek Pendeteksi Emosi Wajah Manusia

### Alur Projek (CRISP-DM)

### 1. Business Understanding
Tujuan utama dari proyek ini adalah membuat model AI yang dapat mengidentifikasi Ekspresi Wajah Manusia

### 2. Data Understanding
* **Sumber Data:** Kumpulan gambar wajah manusia yang dikumpulkan dari [Roboflow](https://universe.roboflow.com/emotions-dectection/human-face-emotions)
* **Anotasi:** Setiap gambar di dalam dataset sudah terdapat *bounding box*

### 3. Data Preparation
Data akan diambil hanya anger, sad dan happy, lalu akan diproses dengan dilakukan splitting datanya

### 4. Modeling
* **Arsitektur Utama:** YOLOv8
* **Pelatihan:** Model akan melalui pelatihan awal yakni fine-tuning untuk mencari kombinasi terbaik dan hasil fine tuning akan digunakan pada training akhir

### 5. Evaluation
Setelah proses pelatihan selesai, model akan memasuki proses TTA untuk memaksimalkan validasi dari modelnya dan akan diperlihatkan juga hasil evaluasianya

### 6. Deployment
Model YOLOv8 yang sudah jadi akan dimasukkan ke dalam website

#### Kurva Hasil Training dan Confusion Matrix
<br>
<img width="495" height="555" alt="Screenshot 2026-08-18 135804" src="https://github.com/user-attachments/assets/4f4ae729-5e4c-43a2-bbd4-36abed507361" />
<br>
<img width="2400" height="1200" alt="output" src="https://github.com/user-attachments/assets/74c6cf9a-6760-434d-a952-aadccb587562" />



#### Flowchart dari cara kerja websitenya
<br>
<img width="541" height="792" alt="Untitled Diagram drawio (5)" src="https://github.com/user-attachments/assets/402eef37-2812-41f4-a161-f192fda13890" />

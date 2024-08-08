import cv2
import numpy as np

# Path gambar
image_path = 'trash.jpeg'

# Membaca gambar
image = cv2.imread(image_path)

# Mengonversi gambar ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Mengaplikasikan threshold
thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)

# Menemukan kontur
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Menghitung area total dan area yang terisi
total_area = thresh.shape[0] * thresh.shape[1]
filled_area = sum(cv2.contourArea(contour) for contour in contours)
filling_level = (filled_area / total_area) * 100  # Persentase kepenuhan

# Menampilkan hasil
print(f"Filling Level: {filling_level:.2f}%")

import smtplib
from email.mime.text import MIMEText

def send_notification(filling_level):
    if filling_level > 80:  # Ambang batas 80%
        msg = MIMEText(f"Alert: Trash bin is {filling_level:.2f}% full.")
        msg['Subject'] = 'TEMPAT SAMPAH PENUH!Lakukan Pengambilan Sampah'
        msg['From'] = 'your_email@example.com'
        msg['To'] = 'cleaning_team@example.com'

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)

send_notification(filling_level)
# Menutup jendela gambar
cv2.destroyAllWindows()



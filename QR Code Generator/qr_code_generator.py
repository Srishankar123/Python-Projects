import qrcode

url_needed=input("Enter the url: ").strip()
filename=input("Enter the filename you want to save your qrcode in: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(url_needed)
img= qr.make_image(fill_color="black", back_color="white")
filename_with_ext = f"{filename}.png"
img.save(filename_with_ext)
print(f"QR Code saved as {filename_with_ext}")


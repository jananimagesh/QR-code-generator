import qrcode
img=qrcode.make("https://www.linkedin.com/in/janani-mca2003/")
img.save("my_linkedIn_profile.jpg")
print("created")

import wifi_qrcode_generator as qr


wifi_name = "Purna_Khatri"
password = "Purna@#$!234"
authentication_type = "WPA"  


qr_code = qr.wifi_qrcode(wifi_name, False, authentication_type, password)


qr_code.make_image().show()  

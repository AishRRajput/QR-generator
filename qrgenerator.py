import qrcode

#taking UPI ID as a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAMES&am=Amount&cu=CURRENCY&tn=MESSAGE
#Defining the payment URL based on the URI ID and the payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create qr codes for each payment apps
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the Qr code to image file
phonepe_qr.save('phonepe_qr.png')
phonepe_qr.save('paytm_qr.png')
phonepe_qr.save('google_pay_qr.png')

#Display the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
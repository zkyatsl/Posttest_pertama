# ---- Posttest 1 ----
# --Program konversi satuan berat--

print("="*30)
print('          WELCOME!!!        ')
print("="*30)

Registration = input("Welcome, Information System Students")

print("="*30)

Name = input("Insert name : ")
Nim = input("Insert NIM : ")
Password = input("Insert Password : ")

print("="*50)
print("="*50)

if Password == "123456" : 
  print("Login Succesfull!")
else :
  print("Wrong Password!")

print("="*50)
print("="*50)

Numbers = float(input("Numbers in Kilograms : "))

print("-"*30)
Operation = input("gram, pon, ons : ")
print("-"*30)

if Operation == "gram" :
  Results = Numbers * 1000
  print("The answer is",Results)
elif Operation == "pon" :
  Results = Numbers * 2.20462
  print("The answer is",Results)
elif Operation == "ons" :
  Results = Numbers * 35.274
  print("The answer is",Results)
else :
  print("Unknown Results")

print("="*50)
print("DONE!!!")
print("="*50)

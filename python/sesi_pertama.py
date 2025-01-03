# Libbary random
import random as rd

welcome_message = "WELCOME TO CUYPY GAMES"
Cupy_position = rd.randint(1,4)
# 1 adalah nomor awal dan nomor akhir atau pembatas 4
print("******************************")
print(f"** {welcome_message} **")
print("******************************")

nama_user = input("Masukan Nama : ")
print(f'''Hello {nama_user}! Cobalah kamu perhatikan Goa Di bawah ini 
|_| |_| |_| |_|
''')

pilihan = int(input('Menurut kamu di Goa nomor berapa CUPY berada ? [1 / 2 / 3 / 4] : '))

print(f'Plihan Kamu adalah {pilihan}')

pilihan_2 = str(input(f"Apakah Kamu Yakin atas Jawaban kamu {pilihan} ? [y/n] : "))

if(pilihan_2 == 'y'):
  if pilihan == Cupy_position:
    print(f"SELAMAT {nama_user} MENANG! posisi CUYPY di goa nomor  {Cupy_position} dan kamu memilih goa nomor {pilihan}")
  else:
    print(f"KAMU KALAH CUYPUY tidak ada di goa nomor{pilihan}, tetapi CUYPUY berada di goa nomor {Cupy_position}")
else:
  print("Kamu Takut yah hehehehe")




# print('''Ini Menggunakan single quote 3x
      
#       Bisa mencetak seperti ini
#       ''')

# f adalah format {}
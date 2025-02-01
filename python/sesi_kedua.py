# # ## Typecasting 1
# # tangga_date = "25"
# # tanggal = int(tangga_date)

# # print(tanggal)
# # print(f"Check Tipe Data Nya : {type(tanggal)}")

# # # Typecasting 2
# # # Variable boleh di timpa kembali jika kondisi tertentu
# # tanggal_lahir = "23"
# # tanggal_lahir = int(tanggal_lahir)
# # print(tanggal_lahir)
# # print(f"Check Tipe Data Nya : {type(tanggal_lahir)}")

# # # LIST

# # # Penambahan nilai
# # kardus = ["Semangka", "Pisang", "Apple"]
# # kardus.append("Jeruk")
# # kardus.append("Melon")
# # print(kardus)
# # print(kardus[4])

# # # Operator nya
# # print(kardus[4 - 3])


# # Contoh

# hobby = "Main bola, berenang, ngoding"
# print(hobby)
# print('-'*40)
# hobbysies = ["Main Bola", "Berenang", "Ngoding", "ngoding php", 'ngoding laravel', "Data Terakhir"]
# tmp_hobysies = hobbysies # variable ini menampung nilai hobbysies

# # cara mengetahui sebuah data yang sering digunakan dalam python len
# last_data = len(tmp_hobysies) - 1  # -1 adalah mengurani nya dengan 1 karena kepahaaman index
# print(tmp_hobysies[last_data])

# print(f"hobbysies -> {hobbysies}")
# # Cara Menanipulasi nilai array
# tmp_hobysies[1] = "Ngoding Javascript"
# print(f"tmp_hobysies -> {tmp_hobysies}")

# # Menggambil nilai Berenang
# # print(hobbysies[1])

# # kalau versi dengan kempahaman manusia
# # starht_from = 1
# # print(hobbysies[2 - starht_from])














# Libbary random
import random as rd

welcome_message = "WELCOME TO CUYPY GAMES"
Cupy_position = rd.randint(1,4)
# 1 adalah nomor awal dan nomor akhir atau pembatas 4
print("******************************")
print(f"** {welcome_message} **")
print("******************************")

# variable menumpang visual gambar
visual_gambar = "|_|"
# duplicated visual gambar
duplicated_gambar = [visual_gambar] * 4 # memanipulasi data seng string menjadi array agar nanti gambar visualusasi bisa di masukan
menghapus_koma_kurung_kotak = " ".join(duplicated_gambar)

# mengisi cuypuy pada visual nya
#duplicated_gambar[Cupy_position - 1] = '|0_0|' # Cara Menyamakan perhitungan index and perhitungan manusia


nama_user = input("Masukan Nama : ")
print(f'''Hello {nama_user}! Cobalah kamu perhatikan Goa Di bawah ini 
{menghapus_koma_kurung_kotak}
''')

# print(f"Posisi pada CuyPuy adalah : {Cupy_position}")
pilihan = int(input('Menurut kamu di Goa nomor berapa CUPY berada ? [1 / 2 / 3 / 4] : '))

print(f'Plihan Kamu adalah {pilihan}')

pilihan_2 = str(input(f"Apakah Kamu Yakin atas Jawaban kamu {pilihan} ? [y/n] : "))
if(pilihan_2 == 'y'):
  if pilihan == Cupy_position:
    print(f"SELAMAT {nama_user} MENANG! posisi CUYPY di goa nomor  {Cupy_position} dan kamu memilih goa nomor {pilihan}")
    list_data = menghapus_koma_kurung_kotak.split() # Membuat Variabel baru untuk memecah list
    
    list_data[Cupy_position - 1] = "|0_0|" # Mengisis isi dari list nya

    menghapus_koma_kurung_kotak = " ".join(list_data) # Menggambungkan kembali string

    print(f'''Nih posisi Goa nya {Cupy_position}
{menghapus_koma_kurung_kotak}
''')
    
  else:
    print(f"KAMU KALAH CUYPUY tidak ada di goa nomor{pilihan}, tetapi CUYPUY berada di goa nomor {Cupy_position}")

    list_data = menghapus_koma_kurung_kotak.split()

    list_data[Cupy_position - 1] = "|0_0|"

    menghapus_koma_kurung_kotak = " ".join(list_data)
    
    print(f'''Nih posisi Goa nya
{menghapus_koma_kurung_kotak}
  ''')
    
elif pilihan_2 == 'n':
  print("Kamu Takut yah hehehehe")
  exit()
else:
  print(f"Masukan y atau n yah ")




# print('''Ini Menggunakan single quote 3x
      
#       Bisa mencetak seperti ini
#       ''')

# f adalah format {}
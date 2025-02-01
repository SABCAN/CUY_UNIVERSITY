bentuk_goa = "|_|"
duplicated_goa = [bentuk_goa] * 4 ## Orginal goa

goa_kosong = duplicated_goa.copy()
# Apapun data yang keisi  kan data pada goa_kosong akan ikut juga duplicated_goa
## Tetapi kalau kita pkake copy maka goa_kosong saja yang ke isi
goa_kosong[2] = "SABCAN"
goa_kosong[0] = "Ucup"

print(duplicated_goa)
print(goa_kosong)

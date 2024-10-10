import biblioteka as inf
from datetime import datetime
print("Labdien, ša programma palidzēs jums veidot reķinu")
print("Lūdzu, ievadiet datus lai programma vara izvedot jums reķinu")
Kl_vards = input("Ievadit savu vārdu:")
velt_txt = input("Ievadiet savu veltījuma tekstu:")
print("Tagad nakamās trijās ailēs ievadiet lādītes izmēru milimetros")
lad_gar = input("Garums:")
lad_plat = input("Platums:")
lad_aug = input("Augstums:")
kokmat_cena = input("Ievadiet ludzu kokmateriala cenu:")
cur_time = datetime.now()
print("Programma saglabāja datus, lūdzu parbaudiet vai viss ir pareizs")
print(f"rēķina izveidošanas laiks ir {cur_time}")
print(f"Jūsu vards ir {Kl_vards}")
print(f"Veltijuma teksts ir {velt_txt}")
print(f"lādītes izmēri ir {lad_gar}mm garums, {lad_plat}mm platums,{lad_aug}mm augstums ")




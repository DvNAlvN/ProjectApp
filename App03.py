from os import system
from time import sleep
from datetime import datetime

def print_menu():
	system("cls")
	print("""
		Daftar menu
		[1]. Lihat pesanan
		[2]. Tambah pesanan
		[3]. Cari pesanan
		[4]. Hapus pesanan
		[5]. Perbarui pesanan
		[Q]. Keluar
		""")
def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(id_pemesan=None, barang=True, banyak=True, harga=True, all_data=False):
	if id_pemesan != None and all_data == False:
		print(f"ID : {id_pemesan}")
		print(f"Pemesan : {data[id_pemesan]['pemesan']}")
		print(f"Barang : {data[id_pemesan]['barang']}")
		print(f"banyak : {data[id_pemesan]['banyak']}")
		print(f"harga : {data[id_pemesan]['harga']}")
	elif banyak == False and all_data == False:
		print(f"ID : {id_pemesan}")
		print(f"Pemesan : {data[id_pemesan]['pemesan']}")
		print(f"Barang : {data[id_pemesan]['barang']}")
		print(f"harga : {data[id_pemesan]['harga']}")
	elif all_data == True:
		for id_pemesan in data:
			pemesan = data[id_pemesan]["pemesan"]
			barang = data[id_pemesan]["barang"]
			banyak = data[id_pemesan]["banyak"]
			harga = data[id_pemesan]["harga"]
			print(f"ID : {id_pemesan} - pemesan : {pemesan} - barang : {barang} - banyak : {banyak} - harga : {harga}")

def lihat_pesanan():
	print_header("Daftar pesanan Tersimpan")
	if not_empty(data):
		print_data(all_data=True)
	else:
		print("MAAF belum ada data tersimpan")
	input("TEKAN ENTER UNTUK KEMBALI KE MENU")


def create_id_pemesan(barang, harga):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	first = barang[0].upper()
	last_4 = harga[-4:]

	id_pemesan = ("%04d%02d%02d-C%s%s" % (tahun, bulan, hari, first, last_4))
	return id_pemesan

def tambah_pesanan():
	print_header("Tambah pesanan")
	pemesan = input("NAMA \t: ")
	barang = input("Barang \t: ")
	banyak = input("banyak \t: ")
	harga = input("harga \t: ")
	respon = input(f"Apakah yakin ingin menyimpan pesanan : {pemesan} ? (Y/N) ")
	if verify_ans(respon):
		id_pemesan = create_id_pemesan(barang=barang, harga=harga)
		data[id_pemesan] = {
			"pemesan" : pemesan,
			"barang" : barang,
			"banyak" : banyak,
			"harga" : harga
		}

		print("Data pesanan tersimpan")
	else:
		print("Data batal disimpan")
	input("Tekan enter untuk kembali ke menu")

def searching_by_pemesan(daftar):
	for id_pemesan in data:
		if data[id_pemesan]['pemesan'] == data:
			return id_pemesan
	else:
		return False

def cari_pesanan():
	print_header("MENCARI BARANG PESANAN")
	pemesan = input("Maukkan nama Pemesan yang dicari : ")
	exists = searching_by_pemesan(pemesan)
	if exists:
		print("Data ditemukan")
		print_data(id_pemesan=exists)
	else:
		print("Data tidak ada")
	input("Tekan ENTER untuk kembali ke MENU")

def hapus_pesanan():
	print_header("Menghapus pesanan")
	pemesan = input("Pesanan yang ingin dihapus: ")
	exists = searching_by_pemesan(pemesan)
	if exists:
		print_data(id_pemesan=exists)
		respon = input(f"yakin ingin Menghapus {pemesan} ? (Y/N)")
		if verify_ans(respon):
			del data[exists]
			saved = save_data()
			if saved:
				print("Data Telah dihapus")
			else:
				print("Kesalahan saat menyimpan")
		else:
			print("Data batal dihapus")
	else:
		print("Data tidak ada")
	input("Tekan ENTER untuk kembali ke MENU")

def update_pemesan(daftar):
	print(f"Pemesan Lama : {daftar}")
	new_pemesan = input("Masukkan nama pemesan baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N)")
	result = verify_ans(respon)
	if result :
		data[daftar]['pemesan']  = new_pemesan
		print('Data telah disimpan')
		print_data(daftar)
	else:
		print("Data batal diubah")

def update_barang(daftar):
	print(f"Barang lama : {data}")
	new_barang = input("Masukkan barang baru : ")
	respon = input("Apakah anda yakin data inngin diubah (Y/N) : ")
	result = verivy_ans(respon)
	if result :
		data[new_barang] = data[daftar]
		del data[daftar]
		print("Data telah disimpan")
		print_data(new_barang)
	else:
		print("Data batal diubah")
def update_banyak(daftar):
	print(f"Banyak lama : {data[daftar]['banyak']}")
	new_banyak = input("Masukkan banyak baru : ")
	respon = input("Apakah anda yakin ingin mengubah data (Y/N) : ")
	result = verify_ans(respon)
	if result :
		data[daftar]['banyak'] = new_banyak
		print("Data telah disimpan")
		print_data(daftar)
	else:
		print("Data batal diubah")
def update_harga(daftar):
	print(f"")

def perbarui_pesanan():
	print_header("MENGUPDATE INFO PESANAN")
	pemesan = input("Nama pemesan yang akan diupdate : ")
	exists = searching_by_pemesan(pemesan)
	if exists:
		print_data(pemesan)
		print("EDIT FIELD [1].PEMESAN [2]. BARANG [3].BANYAK [4].HARGA")
		respon = input("Masukkan pilihan (1/2/3/4) : ")
		if respon == "1":
			update_pemesan(pemesan)
		elif respon == "2":
			update_barang(pemesan)
		elif respon == "3":
			update_banyak(pemesan)
		elif respon == "4":
			update_harga(pemesan)
	else:
		print("Data tidak ada")
	input("Tekan enter untuk kembali ke menu")


def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		lihat_pesanan()
	elif char == "2":
		tambah_pesanan()
	elif char == "3":
		cari_pesanan()
	elif char == "4":
		hapus_pesanan()
	elif char == "5":
		perbarui_pesanan()
	elif char == "6":
		pass

data = {
	"20201007" : {
		"barang" : "kecap",
		"pemesan" : "Budi",
		"harga" : "10.000",
		"banyak" : "1"
	},
	"20201008" : {
		"barang" : "gula",
		"pemesan" : "Adi",
		"harga" : "10.000",
		"banyak" : "1"
	}
}

stop = False

while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)
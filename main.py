import random

hello_pesan= "Welcome To CUYPY GAMES!"
cuypy_posisi = random.randint(1,4)
lanjut = "OK"

while True:
    try:
        print("==========================")
        print(f"=~{hello_pesan}~=")

        nama_user = input("Masukkan nama Anda: ")

        print("==========================")

        print(f'''Hallo {nama_user}, coba perhatikan goa di bawah ini:
        |_| |_| |_| |_| ''')

        pilihan_user = int(input("Menurutmu, di goa nomor berapa CUYPY berada? [1/2/3/4]: "))
        print(f'Oke {nama_user}, pilihanmu adalah {pilihan_user}')
        
        fix = input(f"Untuk melanjutkan game ini, apakah kamu yakin dengan pilihan mu, {nama_user}?:klik[OK/NO] ")
        # logic untuk lanjut apa engga

        if fix == lanjut:
            print(f"okee gassskeunn {nama_user}")
        else:
            print('Terima kasih sudah bermain di CUYPY')
            break
        
        # logic gamenya buat pilihnya
        if pilihan_user == cuypy_posisi:
            print(f"Selamat {nama_user}, kamu berhasil menebaknya! Posisi CUYPY ada di {cuypy_posisi} dan pilihanmu adalah {pilihan_user}")
            break
        else:
            print(f"Kamu kalah, CUYPY tidak berada di situ. CUYPY ada di goa nomor {cuypy_posisi}, sedangkan pilihanmu adalah nomor {pilihan_user}")
            print("Silahkan coba lagi ya")
            print("==========================\n")
    except ValueError:
        print("==========================")
        print("Pilihan harus berupa nilai angka")
        print("==========================\n")

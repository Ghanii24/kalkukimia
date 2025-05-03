def hitung_molaritas():
    mol = float(input("Masukkan jumlah mol zat terlarut (mol): "))
    volume = float(input("Masukkan volume larutan (L): "))
    molaritas = mol / volume
    print(f"Molaritas = {molaritas:.4f} M\n")

def hitung_molalitas():
    mol = float(input("Masukkan jumlah mol zat terlarut (mol): "))
    massa_pelarut = float(input("Masukkan massa pelarut (kg): "))
    molalitas = mol / massa_pelarut
    print(f"Molalitas = {molalitas:.4f} m\n")

def hitung_fraksi_mol():
    mol_terlarut = float(input("Masukkan jumlah mol zat terlarut: "))
    mol_pelarut = float(input("Masukkan jumlah mol pelarut: "))
    total_mol = mol_terlarut + mol_pelarut
    fraksi_mol = mol_terlarut / total_mol
    print(f"Fraksi mol zat terlarut = {fraksi_mol:.4f}\n")

def hitung_persen_massa():
    massa_terlarut = float(input("Masukkan massa zat terlarut (gram): "))
    massa_larutan = float(input("Masukkan massa larutan (gram): "))
    persen = (massa_terlarut / massa_larutan) * 100
    print(f"Persentase massa = {persen:.2f}%\n")

def main():
    while True:
        print("\n=== Kalkulator Konsentrasi Kimia ===")
        print("1. Hitung Molaritas (M)")
        print("2. Hitung Molalitas (m)")
        print("3. Hitung Fraksi Mol")
        print("4. Hitung Persentase Massa")
        print("5. Keluar")

        pilihan = input("Pilih jenis perhitungan (1-5): ")

        if pilihan == "1":
            hitung_molaritas()
        elif pilihan == "2":
            hitung_molalitas()
        elif pilihan == "3":
            hitung_fraksi_mol()
        elif pilihan == "4":
            hitung_persen_massa()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()

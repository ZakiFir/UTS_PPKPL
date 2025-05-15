from entities.book import Book
from use_cases.book_usecase import BookUseCase
from infrastructure.in_memory_repo import InMemoryBookRepository

def menu():
    print("\n=== MENU CRUD BUKU ===")
    print("1. Tambah Buku")
    print("2. Lihat Semua Buku")
    print("3. Cari Buku berdasarkan ID")
    print("4. Edit Buku")
    print("5. Hapus Buku")
    print("0. Keluar")

def input_book():
    id = int(input("ID Buku: "))
    title = input("Judul: ")
    author = input("Penulis: ")
    year = int(input("Tahun: "))
    stock = int(input("Stok: "))
    return Book(id, title, author, year, stock)

def main():
    repo = InMemoryBookRepository()
    usecase = BookUseCase(repo)

    while True:
        menu()
        choice = input("Pilih menu: ")

        if choice == "1":
            book = input_book()
            usecase.add_book(book)
            print("Buku berhasil ditambahkan.")
        
        elif choice == "2":
            books = usecase.list_books()
            if books:
                print("\n=== Daftar Buku ===")
                for b in books:
                    print(f"[{b.id}] {b.title} - {b.author} ({b.year}) | Stok: {b.stock}")
            else:
                print("Belum ada buku.")
        
        elif choice == "3":
            id = int(input("Masukkan ID buku: "))
            book = usecase.get_book(id)
            if book:
                print(f"{book.title} oleh {book.author} ({book.year}) - Stok: {book.stock}")
            else:
                print("Buku tidak ditemukan.")
        
        elif choice == "4":
            id = int(input("Masukkan ID buku yang akan diedit: "))
            old_book = usecase.get_book(id)
            if old_book:
                print("Masukkan data baru:")
                new_book = input_book()
                usecase.delete_book(id)
                usecase.add_book(new_book)
                print("Buku berhasil diubah.")
            else:
                print("Buku tidak ditemukan.")
        
        elif choice == "5":
            id = int(input("Masukkan ID buku yang akan dihapus: "))
            usecase.delete_book(id)
            print("Buku berhasil dihapus (jika ada).")
        
        elif choice == "0":
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

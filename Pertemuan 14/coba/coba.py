import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import seaborn as sns
import matplotlib.pyplot as plt

class AplikasiDataGempa:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualisasi Data Gempa")
        self.root.attributes('-fullscreen', True)
        self.create_widgets()
    
    def create_widgets(self):
        # Create a main frame
        main_frame = tk.Frame(self.root, bg='#282c34')
        main_frame.pack(expand=True, fill='both')

        # Center frame
        center_frame = tk.Frame(main_frame, bg='#282c34')
        center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Load CSV Button
        self.tombol_muatan = tk.Button(center_frame, text="Muat File CSV", command=self.load_csv, bg='#61dafb', fg='white', font=('Helvetica', 14, 'bold'), bd=0, relief=tk.RAISED, padx=10, pady=5)
        self.tombol_muatan.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
        
        # Option Menu
        self.opsi_var = tk.StringVar(value="Pilih opsi")
        self.menu_opsi = ttk.OptionMenu(center_frame, self.opsi_var, "Pilih opsi", "Distribusi Magnitudo", "Lokasi Geografis Gempa", "Data Terbaru", "Region Terbanyak")
        self.menu_opsi.grid(row=1, column=0, padx=20, pady=20, sticky='ew')

        # Plot Data Button
        self.tombol_plot = tk.Button(center_frame, text="Plot Data", command=self.plot_data, state=tk.DISABLED, bg='#61dafb', fg='white', font=('Helvetica', 14, 'bold'), bd=0, relief=tk.RAISED, padx=10, pady=5)
        self.tombol_plot.grid(row=2, column=0, padx=20, pady=20, sticky='ew')
        
        # Exit Button
        self.tombol_keluar = tk.Button(center_frame, text="Keluar", command=self.exit_app, bg='#ff4757', fg='white', font=('Helvetica', 14, 'bold'), bd=0, relief=tk.RAISED, padx=10, pady=5)
        self.tombol_keluar.grid(row=3, column=0, padx=20, pady=20, sticky='ew')

        # Style Configuration for OptionMenu
        style = ttk.Style()
        style.configure('TMenubutton', background='#61dafb', foreground='white', font=('Helvetica', 14, 'bold'))
    
    def load_csv(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.data = pd.read_csv(file_path)
            self.data['TANGGAL'] = pd.to_datetime(self.data['TANGGAL'], errors='coerce')
            self.tombol_plot.config(state=tk.NORMAL)
    
    def plot_data(self):
        if not hasattr(self, 'data'):
            messagebox.showerror("Kesalahan", "Harap muat file CSV terlebih dahulu.")
            return
        
        opsi = self.opsi_var.get()
        
        if opsi == "Distribusi Magnitudo":
            self.plot_distribusi_magnitudo()
        elif opsi == "Lokasi Geografis Gempa":
            self.plot_lokasi_geografis()
        elif opsi == "Data Terbaru":
            self.tampilkan_data_terbaru()
        elif opsi == "Region Terbanyak":
            self.plot_region_terbanyak()
        else:
            messagebox.showerror("Kesalahan", "Harap pilih opsi yang valid.")
    
    def plot_distribusi_magnitudo(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[' Mag '], bins=20, kde=True)
        plt.title('Distribusi Magnitudo')
        plt.xlabel('Magnitudo')
        plt.ylabel('Frekuensi')
        plt.show()
    
    def plot_lokasi_geografis(self):
        # Mengambil 100 data terbaru untuk plot lokasi geografis
        data_terbaru = self.data.sort_values(by='TANGGAL', ascending=False).head(100)
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data_terbaru[' BUJUR '], y=data_terbaru[' LINTANG '], hue=data_terbaru[' Mag '], palette='viridis')
        plt.title('Lokasi Geografis Gempa (100 data terbaru)')
        plt.xlabel('Bujur')
        plt.ylabel('Lintang')
        plt.show()
    
    def tampilkan_data_terbaru(self):
        data_terbaru = self.data.sort_values(by='TANGGAL', ascending=False).head(10)
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=data_terbaru[' BUJUR '], y=data_terbaru[' LINTANG '], hue=data_terbaru[' Mag '], palette='viridis', size=data_terbaru[' Mag '], sizes=(20, 200))
        plt.title('Gempa Terbaru')
        plt.xlabel('Bujur')
        plt.ylabel('Lintang')
        plt.show()
    
    def plot_region_terbanyak(self):
        plt.figure(figsize=(10, 6))
        region_count = self.data['Region'].value_counts().head(10)
        sns.barplot(x=region_count.values, y=region_count.index, palette='viridis')
        plt.title('Top 10 Region dengan Gempa Terbanyak')
        plt.xlabel('Jumlah Gempa')
        plt.ylabel('Region')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    
    def exit_app(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiDataGempa(root)
    root.mainloop()

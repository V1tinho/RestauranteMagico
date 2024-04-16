import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante do Mundo Mágico de Harry Potter")
        self.root.configure(background="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use("clam") 
         
        self.style.configure('Highlighted.TButton', background='#4caf50', foreground='#ffffff')

        self.icon_style = ttk.Style()
        self.icon_style.configure("Icon.TButton", padding=5)

        # Cria um Notebook (abas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Primeira aba: Pedidos
        self.orders_frame = tk.Frame(self.notebook, bg="#f0f0f0")
        self.notebook.add(self.orders_frame, text="Pedidos")
        self.create_orders_interface()

        
        self.customer_frame = tk.Frame(self.notebook, bg="#f0f0f0")
        self.notebook.add(self.customer_frame, text="Dados do Cliente")
        self.create_customer_interface()

        # Fila de pedidos prontos
        self.ready_queue = tk.Listbox(self.orders_frame, font=("Arial", 12), bg="#ffffff", bd=0, highlightthickness=0)
        self.ready_queue.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    def create_orders_interface(self):
        # Cardápio 
        self.menu_items = [
            {"name": "Cerveja Amanteigada", "image": "cerveja_amanteigada.jpg"},
            #adicione mais item.
        ]

        lbl_menu = tk.Label(self.orders_frame, text="Cardápio", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_menu.pack(padx=20, pady=(20, 10))

        self.menu_frame = tk.Frame(self.orders_frame, bg="#f0f0f0")
        self.menu_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        for item in self.menu_items:
            item_frame = tk.Frame(self.menu_frame, bg="#f0f0f0")
            item_frame.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)

            image_path = os.path.join("images", item["image"])  
            image = Image.open(image_path)  
            image = image.resize((50, 50))  
            photo = ImageTk.PhotoImage(image)  
            label = tk.Label(item_frame, text=item["name"], font=("Arial", 12), bg="#f0f0f0")
            label.pack(side=tk.LEFT)

            image_label = tk.Label(item_frame, image=photo, bg="#f0f0f0")
            image_label.image = photo
            image_label.pack(side=tk.LEFT, padx=10)

            button = ttk.Button(item_frame, text="Adicionar ao Pedido", style="Highlighted.TButton", command=lambda item=item["name"]: self.add_item_to_order(item))
            button.pack(side=tk.RIGHT, padx=10)

        self.waiting_queue = tk.Listbox(self.orders_frame, font=("Arial", 12), bg="#ffffff", bd=0, highlightthickness=0)
        self.waiting_queue.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Botões para adicionar e mover pedidos
        button_frame = tk.Frame(self.orders_frame, bg="#f0f0f0")
        button_frame.pack(pady=(10, 20))
        add_order_button = ttk.Button(button_frame, text="Adicionar Pedido", style="Highlighted.TButton", command=self.add_order)
        add_order_button.grid(row=0, column=0, padx=10)
        ready_button = ttk.Button(button_frame, text="Pedido Pronto", style="Highlighted.TButton", command=self.move_order)
        ready_button.grid(row=0, column=1, padx=10)

    def create_customer_interface(self):
        # Campos para os dados do cliente
        lbl_name = tk.Label(self.customer_frame, text="Nome:", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_name.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.entry_name = tk.Entry(self.customer_frame, font=("Arial", 12), bg="#ffffff", bd=0)
        self.entry_name.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

        lbl_table = tk.Label(self.customer_frame, text="Mesa:", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_table.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_table = tk.Entry(self.customer_frame, font=("Arial", 12), bg="#ffffff", bd=0)
        self.entry_table.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_quantity = tk.Label(self.customer_frame, text="Quantidade de itens:", font=("Arial", 14, "bold"), bg="#f0f0f0")
        lbl_quantity.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.entry_quantity = tk.Entry(self.customer_frame, font=("Arial", 12), bg="#ffffff", bd=0)
        self.entry_quantity.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    def add_item_to_order(self, item_name):
        customer_name = self.entry_name.get().strip()
        table_number = self.entry_table.get().strip()
        quantity = self.entry_quantity.get().strip()

        if customer_name and table_number:
            if not quantity.isdigit():
                quantity = "1"

            order_text = f"{item_name} - Quantidade: {quantity}, Cliente: {customer_name}, Mesa: {table_number}"
            self.waiting_queue.insert(tk.END, order_text)
            self.show_message("Sucesso", "Item adicionado ao pedido com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha o nome do cliente e o número da mesa.")

    def add_order(self):
        pass

    def move_order(self):
        selected_index = self.waiting_queue.curselection()
        
        if selected_index:
            selected_order = self.waiting_queue.get(selected_index)
            self.waiting_queue.delete(selected_index)
            self.ready_queue.insert(tk.END, selected_order)
            self.show_message("Sucesso", "Pedido movido para a fila de pedidos prontos!")
        else:
            messagebox.showerror("Erro", "Por favor, selecione um pedido da lista de espera.")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

root = tk.Tk()
app = RestaurantApp(root)
root.mainloop()


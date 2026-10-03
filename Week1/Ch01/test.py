import tkinter as tk
from tkinter import messagebox, ttk


class PizzaOrderApp:
    def __init__(self, root):
        self.root = root
        root.title("피자 주문")
        root.resizable(False, False)

        self.size = tk.StringVar(value="미디엄 (M)")
        self.slices = tk.StringVar(value="8")
        self.drink = tk.StringVar(value="콜라")

        frame = ttk.Frame(root, padding=24)
        frame.grid(sticky="nsew")
        frame.columnconfigure(0, weight=1)

        ttk.Label(frame, text="나만의 피자 주문", font=("", 20, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 8)
        )
        ttk.Label(frame, text="피자 크기, 조각 수, 음료를 선택하세요.").grid(
            row=1, column=0, sticky="w", pady=(0, 22)
        )

        ttk.Label(frame, text="피자 크기").grid(row=2, column=0, sticky="w")
        ttk.Combobox(
            frame,
            textvariable=self.size,
            values=("스몰 (S)", "미디엄 (M)", "라지 (L)", "패밀리 (XL)"),
            state="readonly",
            width=32,
        ).grid(row=3, column=0, sticky="ew", pady=(6, 18))

        ttk.Label(frame, text="몇 조각으로 자를까요? (1~32조각)").grid(
            row=4, column=0, sticky="w"
        )
        controls = ttk.Frame(frame)
        controls.grid(row=5, column=0, sticky="ew", pady=(6, 18))
        controls.columnconfigure(1, weight=1)
        ttk.Button(controls, text="−", width=4, command=lambda: self.adjust(-1)).grid(
            row=0, column=0
        )
        validate = (root.register(self.valid_slice_input), "%P")
        self.slice_entry = ttk.Entry(
            controls,
            textvariable=self.slices,
            justify="center",
            width=10,
            validate="key",
            validatecommand=validate,
        )
        self.slice_entry.grid(row=0, column=1, sticky="ew", padx=8)
        ttk.Button(controls, text="+", width=4, command=lambda: self.adjust(1)).grid(
            row=0, column=2
        )

        ttk.Label(frame, text="음료").grid(row=6, column=0, sticky="w")
        ttk.Combobox(
            frame,
            textvariable=self.drink,
            values=("콜라", "제로 콜라", "사이다", "오렌지 주스", "물", "선택 안 함"),
            state="readonly",
        ).grid(row=7, column=0, sticky="ew", pady=(6, 22))
        ttk.Button(frame, text="주문 확인", command=self.confirm).grid(
            row=8, column=0, sticky="ew"
        )

    @staticmethod
    def valid_slice_input(value):
        # 전체 삭제 후 다시 입력할 수 있도록 빈 문자열도 허용합니다.
        return value == "" or (
            value.isascii() and value.isdecimal() and len(value) <= 2
        )

    def adjust(self, amount):
        current = int(self.slices.get() or "1")
        self.slices.set(str(max(1, min(32, current + amount))))

    def confirm(self):
        count = int(self.slices.get() or "0")
        if not 1 <= count <= 32:
            messagebox.showwarning(
                "조각 수 확인", "조각 수를 1~32 사이의 숫자로 입력해주세요.", parent=self.root
            )
            self.slice_entry.focus_set()
            self.slice_entry.selection_range(0, tk.END)
            return
        messagebox.showinfo(
            "주문 내역",
            f"피자 크기: {self.size.get()}\n조각 수: {count}조각\n음료: {self.drink.get()}",
            parent=self.root,
        )


if __name__ == "__main__":
    window = tk.Tk()
    PizzaOrderApp(window)
    window.mainloop()

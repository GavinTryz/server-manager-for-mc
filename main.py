from gui.main_window import MainWindow

if __name__ == '__main__':
    use_gui = True
    if use_gui:
        main_window = MainWindow()
        main_window.mainloop()
import chess
import chess.engine
import chess.pgn
from selenium import webdriver
import tkinter as tk
import pyautogui
from functools import partial



def get_fen():
    im = pyautogui.screenshot('my_screenshot.png', region=(360, 150, 480, 495))
    driver = webdriver.Edge(executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe")
    driver.get("https://www.ocf.berkeley.edu/~abhishek/putz/")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@type='file']").send_keys("C:/Users/Narcis/PycharmProjects/ChessBoardAnalyser/my_screenshot.png")
    driver.find_element_by_xpath("//input[@type='submit']").click()
    fen = driver.find_element_by_class_name("boxed").text
    fen = fen.split('\n', 1)[0]
    fen = fen[5:]
    #driver.quit()
    return fen

def move_white():
    move.pack_forget()
    fen = get_fen()
    fen = fen + " w"
    get_best_move(fen)

def move_black():
    move.pack_forget()
    fen = get_fen()
    fen = fen + " b"
    get_best_move(fen)

def get_best_move(fen):
    board = chess.Board(fen)
    print("Before: \n")
    print(board)
    engine = chess.engine.SimpleEngine.popen_uci("stockfish-10-win/Windows/stockfish_10_x64_popcnt.exe")
    result = engine.play(board, chess.engine.Limit(depth=25))
    board.push(result.move)
    move.config(text="The best move is:" + str(result.move))
    move.pack()
    print("\nAfter\n")
    print(board)
    print(result.move)
    engine.quit()



window = tk.Tk()
move = tk.Label()
window.geometry("250x100")
choose_color = tk.Label(text="Choose color!")
choose_color.pack()
white_to_play = tk.Button(text="White to play!", command=move_white)
white_to_play.pack()
black_to_play = tk.Button(text="Black to play!", command=move_black)
black_to_play.pack()
window.mainloop()



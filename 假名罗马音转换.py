import tkinter as tk

from tkinter import filedialog



# 定义罗马音和假名的对应字典

romaji_kana_dict1={
'ka':'か',
'ki':'き',
'ku':'く',
'ke':'け',
'ko':'こ',
'sa':'さ',
'shi':'し',
'su':'す',
'se':'せ',
'so':'そ',
'ta':'た',
'chi':'ち',
'tsu':'つ',
'te':'て',
'to':'と',
'na':'な',
'ni':'に',
'nu':'ぬ',
'ne':'ね',
'no':'の',
'ha':'は',
'hi':'ひ',
'fu':'ふ',
'he':'へ',
'ho':'ほ',
'ma':'ま',
'mi':'み',
'mu':'む',
'me':'め',
'mo':'も',
'ya':'や',
'yu':'ゆ',
'yo':'よ',
'ra':'ら',
'ri':'り',
'ru':'る',
're':'れ',
'ro':'ろ',
'wa':'わ',
'wo':'を'
}
romaji_kana_dict2={'a':'あ',
'i':'い',
'u':'う',
'e':'え',
'o':'お',
'n':'ん'}

romaji_kana_dict={
'ka':'か',
'ki':'き',
'ku':'く',
'ke':'け',
'ko':'こ',
'sa':'さ',
'shi':'し',
'su':'す',
'se':'せ',
'so':'そ',
'ta':'た',
'chi':'ち',
'tsu':'つ',
'te':'て',
'to':'と',
'na':'な',
'ni':'に',
'nu':'ぬ',
'ne':'ね',
'no':'の',
'ha':'は',
'hi':'ひ',
'fu':'ふ',
'he':'へ',
'ho':'ほ',
'ma':'ま',
'mi':'み',
'mu':'む',
'me':'め',
'mo':'も',
'ya':'や',
'yu':'ゆ',
'yo':'よ',
'ra':'ら',
'ri':'り',
'ru':'る',
're':'れ',
'ro':'ろ',
'wa':'わ',
'wo':'を',
'a':'あ',
'i':'い',
'u':'う',
'e':'え',
'o':'お',
'n':'ん'}

# 定义GUI窗口

root = tk.Tk()

root.title('Romaji & Kana Converter')



# 定义窗口大小

root.geometry('400x400')



# 定义文本框

text_box = tk.Text(root, width=30, height=20)

text_box.pack()



# 定义按钮

romaji_to_kana_button = tk.Button(root, text='Romaji to Kana', command=lambda: convert(romaji_kana_dict1,romaji_kana_dict2))

kana_to_romaji_button = tk.Button(root, text='Kana to Romaji', command=lambda: convert(dict((v, k) for k, v in romaji_kana_dict.items()),dict() ))



# 将按钮放入窗口

romaji_to_kana_button.pack()

kana_to_romaji_button.pack()





# 定义文件选择函数

def select_file():

             file_path = filedialog.askopenfilename(title='Select File', filetypes=[('Text File', '*.txt')])
             with open(file_path, 'r', encoding='utf-8') as f:
                       text_box.delete('1.0', tk.END)
                       text_box.insert('1.0', f.read())



# 定义转换函数

def convert(dictionary1,dictionary2):

           text = text_box.get('1.0', tk.END).split(" ")

           new_text = ''
           new_text1 = ''

           for char in text:

                       if char in dictionary1:

                                 new_text1 += dictionary1[char]
                       
                       else:

                                 new_text1 += char
           print(new_text1)
           for char in new_text1:

                       if char in dictionary2:

                                 new_text += dictionary2[char]
                       
                       else:

                                 new_text += char

           text_box.delete('1.0', tk.END)
           text_box.insert('1.0', new_text)



# 定义文件保存函数

def save_file():

             file_path = filedialog.asksaveasfilename(title='Save File', filetypes=[('Text File', '*.txt')])

             with open(file_path, 'w', encoding='utf-8') as f:

                          text = text_box.get('1.0', tk.END)

                          f.write(text)
# 定义菜单

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label='Open', command=select_file)

filemenu.add_command(label='Save', command=save_file)

menubar.add_cascade(label='File', menu=filemenu)



# 将菜单放入窗口

root.config(menu=menubar)



# 启动GUI程序

root.mainloop()

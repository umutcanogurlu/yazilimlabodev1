import tkinter as tk
import random

root = tk.Tk()#root = tk.Tk(): Tkinter uygulaması için ana pencere (root) oluşturulur. Bu, programın tüm bileşenlerini içeren temel yapıdır.
root.title("Animation Drawing Screen")#root.title("Animation Drawing Screen"): Pencerenin başlık çubuğunda görüntülenecek başlığı ayarlar: "Animation Drawing Screen".
root.geometry("800x600")#root.geometry("800x600"): Pencerenin boyutunu 800x600 piksel olarak belirler.

canvas = tk.Canvas(root, width=800, height=500, bg="white")
#tk.Canvas: Pencerenin içine bir Canvas (tuval) ekler. Canvas, grafik şekillerin (çizgiler, daireler, vb.) çizilmesi için kullanılan bir alandır.
#width=800, height=500: Tuvalin genişliği 800 piksel, yüksekliği ise 500 piksel olarak ayarlanır.
#bg="white": Tuvalin arka plan rengi beyaz olarak belirlenir.
canvas.pack()#canvas.pack(): Canvas'ı pencereye ekler.

balls = []#balls: Tüm topları (ID, hareket yönü gibi bilgileri) saklamak için kullanılan bir liste.

ball_colors = ["red", "blue", "green", "yellow", "gray"]#ball_colors: Kullanıcının seçebileceği renklerin listesi.

continue_animation = False
#TOP BOYUTU VE RENK MENÜ AYAR KISMI:
#BOYUT MENÜSÜ
size_label = tk.Label(root, text="Select Size:")#Kullanıcıdan top seçimi istenir
size_label.pack()
size_var = tk.IntVar(value=20)#size_var: Seçilen boyutu tutan değişken. Varsayılan olarak 20.
size_menu = tk.OptionMenu(root, size_var, 20, 30, 50)
size_menu.pack()
#RENK MENÜSÜ
color_label = tk.Label(root, text="Select Color:")#Kullanıcıdan bir renk seçmesi istenir.
color_label.pack()
color_var = tk.StringVar(value=ball_colors[0])#color_var: Seçilen rengi tutan değişken. Varsayılan olarak ilk renk ("red").
color_menu = tk.OptionMenu(root, color_var, *ball_colors)
color_menu.pack()
#TOP EKLEME FONKSİYONU
def add_ball():
    size = size_var.get()#size = size_var.get(): Seçilen top boyutunu alır.
    color = color_var.get()#color = color_var.get(): Seçilen rengi alır.
    x = random.randint(size, 800 - size)#x, y: Topun Canvas üzerinde rastgele bir konumunu belirler. Top, tuvalin kenarlarını aşmaz.
    y = random.randint(size, 500 - size)#x, y: Topun Canvas üzerinde rastgele bir konumunu belirler. Top, tuvalin kenarlarını aşmaz.
    ball = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)#canvas.create_oval(...): Belirtilen konuma ve boyuta sahip bir daire çizer.
    balls.append({"id": ball, "dx": random.choice([-3, 3]), "dy": random.choice([-3, 3])})
    #balls.append(...): Topun ID'si, yatay/dikey hareket yönleri (dx, dy) ile balls listesine eklenir.
#TOP HAREKETİ
def move_balls():
    global continue_animation
    if not continue_animation:
        return
    for ball in balls:
        x1, y1, x2, y2 = canvas.coords(ball["id"])#canvas.coords(ball["id"]): Topun mevcut konumunu alır.
        if x1 <= 0 or x2 >= 800:
            ball["dx"] = -ball["dx"]
        if y1 <= 0 or y2 >= 500:
            ball["dy"] = -ball["dy"]
        canvas.move(ball["id"], ball["dx"], ball["dy"])#canvas.move(...): Topun pozisyonunu dx ve dy değerlerine göre günceller.
    root.after(30, move_balls)#root.after(30, move_balls): Bu fonksiyonu 30 milisaniye sonra yeniden çağırarak hareketi sürekli hale getirir.
    #Eğer top Canvas'ın sınırlarına çarparsa:
    #Yatay sınırda: dx tersine çevrilir (yön değişir).
    #Dikey sınırda: dy tersine çevrilir.

##KONTROL FONKSİYONLARI:
def start():#BAŞLATMA
    global continue_animation
    continue_animation = True
    move_balls()
#DURDURMA
def stop():
    global continue_animation
    continue_animation = False
#SIFIRLAMA
def reset():
    global balls
    for ball in balls:
        canvas.delete(ball["id"])
    balls = []
#TOP HIZLARI
def speed_up():
    for ball in balls:
        ball["dx"] *= 1.5
        ball["dy"] *= 1.5
#Kullanıcı Arayüzü Butonları
frame = tk.Frame(root)
frame.pack()

add_button = tk.Button(frame, text="Add Ball", command=add_ball)#Add Ball: Yeni bir top ekler.
add_button.pack(side=tk.LEFT)

start_button = tk.Button(frame, text="Start", command=start)#Start: Hareketi başlatır.
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(frame, text="Stop", command=stop)#Stop: Hareketi durdurur.
stop_button.pack(side=tk.LEFT)

reset_button = tk.Button(frame, text="Reset", command=reset)#Reset: Tüm topları siler.
reset_button.pack(side=tk.LEFT)

speed_button = tk.Button(frame, text="Speed Up", command=speed_up)#Speed Up: Topların hızını artırır.
speed_button.pack(side=tk.LEFT)

root.mainloop()

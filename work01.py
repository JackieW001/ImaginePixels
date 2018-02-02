filename = "work01.ppm"
w = 500
h = 500

def write_header(file, w, h):
    file.write("P3\n")
    file.write(str(w) + " " + str(h) + "\n")
    file.write("255\n")

def color(file, w, h):
    for i in range(w):
        for j in range(h):
            file.write("0 0 255 ")
        
with open(filename, "w") as file:
    write_header(file, w, h)
    color(file, w, h)

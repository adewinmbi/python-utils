from PIL import Image
import turtle

rgba = Image.open("res\\vcmovie.png")
im = rgba.convert('RGB')

p = turtle.Turtle()

p.speed(100000000)

def RenderImage(image):
  width, height = image.size

  for i in range(0, height):
    p.penup()
    p.goto(0, height - i)
    p.pendown()

    for n in range(0, width):
      pixelCoord = x, y = n - 1, height - i - 1
      hexColor = '#%02x%02x%02x' % im.getpixel(pixelCoord)
      p.pencolor(hexColor)
      p.goto(n, height - i)
      # print(n, height - i)

RenderImage(im)

wn = turtle.Screen()
wn.mainloop()
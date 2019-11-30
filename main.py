from guizero import App
##############
#COLORS class#
##############
class colors:
    class workspace:
        px1 = "#aaaaaa"
        px2 = "#ffffff"
    class schemes:
        
        red     = "#FF0000"
        green   = "#00FF00"
        blue    = "#0000FF"
        yellow  = "#FFFF00"
        orange  = "#FF6600"
    class palette:
        fg = "#0000FF"
        bg = "#FFFF00"

app = App(title="drawing app")

##
#
##
app.display()

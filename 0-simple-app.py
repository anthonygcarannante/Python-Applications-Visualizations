# You need to run Python v3.9 or higher to use justpy
import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis.")
    return wp

jp.justpy(app)
from flask import Flask, render_template

app = Flask(__name__)

players = [
    {"name": "Līva Laura L.", "desc": "Mamma, jo vienmēr visus apčubinās un pārliecinās vai visiem viss ir."},
    {"name": "Una Š.", "desc": "Asinsspiediena cēlājs, māk uzkurināt un pakaitināt."},
    {"name": "Kristīne H.", "desc": "Brauc uz treniņiem ar vilcienu. Parūpējas, ka zālē ir bumbas."},
    {"name": "Samanta G.", "desc": "Viņai ir BMW. Mašīnai vajag jaunas riepas, pati nav riepa."},
    {"name": "Emīlija T.", "desc": "DJ pults, jo māk savienoties ar tumbiņu."},
    {"name": "Luīze Š.", "desc": "Kapteine. Uzticamā roka, kam visi visu var teikt."},
    {"name": "Ieva V.", "desc": "Viņai vienmēr iet labi pat tad, kad neiet tik labi."},
    {"name": "Annija B.", "desc": "Pasākumu organizētāja un jokdare. Kādu dienu iedankos."},
    {"name": "Aleksa S.", "desc": "Šajā sezonā kā atbalstītāja, bet vispār daudz smaida."},
    {"name": "Anete O.", "desc": "Paliks zālē visilgāk, pat tad ja visi jau sen būs prom."},
    {"name": "Anita M.", "desc": "DJ, jo viņai vajadzētu būt somā tumbiņai."},
    {"name": "Šarlote P.", "desc": "Apslēpti ļoti smieklīga, reizēm pat pārāk."},
    {"name": "Paula C.", "desc": "Cīņasspars. Ja kādai būs nolaidušās rokas, tad tā nebūs viņa."}
]

games = [
    {"date": "7.01", "time": "19:30", "place": "Rimi OSC", "opponent": "LV Izlase"},
    {"date": "10.01", "time": "14:00", "place": "Rimi OSC", "opponent": "Kibirkstis"},
    {"date": "14.01", "time": "19:00", "place": "Rimi OSC", "opponent": "TTT Juniores"},
    {"date": "17.01", "time": "13:00", "place": "Rimi OSC", "opponent": "TTT Rīga"},
    {"date": "25.01", "time": "14:00", "place": "Alytus", "opponent": "Alytus"},
    {"date": "28.01", "time": "19:00", "place": "Rimi OSC", "opponent": "Liepāja"}
]

@app.route("/")
def index():
    return render_template("index.html", players=players, games=games)

if __name__ == "__main__":
    app.run(debug=True)

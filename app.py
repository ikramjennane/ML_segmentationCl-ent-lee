from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = ""  # Initialisez result_text avec une chaîne vide

    if request.method == 'POST':
        p1 = int(request.form['income'])
        p2 = int(request.form['spending'])

        # Charger le modèle pré-entrainé
        model = joblib.load('Customer_Segmentation')
        result = model.predict([[p1, p2]])[0]

        # Déterminer le texte du résultat
        if result == 0:
            result_text = "Clients avec un revenu annuel moyen et des dépenses annuelles moyennes : Ce Client appartient au cluster n° 1"
        elif result == 1:
            result_text = "Clients avec un revenu annuel élevé mais de faibles dépenses annuelles : Ce Client appartient au cluster n° 2"
        elif result == 2:
            result_text = "Clients avec un faible revenu annuel et de faibles dépenses annuelles : Ce Client appartient au cluster n° 3"
        elif result == 3:
            result_text = "Clients à faible revenu annuel mais dépenses annuelles élevées : Ce Client appartient au cluster n° 4"
        elif result == 4:
            result_text = "Clients avec un revenu annuel élevé et des dépenses annuelles élevées : Ce Client appartient au cluster n° 5"
        else:
            result_text = "Résultat invalide"

    return render_template('index.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)

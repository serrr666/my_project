from flask import Flask, request
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
 
@app.route('/registration_office', methods=['GET', 'POST'])
 
def patients():
    if request.method == "GET":
        return {
            'сообщение': 'Список пациентов',
            'метод': request.method
        }
    if request.method == "POST":
        return {
            'сообщение': 'Добавляем нового пациента',
            'данные ': request.json,
            'метод': request.method
            }
 
@app.route('/registration_office/<int:patient_id>', methods=['GET', 'PUT', 'DELETE'])
def patient(patient_id):
    if request.method == "GET":
        return {
            'id': patient_id,
            'сообщение': 'Данные о пациенте {}'
            .format(patient_id),
            'метод': request.method
        }
    if request.method == "PUT":
        return {
            'id': patient_id,
            'сообщение': 'Обновлем данные пациента {}'
            .format(patient_id),
            'метод': request.method,
        'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': patient_id,
            'сообщение': 'Удаляем данные пациента {}'
            .format(patient_id),
            'метод': request.method
        }
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
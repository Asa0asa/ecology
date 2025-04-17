from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  """Отображает главную страницу."""
  return render_template('index.html')

@app.route('/2')
def reason():
  """Отображает страницу с причинами глобального потепления."""
  return render_template('reasons.html')

@app.route('/3')
def consequence():
  """Отображает страницу с последствиями глобального потепления."""
  return render_template('consequences.html')


@app.route('/5')
def abouts():
  """Отображает страницу "О нас"."""
  return render_template('about.html')

@app.route('/privacy-policy')
def privacy_policy():
    """Отображает страницу политики конфиденциальности."""
    return render_template('privacy_policy.html')

@app.route('/terms-of-service')
def terms_of_service():
    """Отображает страницу условий использования."""
    return render_template('terms_of_service.html')




# Вопросы викторины (вопрос, варианты ответов, правильный ответ)
questions = [
    {
        "question": "Что такое глобальное потепление?",
        "options": [
            "Временное повышение температуры в одном регионе",
            "Долгосрочное повышение средней температуры Земли",
            "Естественное колебание температуры океана",
            "Уменьшение количества осадков"
        ],
        "answer": "Долгосрочное повышение средней температуры Земли"
    },
    {
        "question": "Какова основная причина глобального потепления?",
        "options": [
            "Увеличение солнечной активности",
            "Извержения вулканов",
            "Выбросы парниковых газов в результате деятельности человека",
            "Изменение орбиты Земли"
        ],
        "answer": "Выбросы парниковых газов в результате деятельности человека"
    },
    {
        "question": "Какие газы в наибольшей степени способствуют парниковому эффекту?",
        "options": [
            "Кислород и азот",
            "Углекислый газ, метан и закись азота",
            "Аргон и гелий",
            "Водород и гелий"
        ],
        "answer": "Углекислый газ, метан и закись азота"
    },
    {
        "question": "Какое из следующих последствий НЕ связано с глобальным потеплением?",
        "options": [
            "Повышение уровня моря",
            "Увеличение частоты и интенсивности экстремальных погодных явлений (засухи, наводнения, ураганы)",
            "Таяние ледников и полярных шапок",
            "Увеличение популяции пингвинов"
        ],
        "answer": "Увеличение популяции пингвинов"
    },
    {
        "question": "Какой сектор экономики вносит наибольший вклад в выбросы парниковых газов?",
        "options": [
            "Сельское хозяйство",
            "Транспорт",
            "Энергетика",
            "Обрабатывающая промышленность"
        ],
        "answer": "Энергетика"
    }
]


@app.route("/6", methods=["GET", "POST"])
def quizs():
    if request.method == "POST":
        score = 0
        results = []
        for i, question in enumerate(questions):
            selected_answer = request.form.get(f"question{i}")
            is_correct = selected_answer == question["answer"]
            if is_correct:
                score += 1
            results.append({"question": question["question"],
                             "selected_answer": selected_answer,
                             "correct_answer": question["answer"],
                             "is_correct": is_correct})

        return render_template("result.html", score=score, total_questions=len(questions), results=results)
    else:
        return render_template("quiz.html", questions=questions) # <---- Здесь важно передать 'questions'


@app.route("/4") # Пример, измените в соответствии с вашим кодом
def results():
    #  Если results() должна отображать викторину, то перенаправьте на quiz()
    return render_template('quiz.html')


if __name__ == '__main__':
  app.run(debug=True)


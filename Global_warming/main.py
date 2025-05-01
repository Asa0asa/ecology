from flask import Flask, render_template, request


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



# Вопросы викторины (вопрос, варианты ответов, правильный ответ)
questions = [
    {
        'question': 'Что такое глобальное потепление?',
        'options': ['Долгосрочное понижение средней температуры Земли.', 'Долгосрочное повышение средней температуры климатической системы Земли.', 'Краткосрочное изменение температуры на Земле.'],
        'answer': 1
    },
    {
        'question': 'Какое явление является прямым следствием глобального потепления?',
        'options': ['Уменьшение количества ураганов.', 'Увеличение площади ледников.', 'Повышение уровня моря.'],
        'answer': 2
    },
    {
        'question': 'Что является одним из основных факторов, способствующих глобальному потеплению?',
        'options': ['Выбросы парниковых газов в атмосферу.', 'Уменьшение солнечной активности.', 'Увеличение площади лесов.'],
        'answer': 0
    }
]



@app.route('/4')
def qui():
    return render_template('quiz.html', questions=questions)


@app.route('/result', methods=['POST'])
def results():
    score = 0
    for i, question in enumerate(questions):
        answer = int(request.form.get(f'question-{i}'))
        if answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))



if __name__ == '__main__':
  app.run(debug=True)


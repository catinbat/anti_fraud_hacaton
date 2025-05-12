- Python 3.9+ (рекомендуется 3.10)

requirements.txt, main.py, catboost_final_model.joblib должны лежать рядом

Необходимые для запуска команды в терминале:

pip install -r requirements.txt
uvicorn main:app --reload

Адрес в браузере после запуска:
http://127.0.0.1:8000/docs


Пример запроса:
{
  "mean_percent_of_ordered_items": 75.0,
  "DaysAfterRegistration": 500,
  "count_items": 3,
  "NmAge": 200,
  "avg_unique_purchase": 0.8
}


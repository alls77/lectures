From python:3
Workdir /usr/src/app/
Copy . .
#v moment sborki
RUN pip install --no-input -r requirements.txt
Expose 5000
CMD ["python", "./manage.py", "runserver", "0.0.0.0:5000"]
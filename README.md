In [2]: models.Car.objects.all()
Out[2]: <QuerySet [<Car: LADA>, <Car: BMW>]>

In [3]: list(models.Car.objects.all())
Out[3]: [<Car: LADA>, <Car: BMW>]

In [4]: list(models.Student.objects.all())
Out[4]: [<Student: Ахмадиев Айдар>, <Student: Иванов Иван>]

In [5]: list(models.Car.objects.all())
Out[5]: [<Car: LADA>, <Car: BMW>, <Car: Volvo>, <Car: Nissan>, <Car: Lexus>]

In [6]: models.Car.objects.first()
Out[6]: <Car: LADA>

In [7]: models.Car.objects.last()
Out[7]: <Car: Lexus>

In [8]: models.Car.objects.count()
Out[8]: 5

In [9]: models.Car.objects.order_by('car_name')
Out[9]: <QuerySet [<Car: BMW>, <Car: LADA>, <Car: Lexus>, <Car: Nissan>, <Car: Volvo>]>

In [10]: models.Car.objects.order_by('-car_name')
Out[10]: <QuerySet [<Car: Volvo>, <Car: Nissan>, <Car: Lexus>, <Car: LADA>, <Car: BMW>]>

In [11]: models.Car.objects.filter(car_name__contains='A')
Out[11]: <QuerySet [<Car: LADA>, <Car: Nissan>]>

In [12]: models.Car.objects.filter(car_name__exact='LADA')
Out[12]: <QuerySet [<Car: LADA>]>

In [13]: models.Car.objects.filter(car_name__iexact='lada')
Out[13]: <QuerySet [<Car: LADA>]>

In [14]: models.Student.objects.all()
Out[14]: <QuerySet [<Student: Ахмадиев Айдар>, <Student: Иванов Иван>]>

In [15]: models.Student.objects.filter(grade__lte=5)
Out[15]: <QuerySet [<Student: Ахмадиев Айдар>, <Student: Иванов Иван>]>

In [16]: models.Student.objects.filter(grade__lt=3)
Out[16]: <QuerySet [<Student: Иванов Иван>]>

In [17]: models.Student.objects.filter(grade__gt=3)
Out[17]: <QuerySet [<Student: Ахмадиев Айдар>]>

In [18]: models.Student.objects.latest('age')
Out[18]: <Student: Ахмадиев Айдар>

In [19]: models.Student.objects.earliest('age')
Out[19]: <Student: Иванов Иван>

In [20]: models.Car.objects.filter(car_body__exact='saloon')
Out[20]: <QuerySet [<Car: BMW>, <Car: Nissan>, <Car: Lexus>]>

In [21]: models.Car.objects.values("car_name", "car_body")
Out[21]: <QuerySet [{'car_name': 'LADA', 'car_body': 'estate'}, {'car_name': 'BMW', 'car_body': 'saloon'}, {'car_name': 'Volvo', 'car_body': 'estate'}, {'car_name': 'Nissan', 'car_body': 'saloon'}, {'car_name': 'Lexus', 'car_body': 'saloon'}]>

In [22]: models.Car.objects.get(id=5)
Out[22]: <Car: Lexus>

In [23]: models.Car.objects.get(id=1)
Out[23]: <Car: LADA>

In [24]: models.Car.objects.filter(id=6).exists()
Out[24]: False

In [25]: models.Car.objects.create(car_name='AUDI')
Out[25]: <Car: AUDI>


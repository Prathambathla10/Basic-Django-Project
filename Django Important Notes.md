# Django Important Notes







### Ways to create object in Django models:



1st way: car = Car (name="Rolls Royce", max\_speed= 200)

&nbsp;	 car.save()





2nd way: car= Car.objects.create (name="Rolls Royce", max\_speed= 200)





3rd way: car\_dict = {"name" : "Rolls Royce", "max\_speed" : 200}

&nbsp;	 Car.objects.create (\*\*car\_dict)


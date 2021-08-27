import circle
#from circle import areaOfCircle, piUptoDecimal

radius=5
print("Area of Circle with Radius ",radius," is : ",circle.areaOfCircle(radius))
print(circle.piUptoDecimal)
print("Gloabls keys : ",globals().keys())
print("Local keys : ",locals().keys())
print(circle.areaOfCircle.__doc__)
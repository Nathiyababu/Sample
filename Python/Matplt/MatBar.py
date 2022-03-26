import matplotlib.pyplot as plt

x=["science","maths","English"]
h=[200,300,500]
c=["red","green","orange"]
plt.bar(x,h,width=0.5,color=c)
plt.xlabel("Courses")
plt.ylabel("Students Enrolled")
plt.title("Studetns enrolled for different courses 2021")
plt.show()
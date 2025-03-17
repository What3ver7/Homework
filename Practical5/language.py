import matplotlib.pyplot as plt
dict={"TypeScript":"38.5%",
      "SQL":"51%",
      "Python":"51%",
      "HTML":"52.9%",
      "JavaScript":"62.3%",
       }
x=list(dict.keys())
y =[float(value.strip('%')) for value in dict.values()]
plt.bar(x,y)
plt.yticks(range(0,100,10))
for i, value in enumerate(y):
    plt.text(i, value, f"{value}%",ha="center", va="bottom")
plt.xlabel("Application")
plt.ylabel("Percentage")
plt.title("Programming language popularity")
plt.show()
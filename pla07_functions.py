#a = 3
#b = 4
#c = (a*a + b*b) ** 0.5
#print(c)


def hypot(cathet1, cathet2):
    result = cathet1 * cathet1 + cathet2 * cathet2
    result = result ** 0.5
    return result

def cathet(hipotenuza, another_cathet):
    return (hipotenuza ** 2 - another_cathet ** 2) **0.5
if __name__ == "__name__":

    print(hypot(3,4))
    print(cathet(5,4))

    print(__name__)
def valor(z):
    if z >= 0:
        return 1
    else:
        return 0    
n = 0.1
y = 0
w1 = 0
b = 0
x1 = 0
d = 0
fila  = 1
x = 1
epoca = 1   

#Modificable (esto representa la tabla)
while x <= 100:
    if fila == 3:
        fila = 1
    if fila == 1:
        print("Época", epoca)
        epoca += 1
        x1 = 0
        d = 1
    if fila == 2:
        x1 = 1
        d = 0

        
    z = (w1 * x1) + b
    y = valor(z)
    error = d - y
    if error != 0:
        w1 = w1 + n * error * x1
        b = b + n * error
    print("Paso ", x)
    print("w1 = ", w1)
    print("b = ", b)
    print("----------------")
    x += 1
    fila += 1
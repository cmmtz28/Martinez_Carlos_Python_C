"""Desarrollar las primeras líneas en Python creando un formulario en el que te preguntará lo siguiente:
1.	¿Cuál es tu nombre(s)?
2.	¿Cuál es tu primer apellido?
3.	¿Cuál es tu segundo apellido?
4.	¿En qué año naciste?
5.	¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)
"""

año=2023
nom=input("¿Cuál es tu nombre(s)?")
pa=input("¿Cuál es tu primer apellido?")
sa=input("¿Cuál es tu segundo apellido?")
an=input("¿En qué año naciste?")
md=input("¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)")

n_completo=nom+" "+pa+" "+sa
print("Este es tu nombre completo en mayúsculas: "+n_completo.upper())
print("Este es tu nombre completo en minúsculas "+n_completo.lower())

f_n=(md[3:])+"-"+(md[:2])+"-"+str(an)
print("Esta es tu fecha de nacimiento “dd-mm-aaaa”. "+f_n)
edad=int(año)-int(an)
print("Esta es tu edad: "+str(edad))
vocales=0
n_completo=n_completo.lower()
for i in range(0,len(n_completo)):
    if n_completo[i]=="a" or n_completo[i]=="e" or n_completo[i]=="i" or n_completo[i]=="o" or n_completo[i]=="u":
        vocales+=1
    
print("Tu nombre completo tiene "+str(vocales)+" vocales")
n_c=len(nom)+len(pa)+len(sa)
print("Tu nombre completo tiene "+str(n_c)+" letras")

entero=type(edad)==int
print("¿Tu edad es un carácter de tipo número? "+str(entero))
alfa=type(n_completo)==str
print("¿Tu nombre completo es un carácter de tipo alfanumérico? "+str(alfa))
edad+=10
print("Tu edad en 10 años será "+str(edad))
prom=((edad-10)*2+20)/2
print("La media de tu edad actual y tu edad en 20 años es: "+str(prom))

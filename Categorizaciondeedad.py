#Categorizacion segun su edad 

print("catecorizacion por edades")
print()

Edad= int(input("Epecemos!. Intruce tu edad: " ))

if Edad <=12 and Edad >0:
    print("Tu categoria es: Infancia. ")
elif Edad >=13 and Edad <18:
    print("Tu categoria es: Adolescencia. ")
elif Edad >=19 and Edad <39:
    print("Tu categoria es: Adultez. ")
elif Edad >=40 and Edad <59:
    print("Tu categoria es: Edad Media. ")
elif Edad >=60 and Edad <79:
    print("Tu categoria es: Adultez tardia.")
elif Edad >80 and Edad <100:
    print("Tu categoria es: Vejez")
else:
    print("Usted no es Humano")
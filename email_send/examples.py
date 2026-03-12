import smtplib

my_email = "eichhornaureliano.gmz@gmail.com"
password = "fvdl xpfe nvlm usyz"

#-----------------------------------UNA FORMA DE HACERLO-----------------------------------------#
# connection = smtplib.SMTP("smtp.gmail.com")
#
# #activa un protocolo de seguridad es decir, hace que la conexión sea segura
# connection.starttls()
#
# #iniciamos sesion
# connection.login(user= my_email, password= password)
#
# #enviar el correo electronico
# connection.sendmail(from_addr= my_email, to_addrs= "aurelianoeichhorn@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email")
#
# #y por ultimo lo cerramos como si fuese un archivo
# connection.close()



#-----------------------------------OTRA FORMA DE HACERLO(mas fácil)-----------------------------------------#
#de esta forma no usamos el .close()
with smtplib.SMTP("smtp.gmail.com") as connection:

    #activa un protocolo de seguridad es decir, hace que la conexión sea segura
    connection.starttls()

    #iniciamos sesion
    connection.login(user= my_email, password= password)

    #enviar el correo electronico
    connection.sendmail(from_addr= my_email,
                        to_addrs= "lucas22bertola@gmail.com",
                        msg="Subject:Que onda\n\npuuutiiiinnn"
                        )

# import datetime
#
# #now se convierte en un objeto
# now = datetime.datetime.now()
#
# # extraemos sus atributos
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# dia_de_la_semana = now.weekday()
# print(now, "\n", year, month , day, hour, second, dia_de_la_semana)
#
# date_of_birth_day = datetime.datetime()


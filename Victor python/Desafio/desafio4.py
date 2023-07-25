#desafio: Faça um arquivo em python que receba do usuario uma data especifica e retorne o timestam desta data.
import datetime
  
date_example = (input("escolha a data e a hora que você quer converter: "))
date_format = datetime.datetime.strptime(date_example,
                                         "%m/%d/%Y, %H:%M:%S")
unix_time = datetime.datetime.timestamp(date_format)
print(unix_time)

#"8/6/2021, 05:54:8"
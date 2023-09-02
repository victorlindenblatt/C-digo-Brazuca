import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5c75f101c0f2f3a3541b56e0cbaa42ef"
# Your Auth Token from twilio.com/console
auth_token  = "90f7fed7f9450892c29491bff7e6fc50"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} o vendedor: {vendedor}, bateu a meta de Vendas: {vendas}')
        message = client.messages.create(
            to="+5521999999999",
            from_="seu_numero_twillio",
            body=f'No mês de {mes} o vendedor: {vendedor}, bateu a meta de vendas: {vendas}')
        print(message.sid)





# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada

# PROJETO
import pandas as pd
import smtplib

lista_meses = ['janeiro']

# Localizar Coluna e Linha
for mes in lista_meses:
    tabela_vendas = pd.read_excel(r'janeiro.xlsx')
    if (tabela_vendas['Vendas'] > 0).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 0, 'Vendedor']
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 0, 'Vendas']
        email = tabela_vendas.loc[tabela_vendas['Vendas'] > 0, 'Email']
        
lista = [email]
print (lista)

# Mude esses conforme o uso
seu_email = "e-mail"
sua_password = "senha"
  
# Estabelecendo conexão com gmail
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(seu_email, sua_password)
  
# Conseguindo os nomes e e-mails
names = tabela_vendas['Vendedor']
emails = tabela_vendas['Email']
values = tabela_vendas['Vendas']
  
# Relendo os registros de e-mail
for i in range(len(emails)):
  
    # Grave o nome, e-mail e valor do devedor
    name = names[i]
    email = emails[i]
    value = values[i]

    # A mensagem a ser enviada
    message = f"Fala {name} paga o que deve {value}"

    # Envie o E-mail
    server.sendmail(seu_email, [email], message)
  
# Feche o server
server.close()
print('Seu e-mail foi enviado com sucesso!')
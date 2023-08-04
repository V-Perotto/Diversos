Dim nome
nome = InputBox("Digite seu nome")
msgbox ("Seu nome e: " + nome)

Dim name
name = InputBox("Qual o seu nome?", Preencha)
if name = "" then
msgbox("Voce nao digitou nem uma informacao!")
else
msgbox("O nome digitado foi: " + name)
end if

set wsite = CreateObject("wscript.shell")
website = InputBox("meu buscador", "buscador")
if website = "" then
msgbox "Para que seja feita uma busca e preciso digitar algo!"
else
wsite.run "https://www.google.com/search?q=" + website + ""
end if
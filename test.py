import pyperclip
while pyperclip.waitForPaste()[12:21] != 'infoarena':
    print(pyperclip.waitForPaste())

# se si opreste cand ii dai link bun
# TODO: whileul ala sa mearga pana cand ii (infoarena) (pbinfo) sau (codeforces) siteul si apoi sa fie si problema pe site
# dupa ce se opreste ii bagi text box
# Do you want to solve this problem?
# daca e yes, inseamna ca vrea sa foloseasca programul
# daca nu, a copiat din greseala
# si inca o optiune yes (x2) - ceva de genu, ca sa si porneasca editoru preferat

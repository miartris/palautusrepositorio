# Kokemukset copilotista

## Logiikka

En ole juuri käyttänyt agentteja ennen ja tehnyt pääosin käsin.
Joukkueen perusteella suodatetun pelaajien listan lueteltuna pisteidentekijöiden mukaan agentti suoritti mutkattomasti. Ongelmia syntyi kun pyydettiin integroimaan mainiin. Joukkueiden tulostus oli rikki ja agentti yritti lisätä joukkueita settiin joka oli määritelty silmukan sisällä eli muuttuja oli lokaali ja pyyhkyityi joka loopilla.

VS coden autofill ehdotukset usein aika kauheita ja häiritseviä.

## Testit

Agentti meinasi ensin ryhtyä tekemään unittest kirjastolla. Uudella promptilla sen sai käyttämään pytestiä. Se kirjoitti testit mutta sai väärin importteja minkä takia moduuleja ei ensiksi löytynyt ja pukkasi erroria.

## Lint

Agentti onnistui parilla iteraatiolla refaktoroimaan ja korjaamaan pylintin valitukset. Sovellus toimii, mutta tulostus muuttui hieman. Testit saattoivat auttaa agenttia säilyttämään sovelluslogiikan ennallaan vaikka refaktorointia oli aika paljon.
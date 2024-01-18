# Projekta uzdevums

## **Nosaukums:** My Fitness App

### **Apraksts:**
Projekta uzdevums ir izvedot treniņa plānu atkarībā no lietotāja vēlmēm, piemēram, kuras ķermeņa daļas vēlas stiprināt un cik vingrinājumus noteiktai ķermeņa daļai vēlas izpildīt. Programma nejauši izvēlas noteiktā ķermeņa grupas vingrinājumus, izvada to nosaukumu, kā vingrinājums jāizpilda un, cik reizes vingrinājums jāizpilda.

### Galvenie funkcionalitātes elementi:
1. **Vingrinājumu Atlasīšana:**
- Lietotājs var atlasīt vingrinājumus atbilstoši vēlamajām ķermeņa daļām.
2. **Treniņa Pāna Izveide:** 
- Lietotājs var izveidot savu treniņa plānu, norādot vingrinājumu skaitu.
3. **Informācija:**
 - Par katru vingrinājumu, lietotājam tiek sniegts izpildes skaidrojums, un vēlamais vingrinājuma izpildes skaits.

### Izmantotās bibliotēkas:

Pandas ir plaši izmantota Python bibliotēka datu apstrādei un analīzei. Es to izmantoju, lai nolasītu datus no xlsx faila. Varēju arī izvēlēties strādāt ar bibliotēku openpyxl, bet strādāt ar pandas man šķita vieglāk.
Random moduli var izmantot, lai veiktu nejaušas darbības, piemēram, ģenerētu nejaušus skaitļus, vai manā programmā, lai izvēlētos nejaušus vingrinājumus no saraksta. Es gribēju, lai programma neprasa īsti nekādus jautājumus, bet vienkārši izvada vairākus nejaušus vingrinājumus no noteiktās ķermeņa daļas vingrinājumu saraksta, tieši tāpēc arī izmantoju tieši šo metodi.

### Programmatūras izmantošanas metodes:

1. **Izveido treniņa programmu:**
- Ievadi ķermeņa daļas, kuras vēlies trenēt.
- Norādi vingrinājumu skaitu katrai ķermeņa daļai.
2. **Skaties rezultātu:**
- Programma izvadīs vingrinājuma nosaukumu, aprakstu kā vingrinājumu izpildīt un cik reizes vingrinājums jāpilda.
### Programmas izpildes piemērs:

Ievadi ķermeņa daļas, kuras šodien vēlies stiprināt (atdalot ar komatu, bez atstarpes): *Kājas,Rokas*

Ievadi vēlamo vingrinājumu skaitu katrai ķermeņa daļai (atdalot ar komatu, bez atstarpes): *2,1*

**Kājas** - Izklupieni
- Izpilde: Sākums stāvus, ieelpojiet un speriet lielu soli uz priekšu, saglabājot taisnu muguru. Nolaidieties lejup, līdz ceļgals saliekts vismaz 90 grādu leņķī. Atgriezieties sākuma stāvoklī. To pašu jādara ar otru kāju.
- Reizes: 3x12

**Kājas** - Wall sit
- Izpilde: Mugura pret sienu, ar kājām plecu platumā un aptuveni 2 pēdu attālumā no sienas. Ar muguru jāslīd lejup pa sienu līdz augšstilbi ir paralēli zemei, jeb veido 90 grādus pret sienu. Vēlams pozīciju noturēt vismaz 60 sekundes.
- Reizes: 2x60s

**Rokas** - Bench press ar hantelēm
- Izpilde: Horizontāli guļot uz sola, spied hanteles uz augšu. Lejā rokām jāveido 90 grādu leņķis ar zemi.
- Reizes: 3x12

### Papildu informācija:
- Dati par vingrinājumiem tiek nolasīti no Excel faila ('Vingrinajumi.xlsx').

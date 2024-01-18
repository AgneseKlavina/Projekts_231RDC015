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

### Papildu informācija:
- Dati par vingrinājumiem tiek nolasīti no Excel faila ('Vingrinajumi.xlsx').
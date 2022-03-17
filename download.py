# -*- coding: utf-8 -*-
import requests

#vg2 IM
bs = [] #brukerstøtte
ds = [] #driftsstøtte
uv = [] #utvikling


url = 'https://data.udir.no/kl06/v201906/laereplaner-lk20/ITK02-01'


url_ds = 'https://data.udir.no/kl06/v201906/kompetansemaalsett-lk20/KV372'
url_bs = 'https://data.udir.no/kl06/v201906/kompetansemaalsett-lk20/KV373'
url_uv = 'https://data.udir.no/kl06/v201906/kompetansemaalsett-lk20/KV374'


def get_kompetansemaal_as_list(url):
    ret = []
    res = requests.get(url)
    json = res.json()
    for maal in json['kompetansemaal']:
        if maal:
            ret.append(maal['tittel'])
    return ret


print(get_kompetansemaal_as_list(url_uv))


km_ds = ['utforske og beskrive komponenter i en driftsarkitektur', 'planlegge, implementere og drifte fysiske og virtuelle løsninger med segmenterte nettverk', 'gjøre rede for prinsipper og strukturer for skytjenester og virtuelle tjenester', 'administrere brukere, tilganger og rettigheter i relevante systemer', 'utforske og beskrive relevante nettverksprotokoller, nettverkstjenester og serverroller', 'planlegge og dokumentere arbeidsprosesser og IT-løsninger', 'utforske trusler mot datasikkerhet og gjøre rede for dagens trusselbilde og hvordan truslene kan påvirke en åpen samfunnsdebatt og tilliten til demokratiet', 'gjennomføre risikoanalyse av nettverk og tjenester i en virksomhets systemer og foreslå tiltak for å redusere risikoen', 'forenkle og automatisere arbeidsprosesser i utvikling av IT-løsninger', 'planlegge, drifte og implementere IT-løsninger som ivaretar informasjonssikkerhet og gjeldende regelverk for personvern', 'reflektere over og beskrive hvordan brudd på personvernet kan påvirke enkeltmennesker, virksomheter og samfunn', 'utforske dataindustriens miljøavtrykk og vurdere tiltak for å sikre bærekraftige valg i IT-løsninger']
km_bs = ['gjøre rede for og anvende etiske retningslinjer og relevant lovverk i eget arbeid', 'utøve brukerstøtte og veilede i relevant programvare', 'kartlegge behovet for og utvikle veiledninger for brukere og kunder', 'utvikle kursmateriell og gjennomføre kurs i relevante IT-systemer tilpasset en målgruppe', 'bruke og tilpasse kommunikasjonsform og fagterminologi i møte med brukere, kunder og fagmiljø', 'feilsøke og rette feil ved hjelp av feilsøkingsstrategier og relevante rammeverk', 'beskrive og bruke rammeverk for kvalitetssikring av IT-drift', 'beskrive og anvende ulike metoder for å håndtere krevende situasjoner i kontakt med brukere og kunder', 'reflektere over og gjøre rede for hvordan intelligente systemer påvirker bransjen og samfunnet', 'bruke og administrere samhandlingsverktøy som effektiviserer samarbeid og deling av informasjon', 'drøfte hvilke krav og forventninger som stilles til et likeverdig og inkluderende yrkesfellesskap, og beskrive hvilke plikter og rettigheter arbeidsgiver og arbeidstaker har i arbeidslivet']
km_uv = ['vurdere fordeler og ulemper ved ulike programmeringsspråk og velge og anvende relevante programmeringsspråk og algoritmer i eget arbeid', 'lage og begrunne funksjonelle krav til en IT-løsning basert på behovskartlegging', 'vurdere brukergrensesnitt til IT-tjenester og designe tjenester som er tilpasset brukernes behov', 'gjøre rede for hensikten med teknisk dokumentasjon og utarbeide teknisk dokumentasjon for IT-løsninger', 'beskrive og anvende relevante versjonskontrollsystemer i utviklingsprosjekter', 'designe og implementere IT-tjenester med innebygget personvern', 'analysere digitale trusler, verdier og sårbarheter og utvikle applikasjoner med innebygget sikkerhet', 'anvende relevant testmiljø og utføre testing tilpasset IT-løsningen som utvikles', 'modellere og opprette databaser for informasjonsflyt i systemer', 'beskrive ulike datalagringsmodeller og metoder for å hente ut og sette inn bestemte data fra databaser som brukes av andre systemer']

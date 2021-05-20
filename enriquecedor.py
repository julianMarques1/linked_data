from rdflib import Graph, Literal

def ah_the_negociator():
    pass

graphinho = Graph()
graphinho.parse("links.ttl", format="turtle")

for statequieto in graphinho:
    if not isinstance(statequieto[2], Literal):
        continue
    #link_a_dpedia = statequieto[2].toPython()
    #toa_la_data = ah_the_negociator(link_a_dpedia)
    dbpedia = Graph()
    dbpedia.parse("https://dbpedia.org/resource/Aaron_Taylor-Johnson")
    print(dbpedia.serialize(format="turtle"))
    break
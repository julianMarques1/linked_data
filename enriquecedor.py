from rdflib import Graph, Literal, Namespace
from rdflib.namespace import OWL
from urllib.request import urlopen, Request


def get_link_to_data(resource):
    "Returns 'https://dbpedia.org/data/...'"

    return urlopen(
        Request(resource, headers={"Accept": "application/rdf+xml"})
    )


def main():
    dbo = Namespace("http://dbpedia.org/ontology/")
    prov = Namespace("http://www.w3.org/ns/prov#")

    links = Graph()
    links.parse("links.ttl", format="turtle")

    output = Graph()
    output.parse("dataset-original.ttl", format="turtle")
    output += links

    proprieties = [dbo.birthDate, dbo.occupation, prov.wasDerivedFrom]

    for stmt in links:
        if stmt[1] != OWL["sameAs"]:
            continue

        actor = Graph()
        actor.parse(get_link_to_data(stmt[2].toPython()))

        for property in proprieties:
            output += actor.triples((None, property, None))

    output.serialize(
        "dataset-enriquecido.ttl", format="turtle", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

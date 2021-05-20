from rdflib import Graph, Literal
from rdflib.namespace import OWL
from urllib.request import urlopen, Request


def get_link_to_data(resource):
    "Returns 'https://dbpedia.org/data/...'"

    return urlopen(
        Request(
            resource,
            headers={
                "Accept": "application/rdf+xml",
            },
        )
    )


def main():
    links = Graph()
    links.parse("links.ttl", format="turtle")

    output = Graph()
    output.parse("dataset-original.ttl", format="turtle")
    output.parse("links.ttl", format="turtle")

    proprieties = {}

    for stmt in links:
        if stmt[1] != OWL["sameAs"]:
            continue

        actor = Graph()
        actor.parse(get_link_to_data(stmt[2].toPython()))

        # output.add((individual, OWL.birthDate, actor[aca va el nombre de la propiedad]))
        # output.add((individual, OWL.propiedad, dbpedia[aca va el nombre de la propiedad]))
        # output.add((individual, OWL.propiedad, dbpedia[aca va el nombre de la propiedad]))

    output.serialize(
    "dataset-enriquecido.rdf", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python

"""Vendored from https://github.com/bruvellu/worms.py (MIT License).

Client to access the web services of the WoRMS database
(http://www.marinespecies.org/).
"""

from suds import null, WebFault
from suds.client import Client
import logging

logger = logging.getLogger("worms")
logger.setLevel(logging.DEBUG)
logger.propagate = False
formatter = logging.Formatter(
    "[%(levelname)s] %(asctime)s @ %(module)s %(funcName)s (l%(lineno)d): %(message)s"
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(console_handler)


class Aphia:
    """WoRMS interactor."""

    def __init__(self):
        self.url = "http://www.marinespecies.org/aphia.php?p=soap&wsdl=1"
        logger.info("Initiating contact with WoRMS...")
        try:
            self.client = Client(self.url)
            logger.info("Connected to WoRMS web services.")
        except Exception:
            print("Could not connect to client!")
            self.client = None

    def wire(self, service, query, attempt=0):
        """Manage re-connections between client and WoRMS."""
        try:
            results = service(query)
        except Exception:
            while attempt < 3:
                logger.warning("Could not connect... try=%d" % attempt)
                attempt += 1
                return self.wire(service, query, attempt)
            logger.critical("Closing up the connection. I failed.")
            results = None
        return results

    def get_aphia_id(self, query):
        logger.info('Searching for the name "%s"', query)
        return self.wire(self.client.service.getAphiaID, query)

    def get_aphia_records(self, query):
        logger.info('Searching for the name "%s"', query)
        results = self.wire(self.client.service.getAphiaRecords, query)
        self.show_results(results)
        return results

    def get_aphia_name_by_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaNameByID, query)

    def get_aphia_record_by_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaRecordByID, query)

    def get_aphia_record_by_external_id(self, query, dbtype=""):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaRecordByExtID, query)

    def get_external_id_by_aphia_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getExtIDbyAphiaID, query)

    def get_aphia_records_by_names(self, query):
        logger.info('Searching for the name(s) "%s"', query)
        return self.wire(self.client.service.getAphiaRecordsByNames, query)

    def get_aphia_records_by_vernacular(self, query):
        logger.info('Searching for the name "%s"', query)
        return self.wire(self.client.service.getAphiaRecordsByVernacular, query)

    def get_aphia_records_by_date(self, query):
        logger.info('Searching between dates "%s"', query)
        return self.wire(self.client.service.getAphiaRecordsByDate, query)

    def get_aphia_classification_by_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaClassificationByID, query)

    def get_sources_by_aphia_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getSourcesByAphiaID, query)

    def get_aphia_synonyms_by_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaSynonymsByID, query)

    def get_aphia_vernaculars_by_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaVernacularsByID, query)

    def get_aphia_children_by_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaChildrenByID, query)

    def match_aphia_records_by_names(self, query):
        logger.info('Searching for the name(s) "%s"', query)
        return self.wire(self.client.service.matchAphiaRecordsByNames, query)

    def get_aphia_distributions_by_id(self, query):
        logger.info('Searching for the ID "%s"', query)
        return self.wire(self.client.service.getAphiaDistributionsByID, query)

    def show_results(self, results):
        if results:
            logger.info("Found {} record(s)".format(len(results)))
            for result in results:
                self.print_record(result)
        else:
            logger.info("Found no records.")

    def print_record(self, record, pre=""):
        logger.info(
            "{0}{1} / {2} / {3} / {4} / {5}".format(
                pre,
                record["AphiaID"],
                record["scientificname"],
                record["authority"],
                record["rank"],
                record["status"],
            )
        )

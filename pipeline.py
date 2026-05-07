from enrichment.census import enrich_census
from enrichment.fred import enrich_vacancy_rate
from enrichment.places import enrich_property
from enrichment.score import score_and_reasoning
from sheets import get_new_leads, write_back


def process_new_leads():
    leads = get_new_leads()
    for _, lead in leads:
        try:
            enrich_census(lead)
            enrich_vacancy_rate(lead)
            enrich_property(lead)
            score_and_reasoning(lead)
            lead["Status"] = "Done"
        except Exception as e:
            lead["Status"] = "Error"
            lead["Error"] = f"{type(e).__name__}: {e}"

    write_back(leads)
    return leads




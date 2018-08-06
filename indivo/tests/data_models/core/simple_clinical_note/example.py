from indivo.models import SimpleClinicalNote
from indivo.lib.iso8601 import parse_utc_date as date

simple_clinical_note_fact = SimpleClinicalNote(
    date_of_visit=date("2010-02-02T12:00:00Z"),
    finalized_at=date("2010-02-03T13:12:00Z"),
    visit_type="Acute Care",
    visit_type_type="http://codes.indivo.org/visit-types#",
    visit_type_value="123",
    visit_type_abbrev="acute",
    visit_location="Longfellow Medical",
    specialty="Hematology/Oncology",
    specialty_type="http://codes.indivo.org/specialties#",
    specialty_value="234",
    specialty_abbrev="hem-onc",
    signed_at=date("2010-02-03T13:12:00Z"),
    provider_name="Kenneth Mandl",
    provider_institution="Children's Hospital Boston",
    chief_complaint="stomach ache",
    content="Patient presents with ..."
    )


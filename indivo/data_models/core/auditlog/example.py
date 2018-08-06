from indivo.models import Auditlog
from indivo.lib.iso8601 import parse_utc_date as date

auditlog_fact = Auditlog(
    timestamp=date("2016-05-16T12:00:00Z"),
    app_name =CodedValueField,# "imcportal",
    app_module="test",
    event_name="test",
    patient="161891005",
    country=CodedValueField,#"italy",
    event_parameter="test",
    flag=0,
    )


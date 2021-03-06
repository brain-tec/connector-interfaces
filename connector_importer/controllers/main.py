# Author: Simone Orsi
# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request
from ..utils.report_html import Reporter


class ReportController(http.Controller):
    """Controller to display import reports."""

    # TODO: refactor this to use qweb template only
    @http.route(
        '/importer/import-recordset/<model("import.recordset"):recordset>',
        type='http', auth="user", website=False)
    def full_report(self, recordset, **kwargs):
        reporter = Reporter(recordset.jsondata, detailed=1)
        values = {
            'recordset': recordset,
            'report': reporter.html(wrapped=0),

        }
        return request.render("connector_importer.recordset_report", values)

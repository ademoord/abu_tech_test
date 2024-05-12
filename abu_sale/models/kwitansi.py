from odoo import models, fields, api
from datetime import datetime
import num2words

class AbuKwitansiInvoice(models.Model):
    _name = 'abu.kwitansi'

    invoice_id = fields.Many2one('account.move', string='No Trans')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    date = fields.Date(string='Tanggal')
    printing_time = fields.Char(string='Jam Cetak', compute='_compute_printing_time')
    nis = fields.Char(string='NIS')
    student_name = fields.Char(string='Nama Siswa')
    class_name = fields.Char(string='Kelas')
    terbilang = fields.Char(string='Terbilang', compute='_compute_terbilang')
    grand_total = fields.Float(string='Grand Total', compute='_compute_grand_total')
    kwitansi_line_ids = fields.One2many('abu.kwitansi.line', 'kwitansi_id', string='Kwitansi Lines')

    @api.depends('date')
    def _compute_printing_time(self):
        for record in self:
            record.printing_time = datetime.now().strftime('%H:%M:%S')

    @api.depends('kwitansi_line_ids.price_total')
    def _compute_terbilang(self):
        for record in self:
            total = sum(line.price_total for line in record.kwitansi_line_ids)
            record.terbilang = num2words.num2words(total, lang='id')

    @api.depends('kwitansi_line_ids.price_total')
    def _compute_grand_total(self):
        for record in self:
            record.grand_total = sum(line.price_total for line in record.kwitansi_line_ids)

    def action_print_kwitansi(self):
        context = {'company': self.env.company}
        report_template = self.env['ir.actions.report'].search([('report_name', '=', 'abu_sale.report_abu_kwitansi')])
        if report_template:
            return report_template.with_context(context).report_action(self)
        else:
            report_template = self.env['ir.actions.report'].create({
                'report_name': 'abu_sale.report_abu_kwitansi',
                'model': 'abu.kwitansi',
                'name': 'ABU Kwitansi Report'
            })
            return report_template.with_context(context).report_action(self)


class AbuKwitansiLine(models.Model):
    _name = 'abu.kwitansi.line'

    kwitansi_id = fields.Many2one('abu.kwitansi', string='Kwitansi')
    no = fields.Char(string='No')
    notes = fields.Char(string='Notes')
    price_total = fields.Float(string='Price Total')

    @api.onchange('price_total')
    def _onchange_price_total(self):
        self.kwitansi_id.grand_total = sum(line.price_total for line in self.kwitansi_id.kwitansi_line_ids)

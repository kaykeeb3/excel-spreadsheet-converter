from flask import Blueprint, request, jsonify, send_file
from ..utils import generate_excel_report
import os

main = Blueprint('main', __name__)

@main.route('/generate-report', methods=['POST'])
def generate_report():
    try:
        # Recebe os dados em formato JSON
        data = request.get_json()

        # Verifica se deve gerar um relatório Excel
        report_type = request.args.get('type', 'excel')  # Verifica se foi fornecido um tipo de relatório, caso contrário, o padrão é 'excel'
        if report_type == 'excel':
            # Gera o relatório em Excel
            report_path = generate_excel_report(data)
        else:
            return jsonify({"error": "Invalid report type. Please specify 'excel'."}), 400

        # Verifica se o arquivo foi realmente criado
        if os.path.exists(report_path):
            return send_file(report_path, as_attachment=True)
        else:
            return jsonify({"error": "Report file was not created."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 400
''
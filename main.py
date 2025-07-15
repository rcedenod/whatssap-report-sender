from dataReader import readSalesData
from financialAnalysis import financialAnalysis, salesBySegment
from reportGenerator import generateSalesPlot, writeReport
from senderWhatssap import sendWhatssap

def main():
    df = readSalesData('Ventas - Fundamentos.xlsx')
    analysis = financialAnalysis(df)
    segmentSales = salesBySegment(df)

    plotPath = generateSalesPlot(segmentSales)
    reportPath = writeReport(analysis, segmentSales, plotPath)

    with open(reportPath) as f:
        reportText = f.read()
    sid = sendWhatssap(reportText)
    print(f'Reporte enviado con SID: {sid}')

if __name__ == '__main__':
    main()
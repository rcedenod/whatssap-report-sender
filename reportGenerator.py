import matplotlib.pyplot as plt
from pathlib import Path

def generateSalesPlot(series, outputPath: str = 'salesBySegment.png') -> str:
    fig, ax = plt.subplots()
    series.plot(kind='bar', ax=ax)
    ax.set_title('Ventas por segmento')
    ax.set_ylabel('Ventas ($)')
    Path(outputPath).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(outputPath)
    plt.close(fig)
    return outputPath

def writeReport(analysisResults: dict, segmentSales, plotPath: str,
                 outputPath: str = 'report.txt') -> str:
    total = analysisResults['totalSales']
    avg = analysisResults['averageSales']
    stats = analysisResults['statistics']

    segmentFmt = segmentSales.map(lambda x: f"${x:,.0f}")

    with open(outputPath, 'w') as f:
        f.write('REPORTE DE VENTAS:\n')
        f.write(f"Total de ventas: ${total:,.0f}\n")
        f.write(f"Promedio de venta: ${avg:,.2f}\n\n")
        f.write('ESTADISTICAS DESCRIPTIVAS\n')
        f.write(stats.to_string(float_format='{:,.2f}'.format))
        f.write('\n\nVENTAS POR SEGMENTOS\n')
        f.write(segmentFmt.to_string())
    return outputPath
import plotly.express as plot
import pandas

def main():
    graph1 = getCubeGraph(5)
    graph1.show()
    graph2 = getCubeGraph(5000)
    graph2.show()

def getCubeGraph(n):
    nrange = range(1, n+1)
    df = pandas.DataFrame({'n' : nrange, 'n^3':[i**3 for i in nrange]})
    return plot.scatter(df, x='n', y='n^3', color='n^3',
        color_continuous_scale="Thermal", title="Cubes from 1 to " + str(n))

if __name__ == "__main__":
    main()

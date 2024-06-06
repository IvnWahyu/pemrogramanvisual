import pandas as pd

def stats_columns(filename, xlabel, ylabel):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        return f"File {filename} not found.", ""
    except pd.errors.EmptyDataError:
        return f"File {filename} is empty.", ""
    except pd.errors.ParserError:
        return f"File {filename} is not a valid CSV.", ""
    
    if xlabel not in df.columns or ylabel not in df.columns:
        return f"Columns {xlabel} or {ylabel} not found in the file.", ""
    
    xdata = df[xlabel]
    ydata = df[ylabel]
    
    xstats = xdata.describe()
    ystats = ydata.describe()
    
    return xstats.to_string(), ystats.to_string()

if __name__ == '__main__':
    print(stats_columns('tempRainYearly.csv', 'Temp', 'Main'))

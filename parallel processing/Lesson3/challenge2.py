import pandas as pd
import math
from concurrent.futures import ProcessPoolExecutor
df = pd.read_csv('parallel processing\Lesson3\googleplaystore.csv')

categories = df['Category'].unique()

def count_categories():
    count_categories_dict = {}
    for category in categories:
        count_categories = df['Category'].str.count(category).sum()
        count_categories_dict[category]=count_categories
    return count_categories_dict

def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)

    chunks = []
    for i in range(0, num_rows, chunk_size):
        chunk = df[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks

if __name__ == '__main__':
    with ProcessPoolExecutor() as exe:
        processes = [exe.submit(count_categories) for chunk in make_chunks(df, 6)]
    results = [process.result() for process in processes]
    [print(result) for result in results]